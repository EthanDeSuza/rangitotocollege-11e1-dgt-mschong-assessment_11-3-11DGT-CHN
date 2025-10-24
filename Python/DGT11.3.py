"""11DGT Assessment 11.3.

This is the main file that runs all the
stuff for doing the tkinter games compendium
assessment.
"""

from tkinter import *
from tkinter.ttk import Progressbar
import random


def wordle():  # Wordle game window
    """Begin the wordle game.

    Runs the wordle game and displayes it to the user.
    """
    # Starts window and defines the title
    global width, x
    wordle_win = Tk()
    title = 'Wordle'
    wordle_win.title(title)
    # Specify window size
    width = 400
    height = 500
    screen_width = wordle_win.winfo_screenwidth()  # Width of the screen
    screen_height = wordle_win.winfo_screenheight()  # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    wordle_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    wordle_win.configure(bg='grey')
    # Create a frame
    interface_frame = Frame(wordle_win, bg='grey')
    interface_frame.pack(pady=30)
    # Sets a word for wordle
    words = ['great', 'games', 'frame', 'comic', 'micro', 'apple',
             'seven', 'sixty', 'point', 'crows', 'straw', 'users',
             'ducks', 'mouse', 'fifty', 'quits', 'truck', 'miles']
    correct_word = random.choice(words)

    def gamble_start():  # starts blackjack
        wordle_win.destroy()
        blackjack()

    def clicker_start():  # starts clicker game
        wordle_win.destroy()
        clicker()

    def reload_game():  # Restarts the game
        wordle_win.destroy()
        wordle()

    def close_game():  # returns to menu
        wordle_win.destroy()
        create_menu()

    def wordle_instruct():  # tells player how to play the game
        wordle_structs = Tk()
        wordle_structs.title('Wordle Instructions')
        wordle_structs.resizable(False, False)
        instruct = Label(wordle_structs, text="How to play",
                         font=('Helvetica', 24, 'underline'))
        instruct.grid(row=0, column=0)
        wordle_struct = Label(wordle_structs, text='To play wordle you '
                              'guess a five letter word,\nthen when you '
                              'press the guess button you will be show\n'
                              'which of your letters are incorrect(grey), '
                              'in the wrong place(yellow)'
                              '\nor correct(green).',
                              font=('Helvetica', 12))
        wordle_struct.grid(row=1, column=0)
    # a navbar and help menu at the top of window
    menu = Menu(wordle_win)
    wordle_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Blackjack', command=gamble_start)
    navmenu.add_command(label='Geoclicker', command=clicker_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=wordle_win.destroy)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='Wordle Instructions', command=wordle_instruct)
    global guess, result

    def checkword():
        """Checks word.

        Compares word given with correct answer to return which letters
        are correct.
        """
        global guesses, guess, result, width, height, x  # Grabs the variables
        if guesses <= 5:  # Limits the players guesses to 6
            if guess.get().lower() == correct_word:  # Check word with correct
                result.destroy()
                for i in range(0, 5):
                    # shows the player all the letter's are correct
                    box = Label(interface_frame, text=guess.get().upper()[i],
                                bg='green', fg='white', width=10, height=5)
                    box.grid(row=guesses+5, column=i + 1)
                # tells the player it's the correct word
                result = Label(interface_frame, text="You guessed the right "
                               f'word!\nIt took you {guesses+1} guesses.',
                               bg='grey')
                result.grid(row=guesses+6, column=1, columnspan=5)
                # removes the capability of guessing more words
                guess.destroy()
                submit.destroy()
                textguess.destroy()
                # creates options to exit the game or replay it
                retry = Button(interface_frame, text="Retry?",
                               width=button_width, height=button_height,
                               command=reload_game)
                exit = Button(interface_frame, text="Exit to menu?",
                              width=button_width, height=button_height,
                              command=close_game)
                retry.grid(row=guesses+7, column=1, columnspan=2)
                exit.grid(row=guesses+7, column=4, columnspan=2)
                global username
                # Finds where the score should be placed and places it there
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
                result.destroy()
                result = Label(interface_frame,
                               text="Your guess must be 5 letters", bg='grey')
                result.grid(row=guesses+7, column=3, columnspan=5)
            else:  # checks letters in word and gives them corresponding colour
                result.destroy()
                for i in range(0, 5):
                    if guess.get().lower()[i] == correct_word[i]:
                        box = Label(interface_frame, bg='green',
                                    text=guess.get().upper()[i],
                                    fg='white', width=10, height=5)
                        box.grid(row=guesses+5, column=i+1)
                    elif guess.get().lower()[i] in correct_word:
                        box = Label(interface_frame, bg='orange',
                                    text=guess.get().upper()[i],
                                    fg='white', width=10, height=5)
                        box.grid(row=guesses+5, column=i+1)
                    else:
                        box = Label(interface_frame, bg='dark grey',
                                    text=guess.get().upper()[i],
                                    fg='white', width=10, height=5)
                        box.grid(row=guesses+5, column=i+1)
                guesses += 1
                # Increases window size to fit new row of guesses
                height += 60
                screen_height = wordle_win.winfo_screenheight() # Height of the screen
                # Calculate Starting Y coordinates for Window
                y = (screen_height/2) - (height/2)
                wordle_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
                # resets the entry box
                guess.delete(0, END)
        if guesses > 5:  # ends game when they reach 6 guesses
            result = Label(interface_frame,
                           text="Out of guesses, the word was: "
                           + correct_word, bg='grey')
            result.grid(row=guesses+6, column=1, columnspan=5, pady=10)
            # Removes guessing capability
            guess.destroy()
            submit.destroy()
            textguess.destroy()
            # Adds restart and exit buttons
            retry = Button(interface_frame, text="Retry?",
                           width=button_width, height=button_height,
                           command=reload_game)
            exit = Button(interface_frame, text="Exit to menu?",
                          width=button_width, height=button_height,
                          command=close_game)
            retry.grid(row=guesses+7, column=1, columnspan=2)
            exit.grid(row=guesses+7, column=4, columnspan=2)
            guesses = 0
    # creates a correct alignment for the whole game
    for repeat in range(0, 5):
        box = Label(interface_frame, width=10, height=5, bg='grey')
        box.grid(row=4, column=repeat+1)
    # title for on the window
    title_label = Label(interface_frame, text=title, bg='grey',
                        font=('Helvetica', 32))
    title_label.grid(row=0, column=1, columnspan=5)
    # the guessing word entry and button
    textguess = Label(interface_frame, bg='grey',
                      text="Guess a  five letter word:")
    guess = Entry(interface_frame, width=9)
    submit = Button(interface_frame, text="Guess", width=9,
                    height=int(button_height/2), command=checkword)
    textguess.grid(row=2, column=2, columnspan=3, pady=5)
    guess.grid(row=3, column=2, columnspan=3)
    submit.grid(row=4, column=3)
    result = Label(interface_frame, text="", bg='grey')
    result.grid(row=guesses+6, column=3, columnspan=5)


