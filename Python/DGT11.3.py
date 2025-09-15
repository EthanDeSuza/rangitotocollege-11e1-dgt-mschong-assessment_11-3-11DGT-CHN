"""11DGT Assessment 11.3.

stuff for doing the tkinter assessment
"""


from tkinter import *
from tkinter.ttk import Progressbar
def wordle():  # Wordle game window
    # begin the wordle game
    root = Tk()
    title = 'Wordle'
    root.title(title)

    #Specify window size
    width=400
    height=700
    root.geometry('{}x{}'.format(width, height))

    # create a frame
    interface_frame = Frame(root)
    interface_frame.pack(pady=30)

    #setup frame grid
    label = Label(interface_frame, text=title, font=('Helvetica', 24))
    # sets a word for wordle
    words = ['great', 'games', 'frame', 'comic', 'micro']
    correct_word = random.choice(words)
    def reload_game():  # Restarts the game
        root.destroy()
        wordle()
    def close_game():
        root.destroy()
        create_menu()
    def wordle_instruct():
        root = Tk()
        root.title('Wordle Instructions')
        root.resizable(False, False)
        wordle_struct = Label(root, text='To play wordle you guess a five letter word,\n'
                              'then when you press the guess button you will be show\n'
                              'which of your letters are incorrect, in the wrong place\n'
                              'or correct.', font=('Helvetica', 12))
        wordle_struct.grid(row=0, column=0)
    # a navbar and help menu at the top of window
    menu = Menu(root)
    root.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Blackjack', command=blackjack_start)
    navmenu.add_command(label='Snake', command=snake_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=root.destroy)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='Wordle Instructions', command=wordle_instruct)
    
    def checkword():  # checks the word and then tells player which letters are correct and which are not or in the wrong place
        global guesses  # Grabs the global guesses variable
        if guesses <= 5:  # limits the players guesses to 6
            if guess.get().lower() == correct_word:  # Checks if it's the correct word
                for i in range(0,5):  # shows the player all the letter's are correct
                    box = Label(interface_frame, text=guess.get().upper()[i], bg='green', fg='white', width=10, height=5)
                    box.grid(row=guesses+4, column=i+1)
                # tells the player it's the correct word
                result = Label(interface_frame, text=f"You guessed the right word!\nIt took you {guesses+1} guesses.")
                result.grid(row=guesses+5, column=1, columnspan=5)
                # removes the capability of guessing more words
                guess.destroy()
                submit.destroy()
                textguess.destroy()
                # creates options to exit the game or replay it
                retry = Button(interface_frame, text="Retry?", width=button_width, height=button_height, command=reload_game)
                exit = Button(interface_frame, text="Exit to menu?", width=button_width, height=button_height, command=close_game)
                retry.grid(row=guesses+6, column=1, columnspan=2)
                exit.grid(row=guesses+6, column=4, columnspan=2)
                if guesses < wordle_top3['first'][0]:
                    wordle_top3['first'][0] = guesses+1
                    wordle_top3['first'][1] = username
                elif guesses < wordle_top3['second'][0]:
                    wordle_top3['second'][0] = guesses+1
                    wordle_top3['second'][1] = username
                elif guesses < wordle_top3['third'][0]:
                    wordle_top3['third'][0] = guesses+1
                    wordle_top3['third'][1] = username
                # resets guesses variable
                guesses = 0
                
            elif len(guess.get()) != 5:  # Check for correct length
                result = Label(interface_frame, text="Your guess must be 5 letters")
                result.grid(row=5, column=3, columnspan=5)
            else:
                for i in range(0,5):
                    if guess.get().lower()[i] == correct_word[i]:
                        box = Label(interface_frame, text=guess.get().upper()[i], bg='green', fg='white', width=10, height=5)
                        box.grid(row=guesses+4, column=i+1)
                    elif guess.get().lower()[i] in correct_word:
                        box = Label(interface_frame, text=guess.get().upper()[i], bg='orange', fg='white', width=10, height=5)
                        box.grid(row=guesses+4, column=i+1)
                    else:
                        box = Label(interface_frame, text=guess.get().upper()[i], bg='grey', fg='white', width=10, height=5)
                        box.grid(row=guesses+4, column=i+1)
                guesses += 1
        if guesses > 5:
            result = Label(interface_frame, text="Out of guesses, the word was: "+correct_word)
            result.grid(row=guesses+5, column=1, columnspan=5)
            guess.destroy()
            submit.destroy()
            textguess.destroy()
            retry = Button(interface_frame, text="Retry?", width=button_width, height=button_height, command=reload_game)
            exit = Button(interface_frame, text="Exit to menu?", width=button_width, height=button_height, command=close_game)
            retry.grid(row=guesses+6, column=1, columnspan=2)
            exit.grid(row=guesses+6, column=4, columnspan=2)
            guesses = 0
    for repeat in range(0, 5):
        box = Label(interface_frame, width=10, height=5)
        box.grid(row=4, column=repeat+1)
    # title for on the window
    title_label = Label(interface_frame, text=title, font=('Helvetica', 32))
    title_label.grid(row=0, column=1, columnspan=5)
    # the guessing word entry and button
    textguess = Label(interface_frame, text="Guess a word:")
    guess = Entry(interface_frame, width=9)
    submit = Button(interface_frame, text="Guess", width=9, height=int(button_height/2), command=checkword)
    textguess.grid(row=2, column=2, columnspan=2, pady=5, padx=5)
    guess.grid(row=2, column=3, columnspan=2, padx=5)
    submit.grid(row=3, column=3)
        
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
    wordlescore = Label(root, text=f'First place: {wordle_top3['first'][1]} with {wordle_top3['first'][0]}')
    wordlescore.grid(row=0, column=0)
    wordlescore = Label(root, text=f'Second place: {wordle_top3['second'][1]} with {wordle_top3['second'][0]}')
    wordlescore.grid(row=1, column=0)
    wordlescore = Label(root, text=f'Third place: {wordle_top3['third'][1]} with {wordle_top3['third'][0]}')
    wordlescore.grid(row=2, column=0)
