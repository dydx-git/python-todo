from app import App
import tkinter as tk


class Layout(App):
    def __init__(self):
        super().__init__()
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()
