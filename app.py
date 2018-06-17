import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview
        )
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.title("Pydot 1.0")
        self.geometry("300x400")
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="n"
        )
        self.colour_schemes = [
            {"bg": "lightgrey", "fg": "black"},
            {"bg": "grey", "fg": "white"},
        ]