# This code creates a Tkinter window with a menu bar containing File and Help menus.
def create_menu():
    def wordle_start():
        root.destroy()
        wordle()
    root = Tk()
    root.title(title)

    #Specify window size
    width=800
    height=450
    root.geometry('{}x{}'.format(width, height))
    # create a quick frame
    frame = Frame(root)
    frame.pack(pady=20)

    #setup frame grid
    framegrid = Label(frame, text=title, font=('Helvetica', 24))
    
    # a navbar menu at the top of window
    menu = Menu(root)
    root.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Wordle', command=wordle_start)
    navmenu.add_command(label='Blackjack', command=blackjack_start)
    navmenu.add_command(label='Snake', command=snake_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit', command=root.destroy)
    namemenu = Menu(menu, tearoff=0)
    namemenu.add_command
    title_label = Label(frame, text=title, font=('Helvetica', 32, 'bold'))
    title_label.grid(row=0, column=0, columnspan=3)
    # button for each of the game windows

    buttonw = Button(frame, text='Play Wordle', width=button_width, height=button_height, command=wordle_start)
    buttonb = Button(frame, text='Play BlackJack', width=button_width, height=button_height, command=blackjack_start)
    buttons = Button(frame, text='Play Snake', width=button_width, height=button_height, command=snake_start)

    buttonw.grid(row=1, column=0, pady=50, padx=(0,20))
    buttonb.grid(row=1, column=1, pady=50, padx=20)
    buttons.grid(row=1, column=2, pady=50, padx=(20,0))
    mainloop()


# progressing the progress bar
def start_progress():
    # create the random amount of progress
    loading = random.randint(1, 10)
    # Create a progressbar widget
    if pg['value']< 100:
        pg['value'] += loading
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
import random
# Sets up some global variables for the wordle game
guesses = 0
guess = ''
correct_word = ''
wordle_top3 = {'first':[7, 'Computer'], 'second':[7, 'Computer'], 'third':[7, 'Computer']}
blackjack_top3 = {'first':[0, 'Computer'], 'second':[0, 'Computer'], 'third':[0, 'Computer']}
snake_top3 = {'first':[0, 'Computer'], 'second':[0, 'Computer'], 'third':[0, 'Computer']}
# Sets up widths anf heights for some buttons
button_width = 20
button_height = 5
# begin loading screen window
root = Tk()
title = 'The Great Games Compendium'
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
start_button = Button(frame, text="Start game", width = button_width, height = button_height, command=start_loading)
start_button.grid(row=3, column=1, columnspan=2, pady=50)
root.mainloop()