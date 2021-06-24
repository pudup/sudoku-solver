import tkinter
import math
import os
from playsound import playsound
from tkinter import messagebox
import random
from solverUIHelp import sudoku_solver, pretty_matrix, helperfunc
from time import sleep


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


grid = []


def make_array():
    global grid
    acceptable = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for j in range(9):
        row = []
        for i in range(9):
            if rows[f"{j}" + f"{i}"].get() in acceptable:
                row.append(int(rows[f"{j}" + f"{i}"].get()))
            else:
                row.append(0)
        grid.append(row)


def show_answer():
    global grid
    for j in range(9):
        for i in range(9):
            rows[f"{j}" + f"{i}"].delete(0, len(rows[f"{j}" + f"{i}"].get()))
            rows[f"{j}" + f"{i}"].insert(0, str(grid[j][i]))


def solve():
    global grid
    make_array()
    sudoku_solver(grid)
    show_answer()


my_window = tkinter.Tk()
my_window.title("Didi Solve Solve")
my_window.config(width=600, height=600, padx=60, pady=50, )

my_canvas = tkinter.Canvas(width=600, height=600, highlightthickness=0)
grid_image = tkinter.PhotoImage(file=resource_path("backgr6.png"))
my_canvas.create_image(300, 300, image=grid_image)
my_canvas.grid(column=4, row=4)

rows = {}
windows = {}

for j in range(9):
    for i in range(9):
        entry = tkinter.Entry(width=2)
        # entry.insert(tkinter.END, f"{j}" + f"{i}")
        # entry.insert(tkinter.END, 0)
        rows[f"{j}" + f"{i}"] = entry
        entry_window = my_canvas.create_window((i + 1) * 60, (j + 1) * 60, window=rows[f"{j}" + f"{i}"])
        windows[f"{j}" + f"{i}"] = entry_window

solve_button = tkinter.Button(text="Solve Puzzle", highlightthickness=0, command=solve)
solve_window = my_canvas.create_window(300, 610, window=solve_button)

my_window.mainloop()
