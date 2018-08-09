# from abc import ABC, abstractmethod
import tkinter as tk

# from tkinter import ttk
import os
from layout import Layout
from database import Database
from todo import Todo
from binder import Binder
from timer import Timer


class Main(Layout, Binder, Todo, Timer):
    pass


if __name__ == "__main__":
    if not os.path.isfile("pymodoro.db"):
        Timer.firstTimeDB()
    if not os.path.isfile("tasks.db"):
        Database.firstTimeDB()
        print("File not present")
    else:
        print("File is present")
    main = Main()
    main.mainloop()
