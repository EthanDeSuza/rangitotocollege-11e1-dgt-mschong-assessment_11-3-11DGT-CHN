"""11DGT Assessment 11.3.



stuff for doing the tkinter assessment.
"""

from tkinter import *
from tkinter.ttk import Progressbar


def wordle():  # Wordle game window
    # begin the wordle game
    wordle_win = Tk()
    title = 'Wordle'
    wordle_win.title(title)


    #Specify window size
    width=400
    height=700
    wordle_win.geometry('{}x{}'.format(width, height))



    # create a frame
    interface_frame = Frame(wordle_win)
    interface_frame.pack(pady=30)
    #setup frame grid
    label = Label(interface_frame, text=title, font=('Helvetica', 24))
    # sets a word for wordle
    words = ['great', 'games', 'frame', 'comic', 'micro']
    correct_word = random.choice(words)
    def gamble_start():
        wordle_win.destroy()
        blackjack()
    def snake_start():
        wordle_win.destroy()
        snake()
    def reload_game():  # Restarts the game
        wordle_win.destroy()
        wordle()
    def close_game():
        wordle_win.destroy()
        create_menu()
    def wordle_instruct():
        wordle_structs = Tk()
        wordle_structs.title('Wordle Instructions')
        wordle_structs.resizable(False, False)
        instruct = Label(wordle_structs, text="How to play", font=('Helvetica', 24, 'underline'))
        instruct.grid(row=0, column=0)
        wordle_struct = Label(wordle_structs, text='To play wordle you guess a five letter word,\n'
                              'then when you press the guess button you will be show\n'
                              'which of your letters are incorrect, in the wrong place\n'
                              'or correct.', font=('Helvetica', 12))
        wordle_struct.grid(row=1, column=0)
    # a navbar and help menu at the top of window
    menu = Menu(wordle_win)
    wordle_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Blackjack', command=gamble_start)
    navmenu.add_command(label='Snake', command=snake_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=wordle_win.destroy)
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
                global username
                if guesses < wordle_top3['first'][0]:
                    wordle_top3['third'][0] = wordle_top3['second'][0]
                    wordle_top3['third'][1] = wordle_top3['second'][1]
                    wordle_top3['second'][0] = wordle_top3['first'][0]
                    wordle_top3['second'][1] = wordle_top3['first'][1]
                    wordle_top3['first'][0] = guesses+1
                    wordle_top3['first'][1] = username
                elif guesses < wordle_top3['second'][0]:
                    wordle_top3['third'][0] = wordle_top3['second'][0]
                    wordle_top3['third'][1] = wordle_top3['second'][1]
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
    # creates a correct alignment for the whole game
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
def blackjack():  # BlackJack game window
    # begin the wordle game
    gamble_win = Tk()
    title = 'BlackJack'
    gamble_win.title(title)
    gamble_win.configure(bg='green')



    #Specify window size
    width=700
    height=500
    gamble_win.geometry('{}x{}'.format(width, height))




    # create a frame
    interface_frame = Frame(gamble_win, bg='green')
    interface_frame.pack(pady=30)
    #setup frame grid
    label = Label(interface_frame, text=title, font=('Helvetica', 24))
    def wordle_start():
        gamble_win.destroy()
        wordle()
    def snake_start():
        gamble_win.destroy()
        snake()
    def reload_game():  # Restarts the game
        gamble_win.destroy()
        blackjack()
    def close_game():
        gamble_win.destroy()
        create_menu()
    def gamble_instruct():
        gamble_structs = Tk()
        gamble_structs.title('BlackJack Instructions')
        gamble_structs.resizable(False, False)
        gamble_struct = Label(gamble_structs, text='You have to choose an amount of tiddlywinks to put into the pot,\n'
                              'then you are given your cards and you have to get as close to 21 \n'
                              'as possible without going over otherwise you lose. You can choose to\n'
                              'either get a new card or end the game with the cards you have, if the\n'
                              'dealer gets closer to 21 without going over they win, if not you win.\n'
                              'If both of you fail then you are returned your tiddlywinks and a new round starts\n'
                              'If you run out of tiddlywinks then you lose and your highscore will be checked on the leaderboards', font=('Helvetica', 12))
        gamble_struct.grid(row=1, column=0)
    # a navbar and help menu at the top of window
    menu = Menu(gamble_win)
    gamble_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Wordle', command=wordle_start)
    navmenu.add_command(label='Snake', command=snake_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=gamble_win.destroy)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='BlackJack Instructions', command=gamble_instruct)
    def beginbet():
        global continues, balance, returnmenu, cardshow1, cardshow2, card1, card2, yours, dnew, pnew
        if td <= 0:
            reload_game()
        else:
            pnew_card = Label(interface_frame)
            pnew_card.grid(row=0, column=0)
            dnew_card = Label(interface_frame)
            dnew_card.grid(row=0, column=0)
            continues.destroy()
            balance.destroy()
            returnmenu.destroy()
            cardshow1.destroy()
            cardshow2.destroy()
            card1.destroy()
            card2.destroy()
            for i in range(0, dnew):
                cover = Label(interface_frame, width=17, height=10, background='green')
                cover.grid(row=3, column=i+2)
            for i in range(0, pnew):
                cover = Label(interface_frame, width=17, height=10, background='green')
                cover.grid(row=5, column=i+2)
            yours.destroy()
            bettingtime()
    def check_winner():
        global total, dtotal, gamble, td, hit, stand, continues, returnmenu
        hit.destroy()
        stand.destroy()
        if total > dtotal and total < 22 or dtotal > 21 and total < 22:
            print('player wins')
            td += gamble *2
            continues = Button(interface_frame, width=10, height=4, text='Continue?', command=beginbet)
            continues.grid(row=4, column=0)
            returnmenu = Button(interface_frame, width=10, height=4, text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=4)
        elif dtotal == total or dtotal > 21 and total > 21:
            print('tie')
            td += gamble
            continues = Button(interface_frame, width=10, height=4, text='Continue?', command=beginbet)
            continues.grid(row=4, column=0)
            returnmenu = Button(interface_frame, width=10, height=4, text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=4)
        elif dtotal > total and dtotal < 22 or total > 21 and dtotal < 22:
            print('dealer wins')
            continues = Button(interface_frame, width=10, height=4, text='Continue?', command=beginbet)
            continues.grid(row=4, column=0)
            returnmenu = Button(interface_frame, width=10, height=4, text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=4)
        else:
            print('How did we get here')
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
       
    for repeat in range(0, 5):
        box = Label(interface_frame, width=17, height=7, bg='green')
        box.grid(row=5, column=repeat)
   
    gametitle = Label(interface_frame, text='BlackJack', bg='green', font=('helvetica', 25))
    gametitle.grid(row=0, column=2)
   
    global td, pnew, dnew, balance
    td = 100
   
    def ten():
        global td, gamble, balance
        gamble = 10
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()
    def fifty():
        global td, gamble, balance
        gamble = 50
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()
    def hundy():
        global td, gamble, balance
        gamble = 100
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()
    def half():
        global td, gamble, balance
        gamble = td//2
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()
    def all():
        global td, gamble, balance
        gamble = td
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()
    def bettingtime():
        begin.destroy()
        global bet10, bet50, bet100, bethalf, betall, howmuch, balance
        howmuch = Label(interface_frame, text='How much would you like to bet?', bg='green')
        howmuch.grid(row=2, column=0, columnspan=5)
        bet10 = Button(interface_frame, width=10, height=5, text='10 TD', command=ten)
        bet50 = Button(interface_frame, width=10, height=5, text='50 TD', command=fifty)
        bet100 = Button(interface_frame, width=10, height=5, text='100 TD', command=hundy)
        bethalf = Button(interface_frame, width=10, height=5, text='Half TD', command=half)
        betall = Button(interface_frame, width=10, height=5, text='All TD', command=all)
        bet10.grid(row=3, column=0)
        bet50.grid(row=3, column=1)
        bet100.grid(row=3, column=2)
        bethalf.grid(row=3, column=3)
        betall.grid(row=3, column=4)
    begin = Button(interface_frame, width=20, height=5, text='Begin Game', command=bettingtime)
    begin.grid(row=3, column=2)
    balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
    balance.grid(row=0, column=4)
    cards = [13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11, 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]
    
    pnew = 0
    dnew = 0
    def addcard():
        global cardnum, total, yours, pnew_card, pnew
        newcard = random.choice(cards)
        cards.remove(newcard)
        pnew_card = Label(interface_frame, width=17, height=10, text=newcard, background='light grey')
        pnew_card.grid(row=5, column=cardnum)
        yours.destroy()
        total += newcard
        yours = Label(interface_frame, text=f'Your cards:\ntotal: {total}', bg='green')
        yours.grid(row=4, column=2)
        cardnum+=1
        pnew += 1
        if total > 21:
            endturn()
    def endturn():
        global dcard1, dcard2, dtotal, dnew_card, cardshow2, dnew
        cardshow2.destroy()
        cardshow2 = Label(interface_frame, width=17, height=10, text=dcard2, background='lime green')
        cardshow2.grid(row=3, column=1)
        dtotal = dcard1+dcard2
        cardnum = 2
        end = 0
        while end == 0:
            if dtotal < 16:
                dnew += 1
                newcard = random.choice(cards)
                cards.remove(newcard)
                dnew_card = Label(interface_frame, width=17, height=10, text=newcard, background='lime green')
                dnew_card.grid(row=3, column=cardnum)
                cardnum += 1
                dtotal += newcard
            else:
                end = 1
                check_winner()

    def drawcards():
        global bet10, bet50, bet100, bethalf, betall, howmuch, dcard1, dcard2, total, cardnum, yours, hit, stand, card1, card2, cardshow1, cardshow2
        cards = [13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11, 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]
        cardnum = 0
        bet10.destroy()
        bet50.destroy()
        bet100.destroy()
        bethalf.destroy()
        betall.destroy()
        howmuch.destroy()
        theirs = Label(interface_frame, text='Dealers cards:')
        theirs.grid(row=2, column=2)
        hit = Button(interface_frame, width=10, height=5, text='Hit', command=addcard)
        hit.grid(row=4, column=0)
        stand = Button(interface_frame, width=10, height=5, text='Stand', command=endturn)
        stand.grid(row=4, column=4)
        # Draws your first card
        pcard1 = random.choice(cards)
        cards.remove(pcard1)
        print(pcard1)
        card1 = Label(interface_frame, width=17, height=10, text=pcard1, background='lime green')
        card1.grid(row=5, column=cardnum)
        cardnum+=1
        # Draws dealers first card
        dcard1 = random.choice(cards)
        cards.remove(dcard1)
        print(dcard1)
        cardshow1 = Label(interface_frame, width=17, height=10, text=dcard1, background='lime green')
        cardshow1.grid(row=3, column=0)
        # Draws your second card
        pcard2 = random.choice(cards)
        while pcard2 + pcard1 > 21:
            pcard2 = random.choice(cards)
        cards.remove(pcard2)
        print(pcard2)
        card2 = Label(interface_frame, width=17, height=10, text=pcard2, background='lime green')
        card2.grid(row=5, column=cardnum)
        cardnum+=1
        # Draws dealers second card
        dcard2 = random.choice(cards)
        while dcard2 + dcard1 > 21:
            dcard2 = random.choice(cards)
        cards.remove(dcard2)
        print(dcard2)
        cardshow2 = Label(interface_frame, width=17, height=10, background='dark green')
        cardshow2.grid(row=3, column=1)
        total = pcard1+pcard2
        yours = Label(interface_frame, text=f'Your cards:\ntotal: {total}', bg='green')
        yours.grid(row=4, column=2)
    gamble_win.mainloop()

