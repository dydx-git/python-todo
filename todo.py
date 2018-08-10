from app import App
from database import Database
import tkinter as tk
import tkinter.messagebox as msg
from timer import Timer


class Todo(App):
    def __init__(self, tasks=None):
        super().__init__()
        db = Database()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.task_name_entry.insert(0, "No Task Selected")
        current_tasks = db.load_tasks()
        for task in current_tasks:
            task_text = task[0]
            self.add_task(False, None, task_text, True)
        completed_tasks = db.load_completed_tasks()
        for task in completed_tasks:
            if task[0] == None:
                pass
            else:
                task_text = task[0]
                self.add_task(True, None, task_text, True)

    def add_task(self, isComplete=False, event=None, task_text=None, from_db=False):
        if isComplete == True:
            if len(task_text) > 0:
                new_task = tk.Label(self.c_tasks, text=task_text, pady=10)

                self.set_task_colour(len(self.tasks), new_task)

                new_task.bind("<Double-Button-1>", lambda event: self.delete_task(event, new_task))
                new_task.pack(side=tk.TOP, fill=tk.X)
                self.tasks.append(new_task)

                if not from_db:
                    db = Database()
                    db.save_task(task_text)
        else:
            if not task_text:
                task_text = self.task_create.get(1.0, tk.END).strip()

            if len(task_text) > 0:
                new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

                self.set_task_colour(len(self.tasks), new_task)

                new_task.bind("<Double-Button-1>", self.complete_task)
                new_task.bind("<Button-1>", self.pass_task)
                new_task.pack(side=tk.TOP, fill=tk.BOTH)
                del_btn = tk.Button(new_task, text="Delete")
                del_btn.bind("<Button-1>", lambda event: self.delete_task(event, new_task))
                del_btn.pack(side=tk.RIGHT, padx=15)
                self.tasks.append(new_task)

                if not from_db:
                    db = Database()
                    db.save_task(task_text)

            self.task_create.delete(1.0, tk.END)

    def pass_task(self, event):
        self.task_name_entry.config(state=tk.NORMAL)
        self.task_name_entry.delete(0, "end")
        self.task_name_entry.insert(0, event.widget.cget("text"))
        self.task_name_entry.config(state="readonly")

    def delete_task(self, event, task):
        db = Database()
        delete_task_query = "DELETE FROM tasks WHERE task=?"
        delete_task_data = (task.cget("text"),)
        db.runQuery(delete_task_query, delete_task_data)
        task.destroy()

    def complete_task(self, event):
        db = Database()
        task = event.widget
        self.tasks.remove(event.widget)
        db.complete_task(task.cget("text"))
        delete_task_query = "DELETE FROM tasks WHERE task=?"
        delete_task_data = (task.cget("text"),)
        db.runQuery(delete_task_query, delete_task_data)
        event.widget.destroy()

        self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])
