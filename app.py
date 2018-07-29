import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create and pack Notebook
        self.nb = ttk.Notebook(self)
        self.nb.pack(expand=True, fill=tk.BOTH)

        # Create main tasks frame
        self.main_frame = tk.Frame(self.nb)
        self.done_frame = tk.Frame(self.nb)

        # Create and pack text and tasks frame
        self.text_frame = tk.Frame(self.main_frame)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.true_frame = tk.Frame(self.main_frame)
        self.true_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create Canvas and config
        self.tasks_canvas = tk.Canvas(self.true_frame)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.scrollbar = tk.Scrollbar(self.tasks_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.tasks_canvas.yview)
        self.tasks_canvas.config(yscrollcommand=self.scrollbar.set)
        self.tasks_canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Create Canvas and config

        # Create Entry box
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)

        # Add pages to notebook
        self.nb.add(self.main_frame, text="Tasks")
        self.nb.add(self.done_frame, text="Completed Tasks")

        # self.tasks_canvas = tk.Canvas(self)
        # self.tasks_frame = tk.Frame(self.tasks_canvas)
        # self.text_frame = tk.Frame(self)
        # self.scrollbar = tk.Scrollbar(
        #     self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview
        # )
        # self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        # self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="n"
        )
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]
