import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super().__init__(parent, *args, **kwargs)
        self.pack(expand=True, fill=tk.BOTH)
        self.inputframe = ttk.Frame(self)
        self.inputframe.pack(side=tk.LEFT, expand=False, fill=tk.Y)
        self.outputnotebook = ttk.Notebook(self)
        self.outputnotebook.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self.build_inputframe()
        self.build_outputnotebook()

    def build_inputframe(self):
        run_button = ttk.Button(self.inputframe, text="Run", command=self.draw)
        run_button.grid(column=2, row=0, sticky=(tk.W, tk.E))
        # rest of app...

    def build_outputnotebook(self):
        actnet_frame = ttk.Frame(self.outputnotebook)
        critnet_frame = ttk.Frame(self.outputnotebook)
        xscrollbar = ttk.Scrollbar(actnet_frame, orient=tk.HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.outputnotebook.add(actnet_frame, text="Tab 1", sticky=tk.N + tk.S + tk.E + tk.W)
        self.outputnotebook.add(critnet_frame, text="Tab 2")
        self.actnet_canvas = tk.Canvas(
            actnet_frame, width=400, height=400, xscrollcommand=xscrollbar.set
        )
        self.actnet_canvas.grid(row=0, sticky=tk.N + tk.S + tk.E + tk.W)
        xscrollbar.config(command=self.actnet_canvas.xview)
        actnet_frame.rowconfigure(0, weight=1)
        actnet_frame.columnconfigure(0, weight=1)

    def draw(self):
        act_image = Image.open("critnet.jpg")  # image is 875 x 175
        width, height = act_image.size
        actphoto = ImageTk.PhotoImage(act_image)
        self.actnet_canvas.delete("all")
        self.actnet_canvas.create_image(0, 0, anchor=tk.NW, image=actphoto)
        self.actnet_canvas.image = actphoto
        self.actnet_canvas["scrollregion"] = (0, 0, width, height)
        # do similar for other tabs.


root = tk.Tk()
root.geometry("800x600")
app = App(root)
app.mainloop()