def blackjack():
    """BlackJack game window.

    Begin the Blackjack game.
    """
    gamble_win = Tk()
    title = 'BlackJack'
    gamble_win.title(title)
    gamble_win.configure(bg='#326E32')
    # Specify window size
    width = 900
    height = 600
    screen_width = gamble_win.winfo_screenwidth()  # Width of the screen
    screen_height = gamble_win.winfo_screenheight() # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    gamble_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    # create a frame
    interface_frame = Frame(gamble_win, bg='#326E32')
    interface_frame.pack(pady=30)

    def wordle_start():  # begins blackjack
        gamble_win.destroy()
        wordle()

    def clicker_start():  # begins clicker game
        gamble_win.destroy()
        clicker()

    def reload_game():  # Restarts the game
        gamble_win.destroy()
        blackjack()

    def close_game():  # exits to menu
        gamble_win.destroy()
        create_menu()

    def gamble_instruct():  # tells player how to play the game
        gamble_structs = Tk()
        gamble_structs.title('BlackJack Instructions')
        gamble_structs.resizable(False, False)
        gamble_struct = Label(gamble_structs, text='How to play',
                              font=('Helvetica', 24, 'underline'))
        gamble_struct.grid(row=0, column=0)
        gamble_struct = Label(gamble_structs, text='You have to choose an '
                              'amount of tiddlywinks to put into the pot,\n'
                              'then you are given your cards and you have '
                              'to get as close to 21 \nas possible without '
                              'going over otherwise you lose. You can choose '
                              'to\neither get a new card or end the game '
                              'with the cards you have, if the\ndealer gets '
                              'closer to 21 without going over they win, if '
                              'not you win.\nIf both of you fail then you '
                              'are returned your tiddlywinks and a new round '
                              'starts\nIf you run out of tiddlywinks then '
                              'you lose and your highscore will be checked '
                              'on the leaderboards.',
                              font=('Helvetica', 12))
        gamble_struct.grid(row=1, column=0)
    # a navbar and help menu at the top of window
    menu = Menu(gamble_win)
    gamble_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Wordle', command=wordle_start)
    navmenu.add_command(label='Geoclicker', command=clicker_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=gamble_win.destroy)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='BlackJack Instructions',
                         command=gamble_instruct)
    def beginbet():
        """Begins next round of betting.

        Resets the window to allow for the next round of the game
        or resets the game if they've lost.
        """
        global continues, balance, returnmenu, cardshow1, winner
        global cardshow2, card1, card2, yours, dnew, pnew, theirs
        if td <= 0:
            reload_game()
        else:
            # Failsafes incase there are no cards that were drawn
            pnew_card = Label(bg='#326E32')
            pnew_card.pack()
            dnew_card = Label(bg='#326E32')
            dnew_card.pack()
            # Resets the game for betting
            continues.destroy()
            winner.destroy()
            returnmenu.destroy()
            cardshow1.destroy()
            cardshow2.destroy()
            card1.destroy()
            card2.destroy()
            theirs.destroy()
            # Covers cards that don't get destroyed
            for i in range(0, dnew):
                cover = Label(interface_frame, width=17,
                              height=10, background='#326E32')
                cover.grid(row=3, column=i+2)
            for i in range(0, pnew):
                cover = Label(interface_frame, width=17, height=10,
                              background='#326E32')
                cover.grid(row=5, column=i+2)
            yours.destroy()
            bettingtime()

    def check_winner():
        """Checks for winner.

        Checks to see who's score is heighest below 22 and
        designates them the winner.
        """
        global total, dtotal, gamble, td, hit, stand, continues
        global returnmenu, balance, winner, score, td_save
        hit.destroy()
        stand.destroy()
        # Checks for player win
        if total > dtotal and total < 22 or dtotal > 21 and total < 22:
            winner = Label(interface_frame, text='You win!',
                           bg='#326E32', font=('helvetica', 30))
            winner.grid(row=10, column=0, columnspan=5)
            td += gamble * 2
            continues = Button(interface_frame, width=10, height=4,
                               text='Continue?', command=beginbet)
            continues.grid(row=4, column=3, pady=150)
            returnmenu = Button(interface_frame, width=10, height=4,
                                text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=1, pady=150)
            if td_save < td:
                td_save = td
            score.destroy()
            score = Label(interface_frame, text=f'Score: {td_save}',
                  font=(15), bg='#326E32')
            score.grid(row=0, column=0)
        # Checks for tie
        elif dtotal == total or dtotal > 21 and total > 21:
            winner = Label(interface_frame, text="It's a tie!",
                           bg='#326E32', font=('helvetica', 30))
            winner.grid(row=10, column=0, columnspan=5)
            td += gamble
            continues = Button(interface_frame, width=10, height=4,
                               text='Continue?', command=beginbet)
            continues.grid(row=4, column=3, pady=150)
            returnmenu = Button(interface_frame, width=10, height=4,
                                text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=1, pady=150)
            score.destroy()
            score = Label(interface_frame, text=f'Score: {td_save}',
                  font=(15), bg='#326E32')
            score.grid(row=0, column=0)
        # Checks for dealer win
        elif dtotal > total and dtotal < 22 or total > 21 and dtotal < 22:
            winner = Label(interface_frame, text='Dealer wins :(',
                           bg='#326E32', font=('helvetica', 30))
            winner.grid(row=10, column=0, columnspan=5)
            continues = Button(interface_frame, width=10, height=4,
                               text='Continue?', command=beginbet)
            continues.grid(row=4, column=3, pady=150)
            returnmenu = Button(interface_frame, width=10, height=4,
                                text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=1, pady=150)
            score.destroy()
            score = Label(interface_frame, text=f'Score: {td_save}',
                  font=(15), bg='#326E32')
            score.grid(row=0, column=0)
            # if points are 0 then checks score against scoreboard
            if td <= 0:
                global username
                if td_save > blackjack_top3['first'][0]:
                    blackjack_top3['third'][0] = blackjack_top3['second'][0]
                    blackjack_top3['third'][1] = blackjack_top3['second'][1]
                    blackjack_top3['second'][0] = blackjack_top3['first'][0]
                    blackjack_top3['second'][1] = blackjack_top3['first'][1]
                    blackjack_top3['first'][0] = td_save
                    blackjack_top3['first'][1] = username
                elif td_save > blackjack_top3['second'][0]:
                    blackjack_top3['third'][0] = blackjack_top3['second'][0]
                    blackjack_top3['third'][1] = blackjack_top3['second'][1]
                    blackjack_top3['second'][0] = td_save
                    blackjack_top3['second'][1] = username
                elif td_save > blackjack_top3['third'][0]:
                    blackjack_top3['third'][0] = td_save
                    blackjack_top3['third'][1] = username
        else:
            print('How did we get here')
        # sets the score to new value dependant on who won
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}',
                        font=(15), bg='#326E32')
        balance.grid(row=0, column=4)

    def ten():  # Bet 10 td
        global td, gamble, balance, td_save
        gamble = 10
        if gamble > td:
            error = Tk()
            error.title('Error')
            error.geometry('300x100')
            error.resizable(False, False)
            errortext = Label(error, text='You do not have enough '
                              'tiddlywinks to make that bet.')
            errortext.pack()
            ok = Button(error, text='OK', command=error.destroy)
            ok.pack()
        else:
            if td_save < td:
                td_save = td
            else:
                td -= gamble
                balance.destroy()
                balance = Label(interface_frame, text=f'Tiddlywinks: {td}',
                                font=(15), bg='#326E32')
                balance.grid(row=0, column=4)
                drawcards()

    def fifty():  # bet 50 td
        global td, gamble, balance, td_save
        gamble = 50
        if gamble > td:
            error = Tk()
            error.title('Error')
            error.geometry('300x100')
            error.resizable(False, False)
            errortext = Label(error, text='You do not have enough '
                              'tiddlywinks to make that bet.')
            errortext.pack()
            ok = Button(error, text='OK', command=error.destroy)
            ok.pack()
        else:
            if td_save < td:
                td_save = td
            else:
                td -= gamble
                balance.destroy()
                balance = Label(interface_frame, text=f'Tiddlywinks: {td}',
                                font=(15), bg='#326E32')
                balance.grid(row=0, column=4)
                drawcards()

    def hundy():  # bet 100 td
        global td, gamble, balance, td_save
        gamble = 100
        if gamble > td:
            error = Tk()
            error.title('Error')
            error.geometry('300x100')
            error.resizable(False, False)
            errortext = Label(error, text='You do not have enough '
                              'tiddlywinks to make that bet.')
            errortext.pack()
            ok = Button(error, text='OK', command=error.destroy)
            ok.pack()
        else:
            if td_save < td:
                td_save = td
            else:
                td -= gamble
                balance.destroy()
                balance = Label(interface_frame, text=f'Tiddlywinks: {td}',
                                font=(15), bg='#326E32')
                balance.grid(row=0, column=4)
                drawcards()


    def half():  # bet half of total td
        global td, gamble, balance, td_save
        gamble = td//2
        if gamble < 1:
            error = Tk()
            error.title('Error')
            error.geometry('300x100')
            error.resizable(False, False)
            errortext = Label(error, text='You do not have enough '
                              'tiddlywinks to make that bet.')
            errortext.pack()
            ok = Button(error, text='OK', command=error.destroy)
            ok.pack()
        else:
            if td_save < td:
                td_save = td
            else:
                td -= gamble
                balance.destroy()
                balance = Label(interface_frame, text=f'Tiddlywinks: {td}',
                                font=(15), bg='#326E32')
                balance.grid(row=0, column=4)
                drawcards()


    def all():  # bet all td
        global td, gamble, balance, td_save
        if td_save < td:
            td_save = td
        else:
            gamble = td
            td -= gamble
            balance.destroy()
            balance = Label(interface_frame, text=f'Tiddlywinks: {td}',
                            font=(15), bg='#326E32')
            balance.grid(row=0, column=4)
            drawcards()

    def bettingtime():  # sets up betting buttons
        begin.destroy()
        global bet10, bet50, bet100, bethalf, betall, howmuch, balance
        width = 900
        height = 600
        screen_width = gamble_win.winfo_screenwidth()  # Width of the screen
        screen_height = gamble_win.winfo_screenheight() # Height of the screen
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        gamble_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
        howmuch = Label(interface_frame, bg='#326E32', font=(15),
                        text='How much would you like to bet?')
        howmuch.grid(row=2, column=0, columnspan=5, pady=25)
        bet10 = Button(interface_frame, width=10, height=5, text='10 TD',
                       command=ten)
        bet50 = Button(interface_frame, width=10, height=5, text='50 TD',
                       command=fifty)
        bet100 = Button(interface_frame, width=10, height=5, text='100 TD',
                        command=hundy)
        bethalf = Button(interface_frame, width=10, height=5, text='Half TD',
                         command=half)
        betall = Button(interface_frame, width=10, height=5, text='All TD',
                        command=all)
        bet10.grid(row=3, column=0, pady=150)
        bet50.grid(row=3, column=1)
        bet100.grid(row=3, column=2)
        bethalf.grid(row=3, column=3)
        betall.grid(row=3, column=4)
    # sets up the frame to be consistant the whole time
    for repeat in range(0, 5):
        box = Label(interface_frame, width=17, height=7, bg='#326E32')
        box.grid(row=5, column=repeat)
    # sets title to the window and td
    gametitle = Label(interface_frame, text='BlackJack', bg='#326E32',
                      font=('helvetica', 25))
    gametitle.grid(row=0, column=2)
    global td, pnew, dnew, balance, score, td_save
    td = 100
    pnew = 0
    dnew = 0
    td_save = td
    # creates button for starting the game
    begin = Button(interface_frame, width=20, height=5, text='Begin Game',
                   command=bettingtime)
    begin.grid(row=3, column=2, pady=150)
    # creates the visible balance
    balance = Label(interface_frame, text=f'Tiddlywinks: {td}',
                    font=(15), bg='#326E32')
    balance.grid(row=0, column=4)
    score = Label(interface_frame, text=f'Score: {td_save}',
                  font=(15), bg='#326E32')
    score.grid(row=0, column=0)
    # creates the cards list
    cards = [13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11, 10, 10, 10, 10,
             9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4,
             4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]

    def addcard():  # adds card to players hand when button is pressed
        global cardnum, total, yours, pnew_card, pnew
        # selects a card from the list then removes it
        newcard = random.choice(cards)
        cards.remove(newcard)
        # creates the new card next to the old cards
        pnew_card = Label(interface_frame, width=17, height=10, text=newcard,
                          background='light grey')
        pnew_card.grid(row=5, column=cardnum)
        # removes old total points and creates a new one with updated points
        yours.destroy()
        total += newcard
        yours = Label(interface_frame, text=f'Your cards:\ntotal: {total}',
                      bg='#326E32', font=('Helvetica', 15, 'bold'))
        yours.grid(row=4, column=2)
        cardnum += 1
        pnew += 1
        # if total is above 21 then it will be the dealers turn
        if total > 21:
            endturn()

    def endturn():  # begins dealers turns
        global dcard1, dcard2, dtotal, dnew_card, cardshow2, dnew, theirs
        # destroys hidden card and create a visible version
        cardshow2.destroy()
        cardshow2 = Label(interface_frame, width=17, height=10, text=dcard2,
                          background='light grey')
        cardshow2.grid(row=3, column=1)
        # changes the total so it now reflects the seen total
        dtotal = dcard1+dcard2
        cardnum = 2
        end = 0
        while end == 0:
            # when below 16 points it will draw a new card
            if dtotal < 16:
                dnew += 1
                newcard = random.choice(cards)
                cards.remove(newcard)
                dnew_card = Label(interface_frame, width=17, height=10,
                                  text=newcard, background='light grey')
                dnew_card.grid(row=3, column=cardnum)
                cardnum += 1
                dtotal += newcard
                theirs.destroy()
                theirs = Label(interface_frame,  bg='#326E32', font=('Helvetica', 15, 'bold'),
                               text=f'Dealers cards:\ntotal: {dtotal}')
                theirs.grid(row=2, column=2)
            # when above 15 it will end game and runs check_winner funct
            else:
                theirs.destroy()
                theirs = Label(interface_frame,  bg='#326E32', font=('Helvetica', 15, 'bold'),
                               text=f'Dealers cards:\ntotal: {dtotal}')
                theirs.grid(row=2, column=2)
                end = 1
                check_winner()

    def drawcards():
        """Draws cards.

        Draws the cards for both the player and the dealer.
        """
        global bet10, bet50, bet100, bethalf, betall, howmuch
        global dcard1, dcard2, total, cardnum, yours, hit, stand
        global card1, card2, cardshow1, cardshow2, theirs
        # Resizes window for card display
        width = 1200
        height = 900
        screen_width = gamble_win.winfo_screenwidth()  # Width of the screen
        screen_height = gamble_win.winfo_screenheight() # Height of the screen
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        gamble_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # resets the cards list
        cards = [13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11,
                 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7,
                 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3,
                 2, 2, 2, 2, 1, 1, 1, 1]
        cardnum = 0
        # removes the betting buttons
        bet10.destroy()
        bet50.destroy()
        bet100.destroy()
        bethalf.destroy()
        betall.destroy()
        howmuch.destroy()
        # creates button to draw a new card
        hit = Button(interface_frame, width=10, height=4, text='Hit',
                     command=addcard)
        hit.grid(row=4, column=1, pady=150)
        # creates button to end turn
        stand = Button(interface_frame, width=10, height=4, text='Stand',
                       command=endturn)
        stand.grid(row=4, column=3, pady=150)
        # Draws your first card
        pcard1 = random.choice(cards)
        cards.remove(pcard1)
        card1 = Label(interface_frame, width=17, height=10, text=pcard1,
                      background='light grey')
        card1.grid(row=5, column=cardnum)
        cardnum += 1
        # Draws dealers first card
        dcard1 = random.choice(cards)
        cards.remove(dcard1)
        cardshow1 = Label(interface_frame, width=17, height=10, text=dcard1,
                          background='light grey')
        cardshow1.grid(row=3, column=0)
        # Draws your second card
        pcard2 = random.choice(cards)
        # checks to make sure it's not an autofail
        while pcard2 + pcard1 > 21:
            pcard2 = random.choice(cards)
        cards.remove(pcard2)
        card2 = Label(interface_frame, width=17, height=10, text=pcard2,
                      background='light grey')
        card2.grid(row=5, column=cardnum)
        cardnum += 1
        # Draws dealers second card
        dcard2 = random.choice(cards)
        while dcard2 + dcard1 > 21:
            dcard2 = random.choice(cards)
        cards.remove(dcard2)
        # hides the dealers second card from the player
        cardshow2 = Label(interface_frame, width=17, height=10,
                          background="#1F421F")
        cardshow2.grid(row=3, column=1)
        total = pcard1+pcard2
        # creates a label that displays the players totals
        yours = Label(interface_frame, bg='#326E32', font=('Helvetica', 15, 'bold'),
                      text=f'Your cards:\ntotal: {total}')
        yours.grid(row=4, column=2)
        theirs = Label(interface_frame, bg='#326E32', font=('Helvetica', 15, 'bold'),
                       text=f'Dealers cards:\ntotal: {dcard1}')
        theirs.grid(row=2, column=2)
    gamble_win.mainloop()


