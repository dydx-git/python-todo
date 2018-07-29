import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.nb = ttk.Notebook(self)
        self.nb.pack(expand=True, fill=tk.BOTH)
        self.main_frame = tk.Frame(self.nb)
        self.main_frame2 = tk.Frame(self.nb)
        self.text_frame = tk.Frame(self.main_frame)
        self.tasks_frame = tk.Frame(self.main_frame, bg="Blue")
        self.tasks_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.tasks_canvas = tk.Canvas(self.tasks_frame, width=400, height=400, bg="red")
        vbar = tk.Scrollbar(self.tasks_canvas, orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        vbar.config(command=self.tasks_canvas.yview)
        self.tasks_canvas.config(yscrollcommand=vbar.set)
        self.tasks_canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        # self.tasks_canvas = tk.Canvas(self)
        # self.tasks_frame = tk.Frame(self.tasks_canvas)
        # self.text_frame = tk.Frame(self)
        # self.scrollbar = tk.Scrollbar(
        #     self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview
        # )
        # self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        # self.title("Pydot 1.0")
        # self.geometry("300x400")
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.nb.add(self.main_frame, text="Tab 1")
        self.nb.add(self.main_frame2, text="Tab 2")
        # self.canvas_frame = self.tasks_canvas.create_window(
        #     (0, 0), window=self.tasks_frame, anchor="n"
        # )
        # self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]


app = App()
app.mainloop()
