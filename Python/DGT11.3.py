"""11DGT Assessment 11.3.

stuff for doing the tkinter assessment
"""


from tkinter import *
from tkinter.ttk import Progressbar
def wordle_start():  # Wordle game window
    root = Tk()
    root.title('Wordle')
    root.geometry('400x600')
    root.resizable(False, False)
    words = []
def blackjack_start():  # BlackJack game window
    root = Tk()
    root.title('BlackJack')
    root.geometry('800x600') 
    root.resizable(False, False)
def snake_start():  # Snake game window
    root = Tk()
    root.title('Snake')
    root.geometry('600x600') 
    root.resizable(False, False)
def scoreboard_start():  # Scoreboard window
    root = Tk()
    root.title('Scoreboard')
    root.geometry('600x500')
    root.resizable(False, False)
    
# This code creates a Tkinter window with a menu bar containing File and Help menus.
def create_menu():
    root = Tk()
    title = 'Games Compendium'
    root.title(title)

    #Specify window size
    width=800
    height=450
    root.geometry('{}x{}'.format(width, height))

    # create a quick frame
    frame = Frame(root)
    frame.pack(pady=20)

    #setup frame grid
    label = Label(frame, text=title, font=('Helvetica', 24))
    
    # a navbar menu at the top of window
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='Navigation', menu=filemenu)
    filemenu.add_command(label='Scoreboard', command=scoreboard_start)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.destroy)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='Game 1 Instructions')
    helpmenu.add_command(label='Game 2 Instructions')
    helpmenu.add_command(label='Game 3 Instructions')

    title_label = Label(frame, text='The Great Game compendium', font=('Helvetica', 32))
    title_label.grid(row=0, column=0, columnspan=3)
    # button for each of the game windows
    button_width = 20
    button_height = 5
    buttonw = Button(frame, text='Wordle', width=button_width, height=button_height, command=wordle_start)
    buttonb = Button(frame, text='BlackJack', width=button_width, height=button_height, command=blackjack_start)
    buttons = Button(frame, text='Snake', width=button_width, height=button_height, command=snake_start)

    buttonw.grid(row=1, column=0, pady=50, padx=(0,20))
    buttonb.grid(row=1, column=1, pady=50, padx=20)
    buttons.grid(row=1, column=2, pady=50, padx=(20,0))
    mainloop()


# progressing the progress bar
def start_progress():
    # Create a progressbar widget
    if pg['value']< 100:
        pg['value'] += 50
        root.after(50, start_progress)
    else:
        root.destroy()
        create_menu()
# check for name entered
def start_loading():
    global username
    username = user.get()
    if len(username) > 0:
        start_progress()
    else:
        root = Tk()
        root.title('Error')
        root.geometry('250x100')
        root.resizable(False, False)
        Label(root, text="You must enter a name to begin!").grid(row=0, column=0, pady=20, padx=20)
# begin loading screen window
root = Tk()
title = 'Games Compendium'
root.title(title)

#Specify window size
width=800
height=450
root.geometry('{}x{}'.format(width, height))

# create a quick frame
frame = Frame(root)
frame.pack(pady=20)

#setup frame grid
label = Label(frame, text=title, font=('Helvetica', 24))

# Loading screen
pg =  Progressbar(frame, orient="horizontal", length=500, mode="determinate")
pg.grid(row=2, column=1, columnspan=2)
# Enter in username
Label(frame, text="Enter username:").grid(row=0, column=1, columnspan=2, pady=(50, 0))
user = Entry(frame)
user.grid(row=1, column=1, columnspan=2, pady=(5, 25))
# button that checks for username and starts loading it if present
start_button = Button(frame, text="Start game", command=start_loading)
start_button.grid(row=3, column=1, columnspan=2, pady=50)
root.mainloop()