def clicker():
    """Begins clicker game.

    Starts the clicker game for the player to play.
    """
    clicker_win = Tk()
    clicker_win.title('GeoClicker')
    clicker_win.configure(bg='dark grey')
    # Specify window size
    width = 500
    height = 600
    screen_width = clicker_win.winfo_screenwidth()  # Width of the screen
    screen_height = clicker_win.winfo_screenheight() # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    clicker_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    # create a frame
    interface_frame = Frame(clicker_win, bg='light grey')
    interface_frame.pack(padx=50, pady=50)

    def scores():  # Saves the score to the leaderboard
        global geo, username
        if geo > clicker_top3['first'][0]:
            clicker_top3['third'][0] = clicker_top3['second'][0]
            clicker_top3['third'][1] = clicker_top3['second'][1]
            clicker_top3['second'][0] = clicker_top3['first'][0]
            clicker_top3['second'][1] = clicker_top3['first'][1]
            clicker_top3['first'][0] = geo
            clicker_top3['first'][1] = username
        elif geo > clicker_top3['second'][0]:
            clicker_top3['third'][0] = clicker_top3['second'][0]
            clicker_top3['third'][1] = clicker_top3['second'][1]
            clicker_top3['second'][0] = geo
            clicker_top3['second'][1] = username
        elif geo > clicker_top3['third'][0]:
            clicker_top3['third'][0] = geo
            clicker_top3['third'][1] = username

    def wordle_start():  # Starts the wordle game
        scores()
        global end, upgrader
        end = True
        try:
            upgrader.destroy()
            clicker_win.destroy()
        except:
            clicker_win.destroy()
        wordle()

    def gamble_start():  # Starts the blackjack game
        scores()
        global end, upgrader
        end = True
        try:
            upgrader.destroy()
            clicker_win.destroy()
        except:
            clicker_win.destroy()
        blackjack()

    def close_game():  # Exits to the main menu
        scores()
        global end, upgrader
        end = True
        try:
            upgrader.destroy()
            clicker_win.destroy()
        except:
            clicker_win.destroy()
        create_menu()

    def end_game():  # Exits the program
        global end, upgrader
        end = True
        try:
            upgrader.destroy()
            clicker_win.destroy()
        except:
            clicker_win.destroy()

    def clicker_struct():  # Opens the instructions window
        clicker_structs = Tk()
        clicker_structs.title('Clicker Instructions')
        clicker_structs.resizable(False, False)
        clicker_struct = Label(clicker_structs, text='How to play',
                               font=('Helvetica', 24, 'underline'))
        clicker_struct.grid(row=0, column=0)
        clicker_struct = Label(clicker_structs,
                               text='You click the mine button to gain geo,'
                               '\nyou can buy upgrades with geo that can\n'
                               'upgrade your geo per click, add autoclickers'
                               ',\nupgrade their speed and amount per click.',
                               font=('Helvetica', 12))
        clicker_struct.grid(row=1, column=0)
    # a navbar and help menu at the top of window
    menu = Menu(clicker_win)
    clicker_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Wordle', command=wordle_start)
    navmenu.add_command(label='Blackjack', command=gamble_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=end_game)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='Clicker Instructions',
                         command=clicker_struct)
    # sets up all the variables needed for the game
    global geo, mult, bank, miners, mult_cost, miner_cost, pick_cost
    global pick, end, lifeblood, lifeblood_cost, counter, upgrader
    end = False
    geo = 0
    mult = 1
    miners = 0
    mult_cost = 10
    miner_cost = 50
    pick_cost = 100
    pick = 1
    lifeblood = 1000
    lifeblood_cost = 1000
    counter = 0

    def mine():  # Adds geo when the button is pressed
        global geo, mult, bank
        geo += mult
        bank.destroy()
        bank = Label(interface_frame, text=f'Geo: {geo}', fg='black',
                     bg='light grey')
        bank.grid(row=2, column=2)