def snake():  # Snake game window
    root = Tk()
    root.title('Snake')
    root.geometry('600x600')
    root.resizable(False, False)
    root.mainloop()
def scoreboard_start():  # Scoreboard window
    root = Tk()
    root.title('Leaderboard')
    root.geometry('600x500')
    root.resizable(False, False)
    title = Label(root, text='The leaderboard', font=('Helvetica', 32, 'bold'))
    title.grid(row=0, column=0, columnspan=5, padx=(125))
    wordle_scores = Label(root, text='Wordle Highscores', font=('Helvetica', 24, 'bold'))
    wordle_scores.grid(row=1, column=2)
    wordlescore = Label(root, text=f"First place: {wordle_top3['first'][1]} with {wordle_top3['first'][0]} guesses", font=('Helvetica', 10, 'italic'))
    wordlescore.grid(row=2, column=2)
    wordlescore = Label(root, text=f"Second place: {wordle_top3['second'][1]} with {wordle_top3['second'][0]} guesses", font=('Helvetica', 10, 'italic'))
    wordlescore.grid(row=3, column=2)
    wordlescore = Label(root, text=f"Third place: {wordle_top3['third'][1]} with {wordle_top3['third'][0]} guesses", font=('Helvetica', 10, 'italic'))
    wordlescore.grid(row=4, column=2)
    blackjackscore = Label(root, text='Blackjack Highscores', font=('Helvetica', 24, 'bold'))
    blackjackscore.grid(row=5, column=2)
    blackjackscore = Label(root, text=f"First place: {blackjack_top3['first'][1]} with {blackjack_top3['first'][0]} tiddlywinks", font=('Helvetica', 10, 'italic'))
    blackjackscore.grid(row=6, column=2)
    blackjackscore = Label(root, text=f"Second place: {blackjack_top3['second'][1]} with {blackjack_top3['second'][0]} tiddlywinks", font=('Helvetica', 10, 'italic'))
    blackjackscore.grid(row=7, column=2)
    blackjackscore = Label(root, text=f"Third place: {blackjack_top3['third'][1]} with {blackjack_top3['third'][0]} tiddlywinks", font=('Helvetica', 10, 'italic'))
    blackjackscore.grid(row=8, column=2)
    snake_scores = Label(root, text='Snake Highscores', font=('Helvetica', 24, 'bold'))
    snake_scores.grid(row=9, column=2)
    snake_scores = Label(root, text=f"First place: {snake_top3['first'][1]} with {snake_top3['first'][0]} points", font=('Helvetica', 10, 'italic'))
    snake_scores.grid(row=10, column=2)
    snake_scores = Label(root, text=f"Second place: {snake_top3['second'][1]} with {snake_top3['second'][0]} points", font=('Helvetica', 10, 'italic'))
    snake_scores.grid(row=11, column=2)
    snake_scores = Label(root, text=f"Third place: {snake_top3['third'][1]} with {snake_top3['third'][0]} points", font=('Helvetica', 10, 'italic'))
    snake_scores.grid(row=12, column=2)
    root.mainloop()
