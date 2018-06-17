from app import App
from database import Database
import tkinter as tk
import tkinter.messagebox as msg


class Todo(App):
    def __init__(self, tasks=None):
        super().__init__()
        db = Database()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        current_tasks = db.load_tasks()
        for task in current_tasks:
            task_text = task[0]
            self.add_task(None, task_text, True)

    def add_task(self, event=None, task_text=None, from_db=False):
        if not task_text:
            task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

            if not from_db:
                db = Database()
                db.save_task(task_text)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        db = Database()
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)

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