# Opens the upgrade window when the button is pressed and destroys the old one

    def upgrade_win():
        global geo, mult, upgrader, mult_upgrade, miner_hire, pick_cost
        global pick_enhance, lifeblood_enhance, lifeblood_cost, upgrader
        try:
            upgrader.destroy()
            upgrader = Tk()
        except:
            upgrader = Tk()
        upgrader.geometry('400x250+250+75')
        upgrader.resizable(False, False)
        upgrader.configure(bg='dark grey')
        titles = Label(upgrader, text='Upgrades',
                       bg='dark grey', font=('Helvetica', 24))
        titles.grid(row=0, column=0, columnspan=3, padx=130)
        mult_upgrade = Button(upgrader, command=mult_upgradefunct,
                              text='Increase Geo per click by 1'
                              f'\nCost: {mult_cost} Geo')
        mult_upgrade.grid(row=1, column=0, pady=10)
        amount = Label(upgrader, bg='dark grey',
                       text=f'Amount owned:  {mult-1} times')
        amount.grid(row=2, column=0)
        miner_hire = Button(upgrader, command=miner_purchase,
                            text='Hire a husk miner'
                            f'\nCost: {miner_cost} Geo')
        miner_hire.grid(row=1, column=2, pady=10)
        amount = Label(upgrader, bg='dark grey',
                       text=f'Amount owned:  {miners} times.')
        amount.grid(row=2, column=2)
        if miners > 0:
            pick_enhance = Button(upgrader, command=pick_upgrade,
                                text="Upgrade the husk miner's pickaxe"
                                f"\nCost: {pick_cost} Geo")
            pick_enhance.grid(row=3, column=0, pady=10)
            amount = Label(upgrader, bg='dark grey',
                        text=f'Amount owned:  {pick-1} times.')
            amount.grid(row=4, column=0)
            lifeblood_enhance = Button(upgrader, command=lifeblood_upgrade,
                                    text="Buy lifeblood for the husk miner"
                                    f"\nCost: {lifeblood_cost} Geo")
            lifeblood_enhance.grid(row=3, column=2, pady=10)
            amount = Label(upgrader, bg='dark grey',
                        text=f'Amount owned:  {counter} times.')
            amount.grid(row=4, column=2)

    def miner_purchase():  # Adds an autoclicker if you have enough geo
        global geo, bank, miner_cost, miner_hire, upgrader, miners
        global lifeblood_enhance, pick_enhance, pick_cost, lifeblood_cost
        if geo >= miner_cost:
            geo -= miner_cost
            miners += 1
            miner_cost = int(miner_cost * 2.5)
            bank.destroy()
            bank = Label(interface_frame, text=f'Geo: {geo}',
                         fg='black', bg='light grey')
            bank.grid(row=2, column=2)
            miner_hire = Button(upgrader, command=miner_purchase,
                                text='Hire a husk miner'
                                f'\nCost: {miner_cost} Geo')
            miner_hire.grid(row=1, column=2, pady=10)
            amount = Label(upgrader, bg='dark grey',
                           text=f'Amount owned:  {miners} times.')
            amount.grid(row=2, column=2)
            pick_enhance = Button(upgrader, command=pick_upgrade,
                                text="Upgrade the husk miner's pickaxe"
                                f"\nCost: {pick_cost} Geo")
            pick_enhance.grid(row=3, column=0, pady=10)
            amount = Label(upgrader, bg='dark grey',
                        text=f'Amount owned:  {pick-1} times.')
            amount.grid(row=4, column=0)
            lifeblood_enhance = Button(upgrader, command=lifeblood_upgrade,
                                    text="Buy lifeblood for the husk miner"
                                    f"\nCost: {lifeblood_cost} Geo")
            lifeblood_enhance.grid(row=3, column=2, pady=10)
            amount = Label(upgrader, bg='dark grey',
                        text=f'Amount owned:  {counter} times.')
            amount.grid(row=4, column=2)

    def lifeblood_upgrade():
        # Speeds up the autoclicker if you have enough geo
        global geo, bank, lifeblood_cost, upgrader, lifeblood
        global lifeblood_enhance, counter
        if geo >= lifeblood_cost:
            geo -= lifeblood_cost
            lifeblood *= 0.9
            counter += 1
            lifeblood_cost = int(lifeblood_cost * 2.5)
            bank.destroy()
            bank = Label(interface_frame, bg='light grey',
                         text=f'Geo: {geo}', fg='black')
            bank.grid(row=2, column=2)
            lifeblood_enhance = Button(upgrader, command=lifeblood_upgrade,
                                       text="Buy lifeblood for the husk miner"
                                       f"\nCost: {lifeblood_cost} Geo")
            lifeblood_enhance.grid(row=3, column=2, pady=10)
            amount = Label(upgrader, bg='dark grey',
                           text=f'Amount owned: {counter}')
            amount.grid(row=4, column=2)

    def pick_upgrade():
        # Increases the geo per click of the autoclicker if you have enough geo
        global geo, bank, pick_cost, upgrader, pick, pick_enhance
        if geo >= pick_cost:
            geo -= pick_cost
            pick += 1
            pick_cost = int(pick_cost * 3.5)
            bank.destroy()
            bank = Label(interface_frame, text=f'Geo: {geo}',
                         fg='black', bg='light grey')
            bank.grid(row=2, column=2)
            pick_enhance = Button(upgrader, command=pick_upgrade,
                                  text="Upgrade the husk miner's pickaxe"
                                  f"\nCost: {pick_cost} Geo")
            pick_enhance.grid(row=3, column=0, pady=10)
            amount = Label(upgrader, text='Amount owned:'
                           f' {pick-1}', bg='dark grey')
            amount.grid(row=4, column=0)

    def mult_upgradefunct():  # Increases the geo per click if you have enough geo
        global geo, mult, mult_cost, bank, mult_upgrade, upgrader
        if geo >= mult_cost:
            geo -= mult_cost
            mult += 1
            mult_cost = int(mult_cost * 1.5)
            bank.destroy()
            bank = Label(interface_frame, text=f'Geo: {geo}',
                         fg='black', bg='light grey')
            bank.grid(row=2, column=2)
            mult_upgrade = Button(upgrader, text='Increase Geo per click by 1'
                                  f'\nCost: {mult_cost} Geo',
                                  command=mult_upgradefunct)
            mult_upgrade.grid(row=1, column=0, pady=10)
            amount = Label(upgrader, text=f'Amount owned: {mult-1}', bg='dark grey')
            amount.grid(row=2, column=0)
    # Opens and sets up game and upgrade window
    geoclicker = Label(interface_frame, text='GeoClicker',
                       bg='light grey', font=('Helvetica', 32))
    geoclicker.grid(row=0, column=0, columnspan=5, padx=50, pady=10)
    mine_geo = Button(interface_frame, text='Mine Geo', command=mine,
                      width=10, height=5, font=('Helvetica', 12))
    mine_geo.grid(row=5, column=2, pady=(100, 100))
    upgrades = Button(interface_frame, text='Upgrades',
                      width=20, height=2, command=upgrade_win)
    upgrades.grid(row=6, column=0, columnspan=5, pady=10)
    upgrader = Tk()
    upgrader.title('Upgrades')
    upgrader.geometry('400x250')
    upgrader.resizable(False, False)
    upgrader.configure(bg='dark grey')
    titles = Label(upgrader, text='Upgrades',
                   font=('Helvetica', 24),bg='dark grey')
    titles.grid(row=0, column=0, columnspan=3, padx=130)
    mult_upgrade = Button(upgrader, text='Increase Geo per click by 1'
                          f'\nCost: {mult_cost} Geo',
                          command=mult_upgradefunct)
    mult_upgrade.grid(row=1, column=0, pady=10)
    amount = Label(upgrader, text=f'Amount owned: {mult-1}',bg='dark grey')
    amount.grid(row=2, column=0)
    miner_hire = Button(upgrader, text='Hire a husk miner'
                        f'\nCost: {miner_cost} Geo', command=miner_purchase)
    miner_hire.grid(row=1, column=2, pady=10)
    amount = Label(upgrader, text=f'Amount owned: {miners}', bg='dark grey')
    amount.grid(row=2, column=2)
    bank = Label(interface_frame, text=f'Geo: {geo}',
                 fg='black',bg='light grey')
    bank.grid(row=2, column=2)

    def mine_auto():  # Starts the autoclicker working
        global miners, geo, bank, pick, end, lifeblood
        if end == True:
            return
        geo += miners * pick
        bank.destroy()
        bank = Label(interface_frame, text=f'Geo: {geo}',
                     fg='black', bg='light grey')
        bank.grid(row=2, column=2)
        clicker_win.after(int(lifeblood), mine_auto)
        
    mine_auto()
    clicker_win.mainloop()