# This code creates a Tkinter window with a menu bar containing File and Help menus.
def create_menu():
    menu_win = Tk()
    menu_win.title(title)

    def wordle_start():
        menu_win.destroy()
        wordle()
    def snake_start():
        menu_win.destroy()
        snake()
    def gamble_start():
        menu_win.destroy()
        blackjack()
   
    def change_name():
        def set_name():
            global username
            username = user.get()
           
            if len(username) > 0:
                print(username)
                change.destroy()
                create_menu()
            else:
                error = Tk()
                error.title('Error')
                error.geometry('250x100')
                error.resizable(False, False)
                Label(root, text="You must enter a name to begin!").grid(row=0, column=0, pady=20, padx=20)
        menu_win.destroy()
        change = Tk()
        change.title('Change User')
        text1 = Label(change, text='Change username:')
        user = Entry(change)
        submit = Button(change, text='Submit', command=set_name)
        text1.grid(row=0, column=0, pady=20, padx=20)
        user.grid(row=0, column=1, padx=20)
        submit.grid(row=1, columnspan=2)
       
   
   
    #Specify window size
    width=800
    height=450
    menu_win.geometry('{}x{}'.format(width, height))
    # create a quick frame
    menu_frame = Frame(menu_win)
    menu_frame.pack(pady=20)

    #setup frame grid
    frame_grid = Label(menu_frame, text=title, font=('Helvetica', 24))
    # a navbar menu at the top of window
    menu = Menu(menu_win)
    menu_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Wordle', command=wordle_start)
    navmenu.add_command(label='Blackjack', command=gamble_start)
    navmenu.add_command(label='Snake', command=snake_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit', command=menu_win.destroy)
    namemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Change username', menu=namemenu)
    namemenu.add_command(label='Change name', command=change_name)



    title_label = Label(menu_frame, text=title, font=('Helvetica', 32, 'bold'))
    title_label.grid(row=0, column=0, columnspan=3)
    # button for each of the game windows



    buttonw = Button(menu_frame, text='Play Wordle', width=button_width, height=button_height, command=wordle_start)
    buttonb = Button(menu_frame, text='Play BlackJack', width=button_width, height=button_height, command=gamble_start)
    buttons = Button(menu_frame, text='Play Snake', width=button_width, height=button_height, command=snake_start)



    buttonw.grid(row=1, column=0, pady=50, padx=(0,20))
    buttonb.grid(row=1, column=1, pady=50, padx=20)
    buttons.grid(row=1, column=2, pady=50, padx=(20,0))
    menu_win.mainloop()




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
