"""11DGT Assessment 11.3.

stuff for doing the tkinter assessment
"""


import tkinter
load = False
def wordle_start():
    root = tk.Tk()
    root.title('Wordle')
    root.geometry('400x600')
    root.resizable(False, False)
    words = []
def blackjack_start():
    root = tk.Tk()
    root.title('BlackJack')
    root.geometry('800x600') 
    root.resizable(False, False)
def snake_start():
    root = tk.Tk()
    root.title('Snake')
    root.geometry('600x600') 
    root.resizable(False, False)
def scoreboard_start():
    root = tk.Tk()
    root.title('Scoreboard')
    root.geometry('600x500')
    root.resizable(False, False)
    
# This code creates a Tkinter window with a menu bar containing File and Help menus.
def create_menu():
    load = True
    root = tk.Tk()
    root.title('Games Compendium')
    root.geometry('800x450')
    root.resizable(False, False)
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


    button = tk.Button(root, text='Wordle', width=20, command=wordle_start)
    button.grid(row=0, column=0, columnspan=2)
    button = tk.Button(root, text='BlackJack', width=20, command=blackjack_start)
    button.grid(row=0, column=2, columnspan=2)
    button = tk.Button(root, text='Snake', width=20, command=snake_start)
    button.grid(row=0, column=4, columnspan=2, padx=5, pady=5)
    tk.mainloop()

# Part of progress bar code for progressign the bar
def start_progress():
    if pg['value']< 100:
        pg['value'] += 1
        root.after(50, start_progress)
    else:
        root.destroy()
        create_menu()

if load == False:
# This code creates a Tkinter window with a progress bar that simulates loading up the games compendium.
    import tkinter as tk
    from tkinter import ttk
    root = tk.Tk()
    root.title('Games Compendium')
    tk.Label(root, text="Loading...").pack(pady=20)
    root.geometry('800x450')
    root.resizable(False, False)
    # Create a progressbar widget
    pg = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
    pg.pack(pady=20)
    start_button = ttk.Button(root, text="Start Progress", command=start_progress)
    start_button.pack()
    root.mainloop()