def scoreboard_start():  # Scoreboard window
    root = Tk()
    root.title('Leaderboard')
    root.geometry('600x500')
    root.configure(bg='dark grey')
    root.resizable(False, False)
    title = Label(root, text='The leaderboard',
                  font=('Helvetica', 32, 'bold'), bg='dark grey')
    title.grid(row=0, column=0, columnspan=5, padx=(125))
    wordle_scores = Label(root, text='Wordle Highscores',
                          font=('Helvetica', 24, 'bold'), bg='dark grey')
    wordle_scores.grid(row=1, column=2)
    wordlescore = Label(root, text=f"First place: {wordle_top3['first'][1]}"
                        f" with {wordle_top3['first'][0]} guesses",
                        font=('Helvetica', 10, 'italic'), bg='dark grey')
    wordlescore.grid(row=2, column=2)
    wordlescore = Label(root, text=f"Second place: {wordle_top3['second'][1]}"
                        f" with {wordle_top3['second'][0]} guesses",
                        font=('Helvetica', 10, 'italic'), bg='dark grey')
    wordlescore.grid(row=3, column=2)
    wordlescore = Label(root, text=f"Third place: {wordle_top3['third'][1]}"
                        f" with {wordle_top3['third'][0]} guesses",
                        font=('Helvetica', 10, 'italic'), bg='dark grey')
    wordlescore.grid(row=4, column=2)
    blackjackscore = Label(root, text='Blackjack Highscores', 
                           font=('Helvetica', 24, 'bold'), bg='dark grey')
    blackjackscore.grid(row=5, column=2)
    blackjackscore = Label(root, text=f"First place: {blackjack_top3['first'][1]}"
                           f" with {blackjack_top3['first'][0]} tiddlywinks",
                           font=('Helvetica', 10, 'italic'), bg='dark grey')
    blackjackscore.grid(row=6, column=2)
    blackjackscore = Label(root, text=f"Second place: {blackjack_top3['second'][1]}"
                           f" with {blackjack_top3['second'][0]} tiddlywinks",
                           font=('Helvetica', 10, 'italic'), bg='dark grey')
    blackjackscore.grid(row=7, column=2)
    blackjackscore = Label(root, text=f"Third place: {blackjack_top3['third'][1]}"
                           f" with {blackjack_top3['third'][0]} tiddlywinks",
                           font=('Helvetica', 10, 'italic'), bg='dark grey')
    blackjackscore.grid(row=8, column=2)
    clicker_scores = Label(root, text='Geoclicker Highscores',
                           font=('Helvetica', 24, 'bold'), bg='dark grey')
    clicker_scores.grid(row=9, column=2)
    clicker_scores = Label(root, text=f"First place: {clicker_top3['first'][1]}"
                           f" with {clicker_top3['first'][0]} Geo",
                           font=('Helvetica', 10, 'italic'), bg='dark grey')
    clicker_scores.grid(row=10, column=2)
    clicker_scores = Label(root, text=f"Second place: {clicker_top3['second'][1]}"
                           f" with {clicker_top3['second'][0]} Geo",
                           font=('Helvetica', 10, 'italic'), bg='dark grey')
    clicker_scores.grid(row=11, column=2)
    clicker_scores = Label(root, text=f"Third place: {clicker_top3['third'][1]}"
                           f" with {clicker_top3['third'][0]} Geo",
                           font=('Helvetica', 10, 'italic'), bg='dark grey')
    clicker_scores.grid(row=12, column=2)
    root.mainloop()


