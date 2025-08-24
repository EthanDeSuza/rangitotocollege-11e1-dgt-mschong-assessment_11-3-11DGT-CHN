"""11DGT Assessment 11.3.

stuff for doing the tkinter assessment
"""


import tkinter

# This code creates a Tkinter window with a menu bar containing File and Help menus.
from tkinter import *
root = Tk()
root.title('Games Compendium')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Navigation', menu=filemenu)
filemenu.add_command(label='Scoreboard')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Game 1 Instructions')
helpmenu.add_command(label='Game 2 Instructions')
helpmenu.add_command(label='Game 3 Instructions')
button = Button(root, text='Now', width=25, command=root.destroy)
button.grid(row=20, column=0, padx=50, pady=50)
button = Button(root, text='Now', width=25, command=root.destroy)
button.grid(row=20, column=20, padx=50, pady=50)
button = Button(root, text='Now', width=25, command=root.destroy)
button.grid(row=20, column=40, padx=50, pady=50)
mainloop()

