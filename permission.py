import numpy as np
import random
import pygame
import sys
import math
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk


window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

s = simpledialog.askstring("4Connect", "ENTER THE NAME OF FIRST PLAYER!")
# print(s)

window.deiconify()
window.destroy()
window.quit()

# turn_input = input("Who plays first (AI / PLAYER) : ").upper()

turn_input = str(s).upper()

print(turn_input)

# print(turn_input)
# turn = turn_input

def access():
    if turn_input == "PLAYER":
        return 0
    elif turn_input == "AI":
        return 1
    elif turn_input == "NONE":
        sys.exit()
    else:
        return 0





    