def create_menu():
    """Create menu.

    This code creates a Tkinter window with a menu bar
    containing File and Help menus.
    """
    menu_win = Tk()
    menu_win.title(title)

    def wordle_start():
        menu_win.destroy()
        wordle()

    def clicker_start():
        menu_win.destroy()
        clicker()

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
                Label(root, text="You must enter"
                      " a name to begin!").grid(row=0, column=0,
                                                pady=20, padx=20)
        menu_win.destroy()
        change = Tk()
        change.title('Change User')
        text1 = Label(change, text='Change username:')
        user = Entry(change)
        submit = Button(change, text='Submit', command=set_name)
        text1.grid(row=0, column=0, pady=20, padx=20)
        user.grid(row=0, column=1, padx=20)
        submit.grid(row=1, columnspan=2)
    # Specify window size
    width = 800
    height = 450
    screen_width = menu_win.winfo_screenwidth()  # Width of the screen
    screen_height = menu_win.winfo_screenheight() # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    menu_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    menu_win.configure(bg='dark grey')
    # create a quick frame
    menu_frame = Frame(menu_win, bg='dark grey')
    menu_frame.pack(pady=20)
    # a navbar menu at the top of window
    menu = Menu(menu_win)
    menu_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Wordle', command=wordle_start)
    navmenu.add_command(label='Blackjack', command=gamble_start)
    navmenu.add_command(label='Geoclicker', command=clicker_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit', command=menu_win.destroy)
    namemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Change username', menu=namemenu)
    namemenu.add_command(label='Change name', command=change_name)
    # Dropdown scoreboard menu  
    scoremenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Scoreboard', menu=scoremenu)
    scoremenu.add_command(label='Wordle Leaderboard')
    scoremenu.add_command(label=f"First place: {wordle_top3['first'][1]}"
                          f" with {wordle_top3['first'][0]} guesses",
                          font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Second place: {wordle_top3['second'][1]}"
                          f" with {wordle_top3['second'][0]} guesses",
                          font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Third place: {wordle_top3['third'][1]}"
                          f" with {wordle_top3['third'][0]} guesses",
                          font=('Helvetica', 10, 'italic'))
    scoremenu.add_separator()
    scoremenu.add_command(label='Blackjack Leaderboard')
    scoremenu.add_command(label=f"First place: {blackjack_top3['first'][1]}"
                          f" with {blackjack_top3['first'][0]} tiddlywinks",
                          font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Second place: {blackjack_top3['second'][1]}"
                          f" with {blackjack_top3['second'][0]} tiddlywinks",
                          font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Third place: {blackjack_top3['third'][1]}"
                          f" with {blackjack_top3['third'][0]} tiddlywinks",
                          font=('Helvetica', 10, 'italic'))
    scoremenu.add_separator()
    scoremenu.add_command(label='Geoclicker Leaderboard')
    scoremenu.add_command(label=f"First place: {clicker_top3['first'][1]}"
                          f" with {clicker_top3['first'][0]} Geo",
                          font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Second place: {clicker_top3['second'][1]}"
                          f" with {clicker_top3['second'][0]} Geo",
                          font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Third place: {clicker_top3['third'][1]}"
                          f" with {clicker_top3['third'][0]} Geo",
                          font=('Helvetica', 10, 'italic'))
    title_label = Label(menu_frame,  bg='dark grey',
                        text=f"Hello {username}! Welcome to \n{title}",
                        font=('Helvetica', 32, 'bold'))
    title_label.grid(row=0, column=0, columnspan=3)
    # button for each of the game windows
    buttonw = Button(menu_frame, text='Play Wordle', command=wordle_start,
                     width=button_width, height=button_height)
    buttonb = Button(menu_frame, text='Play BlackJack', command=gamble_start,
                     width=button_width, height=button_height)
    buttons = Button(menu_frame, text='Play Geoclicker', command=clicker_start,
                     width=button_width, height=button_height)
    buttonw.grid(row=1, column=0, pady=50, padx=(0, 20))
    buttonb.grid(row=1, column=1, pady=50, padx=20)
    buttons.grid(row=1, column=2, pady=50, padx=(20, 0))
    menu_win.mainloop()

# progressing the progress bar


def start_progress():
    """Progress loading.

    Creates the random amount of progress.
    """
    loading = random.randint(1, 10)
    # Create a progressbar widget
    if pg['value'] < 100:
        pg['value'] += loading
        root.after(50, start_progress)
    else:
        root.destroy()
        create_menu()
# check for name entered


def start_loading():
    """Start loading.

    Starts the loading process when button is pressed.
    """
    global username
    username = user.get()
    if len(username) > 0:
        start_progress()
    else:
        root = Tk()
        root.title('Error')
        root.geometry('250x100')
        root.resizable(False, False)
        Label(root, text="You must enter a name to"
              " begin!").grid(row=0, column=0, pady=20, padx=20)


# Sets up some global variables for the wordle game
guesses = 0
guess = ''
correct_word = ''
wordle_top3 = {'first': [6, 'Computer'], 'second': [6, 'Computer'],
               'third': [6, 'Computer']}
blackjack_top3 = {'first': [0, 'Computer'], 'second': [0, 'Computer'],
                  'third': [0, 'Computer']}
clicker_top3 = {'first': [0, 'Computer'], 'second': [0, 'Computer'],
                'third': [0, 'Computer']}
# Sets up widths and heights for some buttons
button_width = 20
button_height = 5
# begin loading screen window
root = Tk()
title = 'The Great Games Compendium'
root.title(title)
root.configure(bg='light grey')
# Specify window size
width = 800
height = 450
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
# create a quick frame
frame = Frame(root, bg='light grey')
frame.pack(pady=20)
label = Label(frame, text=title, font=('Helvetica', 24))
# Loading screen
pg = Progressbar(frame, orient="horizontal", length=500,
                 mode="determinate")
pg.grid(row=2, column=1, columnspan=2)
# Enter in username
Label(frame, text="Enter username:", bg='light grey').grid(row=0, column=1,
                                          columnspan=2, pady=(50, 0))
user = Entry(frame)
user.grid(row=1, column=1, columnspan=2, pady=(5, 25))
# button that checks for username and starts loading it if present
start_button = Button(frame, text="Start game", width=button_width,
                      height=button_height, command=start_loading)
start_button.grid(row=3, column=1, columnspan=2, pady=50)
root.mainloop()
