# from abc import ABC, abstractmethod
import tkinter as tk

# from tkinter import ttk
import os
from layout import Layout
from database import Database
from todo import Todo
from binder import Binder


class Main(Layout, Binder, Todo):
    pass


if __name__ == "__main__":
    if not os.path.isfile("tasks.db"):
        Database.firstTimeDB()
        print("File not present")
    else:
        print("File is present")
    count = 0
    main = Main()
    main.mainloop()
