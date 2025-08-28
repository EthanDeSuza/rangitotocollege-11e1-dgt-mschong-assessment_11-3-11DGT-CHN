"""11DGT Assessment 11.3.

stuff for doing the tkinter assessment
"""


import tkinter

def wordle_start():
    root = tk.Tk()
    root.title('Wordle')
    root.geometry('400x600')
    words = []
def blackjack_start():
    root = tk.Tk()
    root.title('BlackJack')
    root.geometry('800x600') 
def snake_start():
    root = tk.Tk()
    root.title('Snake')
    root.geometry('600x600') 
def scoreboard_start():
    root = tk.Tk()
    root.title('Scoreboard')
    root.geometry('600x500')


# This code creates a Tkinter window with a menu bar containing File and Help menus.
import tkinter as tk
root = tk.Tk()
root.title('Games Compendium')
root.geometry('800x450')
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Navigation', menu=filemenu)
filemenu.add_command(label='Scoreboard', command=scoreboard_start)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Game 1 Instructions')
helpmenu.add_command(label='Game 2 Instructions')
helpmenu.add_command(label='Game 3 Instructions')


button = tk.Button(root, text='Wordle', width=10, command=wordle_start)
button.grid(row=1, column=0, sticky = W, pady=50)
button = tk.Button(root, text='BlackJack', width=10, command=blackjack_start)
button.grid(row=1, column=20, sticky = W, pady=50)
button = tk.Button(root, text='Snake', width=10, command=snake_start)
button.grid(row=1, column=40, sticky = W, pady=50)
tk.mainloop()
