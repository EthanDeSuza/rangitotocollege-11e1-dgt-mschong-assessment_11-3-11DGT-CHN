"""11DGT Assessment 11.3.

This is the main file that runs all the
stuff for doing the tkinter assessment.
"""

from tkinter import *
from tkinter.ttk import Progressbar
import random

def wordle():  # Wordle game window

    """Begin the wordle game.

    Runs the wordle game and displayes it to the user.
    """
    wordle_win = Tk()
    title = 'Wordle'
    wordle_win.title(title)
    # Specify window size
    width = 400
    height = 700
    wordle_win.geometry('{}x{}'.format(width, height))
    # Create a frame
    interface_frame = Frame(wordle_win)
    interface_frame.pack(pady=30)
    # Sets a word for wordle
    words = ['great', 'games', 'frame', 'comic', 'micro', 'apple',
             'seven', 'sixty', 'point', 'crows', 'straw', 'users',
             'ducks', 'mouse', ]
    correct_word = random.choice(words)

    def gamble_start():
        wordle_win.destroy()
        blackjack()

    def clicker_start():
        wordle_win.destroy()
        clicker()

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
        instruct = Label(wordle_structs, text="How to play",
                         font=('Helvetica', 24, 'underline'))
        instruct.grid(row=0, column=0)
        wordle_struct = Label(wordle_structs, text='To play wordle you'
                              'guess a five letter word,\nthen when you '
                              'press the guess button you will be show\n'
                              'which of your letters are incorrect, '
                              'in the wrong place\nor correct.',
                              font=('Helvetica', 12))
        wordle_struct.grid(row=1, column=0)
    # a navbar and help menu at the top of window
    menu = Menu(wordle_win)
    wordle_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Blackjack', command=gamble_start)
    navmenu.add_command(label='clicker', command=clicker_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=wordle_win.destroy)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='Wordle Instructions', command=wordle_instruct)
    global guess, result

    def checkword():


        """Checks the word.


        Compares word given with correct answer to return which letters
        are correct.
        """
        global guesses, guess, result  # Grabs the global guesses variable
        if guesses <= 5:  # Limits the players guesses to 6
            if guess.get().lower() == correct_word:  # Check word with correct
                result.destroy()
                for i in range(0, 5):
                    # shows the player all the letter's are correct
                    box = Label(interface_frame, text=guess.get().upper()[i],
                                bg='green', fg='white', width=10, height=5)
                    box.grid(row=guesses+4, column=i + 1)
                # tells the player it's the correct word
                result = Label(interface_frame, text="You guessed the right"
                               f'word!\nIt took you {guesses+1} guesses.')
                result.grid(row=guesses+5, column=1, columnspan=5)
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
                result.destroy()
                result = Label(interface_frame,
                               text="Your guess must be 5 letters")
                result.grid(row=guesses+6, column=3, columnspan=5)
            else:
                result.destroy()
                for i in range(0, 5):
                    if guess.get().lower()[i] == correct_word[i]:
                        box = Label(interface_frame, bg='green',
                                    text=guess.get().upper()[i],
                                    fg='white', width=10, height=5)
                        box.grid(row=guesses + 4, column=i + 1)
                    elif guess.get().lower()[i] in correct_word:
                        box = Label(interface_frame, bg='orange',
                                    text=guess.get().upper()[i],
                                    fg='white', width=10, height=5)
                        box.grid(row=guesses + 4, column=i + 1)
                    else:
                        box = Label(interface_frame, bg='grey',
                                    text=guess.get().upper()[i],
                                    fg='white', width=10, height=5)
                        box.grid(row=guesses+4, column=i+1)
                guesses += 1
                guess.destroy()
                guess = Entry(interface_frame, width=9)
                guess.grid(row=2, column=3, columnspan=2, padx=5)
        if guesses > 5:
            result = Label(interface_frame,
                           text="Out of guesses, the word was: "
                           + correct_word)
            result.grid(row=guesses+5, column=1, columnspan=5)
            guess.destroy()
            submit.destroy()
            textguess.destroy()
            retry = Button(interface_frame, text="Retry?",
                           width=button_width, height=button_height,
                           command=reload_game)
            exit = Button(interface_frame, text="Exit to menu?",
                          width=button_width, height=button_height,
                          command=close_game)
            retry.grid(row=guesses+6, column=1, columnspan=2)
            exit.grid(row=guesses+6, column=4, columnspan=2)
            guesses = 0
    # creates a correct alignment for the whole game
    for repeat in range(0, 5):
        box = Label(interface_frame, width=10, height=5)
        box.grid(row=4, column=repeat+1)
    # title for on the window
    title_label = Label(interface_frame, text=title,
                        font=('Helvetica', 32))
    title_label.grid(row=0, column=1, columnspan=5)
    # the guessing word entry and button
    textguess = Label(interface_frame, text="Guess a word:")
    guess = Entry(interface_frame, width=9)
    submit = Button(interface_frame, text="Guess", width=9,
                    height=int(button_height/2), command=checkword)
    textguess.grid(row=2, column=2, columnspan=2, pady=5, padx=5)
    guess.grid(row=2, column=3, columnspan=2, padx=5)
    submit.grid(row=3, column=3)
    result = Label(interface_frame, text="")
    result.grid(row=guesses+6, column=3, columnspan=5)

def blackjack():
    """BlackJack game window.


    Begin the wordle game.
    """
    gamble_win = Tk()
    title = 'BlackJack'
    gamble_win.title(title)
    gamble_win.configure(bg='green')
    # Specify window size
    width = 1200
    height = 900
    gamble_win.geometry('{}x{}'.format(width, height))
    # create a frame
    interface_frame = Frame(gamble_win, bg='green')
    interface_frame.pack(pady=30)
    # setup frame grid
    label = Label(interface_frame, text=title, font=('Helvetica', 24))

    def wordle_start():
        gamble_win.destroy()
        wordle()

    def clicker_start():
        gamble_win.destroy()
        clicker()

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
    navmenu.add_command(label='clicker', command=clicker_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=gamble_win.destroy)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='BlackJack Instructions',
                         command=gamble_instruct)

    def beginbet():
        global continues, balance, returnmenu, cardshow1
        global cardshow2, card1, card2, yours, dnew, pnew, theirs
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
            theirs.destroy()
            for i in range(0, dnew):
                cover = Label(interface_frame, width=17,
                              height=10, background='green')
                cover.grid(row=3, column=i+2)
            for i in range(0, pnew):
                cover = Label(interface_frame, width=17, height=10,
                              background='green')
                cover.grid(row=5, column=i+2)
            yours.destroy()
            bettingtime()

    def check_winner():
        global total, dtotal, gamble, td, hit, stand, continues, returnmenu
        hit.destroy()
        stand.destroy()
        if total > dtotal and total < 22 or dtotal > 21 and total < 22:
            print('player wins')
            td += gamble * 2
            continues = Button(interface_frame, width=10, height=4,
                               text='Continue?', command=beginbet)
            continues.grid(row=4, column=3, pady=5)
            returnmenu = Button(interface_frame, width=10, height=4,
                                text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=1, pady=5)
        elif dtotal == total or dtotal > 21 and total > 21:
            print('tie')
            td += gamble
            continues = Button(interface_frame, width=10, height=4,
                               text='Continue?', command=beginbet)
            continues.grid(row=4, column=3, pady=5)
            returnmenu = Button(interface_frame, width=10, height=4,
                                text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=1, pady=5)
        elif dtotal > total and dtotal < 22 or total > 21 and dtotal < 22:
            print('dealer wins')
            continues = Button(interface_frame, width=10, height=4,
                               text='Continue?', command=beginbet)
            continues.grid(row=4, column=3, pady=5)
            returnmenu = Button(interface_frame, width=10, height=4,
                                text='Exit to menu?', command=close_game)
            returnmenu.grid(row=4, column=1, pady=5)
            if td <= 0:
                global username, td_save
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
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
    for repeat in range(0, 5):
        box = Label(interface_frame, width=17, height=7, bg='green')
        box.grid(row=5, column=repeat)
    gametitle = Label(interface_frame, text='BlackJack', bg='green',
                      font=('helvetica', 25))
    gametitle.grid(row=0, column=2)
    global td, pnew, dnew, balance
    td = 100

    def ten():
        global td, gamble, balance, td_save
        gamble = 10
        td_save = td
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()

    def fifty():
        global td, gamble, balance, td_save
        gamble = 50
        td_save = td
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()

    def hundy():
        global td, gamble, balance, td_save
        gamble = 100
        td_save = td
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()

    def half():
        global td, gamble, balance, td_save
        gamble = td//2
        td_save = td
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()

    def all():
        global td, gamble, balance, td_save
        td_save = td
        gamble = td
        td -= gamble
        balance.destroy()
        balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
        balance.grid(row=0, column=4)
        drawcards()

    def bettingtime():
        begin.destroy()
        global bet10, bet50, bet100, bethalf, betall, howmuch, balance
        howmuch = Label(interface_frame, bg='green',
                        text='How much would you like to bet?')
        howmuch.grid(row=2, column=0, columnspan=5)
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
        bet10.grid(row=3, column=0)
        bet50.grid(row=3, column=1)
        bet100.grid(row=3, column=2)
        bethalf.grid(row=3, column=3)
        betall.grid(row=3, column=4)
    begin = Button(interface_frame, width=20, height=5, text='Begin Game',
                   command=bettingtime)
    begin.grid(row=3, column=2)
    balance = Label(interface_frame, text=f'Tiddlywinks: {td}', bg='green')
    balance.grid(row=0, column=4)
    cards = [13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11, 10, 10, 10, 10,
             9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4,
             4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]
    pnew = 0
    dnew = 0

    def addcard():
        global cardnum, total, yours, pnew_card, pnew
        newcard = random.choice(cards)
        cards.remove(newcard)
        pnew_card = Label(interface_frame, width=17, height=10, text=newcard,
                          background='light grey')
        pnew_card.grid(row=5, column=cardnum)
        yours.destroy()
        total += newcard
        yours = Label(interface_frame, text=f'Your cards:\ntotal: {total}',
                      bg='green')
        yours.grid(row=4, column=2)
        cardnum += 1
        pnew += 1
        if total > 21:
            endturn()

    def endturn():
        global dcard1, dcard2, dtotal, dnew_card, cardshow2, dnew, theirs
        cardshow2.destroy()
        cardshow2 = Label(interface_frame, width=17, height=10, text=dcard2,
                          background='light grey')
        cardshow2.grid(row=3, column=1)
        dtotal = dcard1+dcard2
        cardnum = 2
        end = 0
        while end == 0:
            if dtotal < 16:
                dnew += 1
                newcard = random.choice(cards)
                cards.remove(newcard)
                dnew_card = Label(interface_frame, width=17, height=10,
                                  text=newcard, background='light grey')
                dnew_card.grid(row=3, column=cardnum)
                cardnum += 1
                dtotal += newcard
                theirs = Label(interface_frame,  bg='green',
                               text=f'Dealers cards:\ntotal: {dtotal}')
                theirs.grid(row=2, column=2)
            else:
                end = 1
                check_winner()

    def drawcards():
        global bet10, bet50, bet100, bethalf, betall, howmuch
        global dcard1, dcard2, total, cardnum, yours, hit, stand
        global card1, card2, cardshow1, cardshow2, theirs
        cards = [13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11,
                 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7,
                 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3,
                 2, 2, 2, 2, 1, 1, 1, 1]
        cardnum = 0
        bet10.destroy()
        bet50.destroy()
        bet100.destroy()
        bethalf.destroy()
        betall.destroy()
        howmuch.destroy()
        hit = Button(interface_frame, width=10, height=4, text='Hit',
                     command=addcard)
        hit.grid(row=4, column=1, pady=5)
        stand = Button(interface_frame, width=10, height=4, text='Stand',
                       command=endturn)
        stand.grid(row=4, column=3, pady=5)
        # Draws your first card
        pcard1 = random.choice(cards)
        cards.remove(pcard1)
        print(pcard1)
        card1 = Label(interface_frame, width=17, height=10, text=pcard1,
                      background='light grey')
        card1.grid(row=5, column=cardnum)
        cardnum += 1
        # Draws dealers first card
        dcard1 = random.choice(cards)
        cards.remove(dcard1)
        print(dcard1)
        cardshow1 = Label(interface_frame, width=17, height=10, text=dcard1,
                          background='light grey')
        cardshow1.grid(row=3, column=0)
        # Draws your second card
        pcard2 = random.choice(cards)
        while pcard2 + pcard1 > 21:
            pcard2 = random.choice(cards)
        cards.remove(pcard2)
        print(pcard2)
        card2 = Label(interface_frame, width=17, height=10, text=pcard2,
                      background='light grey')
        card2.grid(row=5, column=cardnum)
        cardnum += 1
        # Draws dealers second card
        dcard2 = random.choice(cards)
        while dcard2 + dcard1 > 21:
            dcard2 = random.choice(cards)
        cards.remove(dcard2)
        print(dcard2)
        cardshow2 = Label(interface_frame, width=17, height=10,
                          background='dark green')
        cardshow2.grid(row=3, column=1)
        total = pcard1+pcard2
        yours = Label(interface_frame, bg='green',
                      text=f'Your cards:\ntotal: {total}')
        yours.grid(row=4, column=2)
        theirs = Label(interface_frame, bg='green',
                       text=f'Dealers cards:\ntotal: {dcard1}')
        theirs.grid(row=2, column=2)
    gamble_win.mainloop()

def clicker():  # clicker game window
    clicker_win = Tk()
    clicker_win.title('GeoClicker')
    clicker_win.configure(bg='dark grey')
    # Specify window size
    width = 500
    height = 750
    clicker_win.geometry('{}x{}'.format(width, height))
    # create a frame
    interface_frame = Frame(clicker_win, bg='light grey')
    interface_frame.pack(padx=50, pady=50)
    # setup frame grid
    label = Label(interface_frame, text=title, font=('Helvetica', 24))

    def wordle_start():
        global end
        end = True
        clicker_win.destroy()
        wordle()

    def gamble_start():
        global end
        end = True
        clicker_win.destroy()
        blackjack()

    def reload_game():  # Restarts the game
        global end
        end = True
        clicker_win.destroy()
        clicker()

    def close_game():
        global end
        end = True
        clicker_win.destroy()
        create_menu()
    def clicker_struct():
        clicker_structs = Tk()
        clicker_structs.title('Clicker Instructions')
        clicker_structs.resizable(False, False)
        clicker_struct = Label(clicker_structs, text='', font=('Helvetica', 12))
        clicker_struct.grid(row=1, column=0)
    # a navbar and help menu at the top of window
    menu = Menu(clicker_win)
    clicker_win.config(menu=menu)
    navmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Navigation', menu=navmenu)
    navmenu.add_command(label='Wordle', command=wordle_start)
    navmenu.add_command(label='clicker', command=gamble_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit to menu', command=close_game)
    navmenu.add_command(label='Exit', command=clicker_win.destroy)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='Clicker Instructions',
                         command=clicker_struct)
    global geo, mult, bank, miners, mult_cost, miner_cost, pick_cost, pick, end, lifeblood, lifeblood_cost, counter
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
    bank = Label(interface_frame, text=f'Geo: {geo}', fg='black', bg='light grey')
    bank.grid(row=2, column=2)
    def mine():
        global geo, mult, bank
        geo += mult
        bank.destroy()
        bank = Label(interface_frame, text=f'Geo: {geo}', fg='black', bg='light grey')
        bank.grid(row=2, column=2)
    def upgrade_win():
        global geo, mult, upgrader, mult_upgrade, miner_hire, pick_cost, pick_enhance, lifeblood_enhance, lifeblood_cost
        upgrader = Tk()
        upgrader.title('Upgrades')
        upgrader.geometry('400x600')
        upgrader.resizable(False, False)
        titles = Label(upgrader, text='Upgrades', font=('Helvetica', 24))
        titles.grid(row=0, column=0, columnspan=3, padx=130)
        mult_upgrade = Button(upgrader, text=f'Increase Geo per click by 1\nCost: {mult_cost} Geo', command=mult_upgradefunct)
        mult_upgrade.grid(row=1, column=0)
        miner_hire = Button(upgrader, text=f'Hire a husk miner\nCost: {miner_cost} Geo', command=miner_purchase)
        miner_hire.grid(row=1, column=2)
        pick_enhance = Button(upgrader, text=f"Upgrade the husk miner's pickaxe\nCost: {pick_cost} Geo", command=pick_upgrade)
        pick_enhance.grid(row=3, column=0)
        lifeblood_enhance = Button(upgrader, text=f"Buy lifeblood for the husk miner\nCost: {lifeblood_cost} Geo", command=lifeblood_upgrade)
        lifeblood_enhance.grid(row=3, column=2)

    def miner_purchase():
        global geo, bank, miner_cost, miner_hire, upgrader, miners
        if geo >= miner_cost:
            geo -= miner_cost
            miners += 1
            miner_cost = int(miner_cost * 2.5)
            bank.destroy()
            bank = Label(interface_frame, text=f'Geo: {geo}', fg='black', bg='light grey')
            bank.grid(row=2, column=2)
            miner_hire.destroy()
            miner_hire = Button(upgrader, text=f'Hire a husk miner\nCost: {miner_cost} Geo', command=miner_purchase)
            miner_hire.grid(row=1, column=2)
            amount = Label(upgrader, text=f'You have purchased this {miners} times.')
            amount.grid(row=2, column=2)
    
    def lifeblood_upgrade():
        global geo, bank, lifeblood_cost, upgrader, lifeblood, lifeblood_enhance, counter
        if geo >= lifeblood_cost:
            geo -= lifeblood_cost
            lifeblood *= 0.9
            counter += 1
            lifeblood_cost = int(lifeblood_cost * 2.5)
            bank.destroy()
            bank = Label(interface_frame, text=f'Geo: {geo}', fg='black', bg='light grey')
            bank.grid(row=2, column=2)
            lifeblood_enhance.destroy()
            lifeblood_enhance = Button(upgrader, text=f'Hire a husk miner\nCost: {lifeblood_cost} Geo', command=lifeblood_upgrade)
            lifeblood_enhance.grid(row=3, column=2)
            amount = Label(upgrader, text=f'You have purchased this {counter} times.')
            amount.grid(row=4, column=2)

    def pick_upgrade():
        global geo, bank, pick_cost, upgrader, pick, pick_enhance
        if geo >= pick_cost:
            geo -= pick_cost
            pick += 1
            pick_cost = int(pick_cost * 3.5)
            bank.destroy()
            bank = Label(interface_frame, text=f'Geo: {geo}', fg='black', bg='light grey')
            bank.grid(row=2, column=2)
            pick_enhance.destroy()
            pick_enhance = Button(upgrader, text=f"Upgrade the husk miner's pickaxe\nCost: {pick_cost} Geo", command=pick_upgrade)
            pick_enhance.grid(row=3, column=0)
            amount = Label(upgrader, text=f'You have purchased this {pick-1} times.')
            amount.grid(row=4, column=0)
    def mult_upgradefunct():
        global geo, mult, mult_cost, bank, mult_upgrade, upgrader
        if geo >= mult_cost:
            geo -= mult_cost
            mult += 1
            mult_cost = int(mult_cost * 1.5)
            bank.destroy()
            bank = Label(interface_frame, text=f'Geo: {geo}', fg='black', bg='light grey')
            bank.grid(row=2, column=2)
            mult_upgrade.destroy()
            mult_upgrade = Button(upgrader, text=f'Increase Geo per click by 1\nCost: {mult_cost} Geo', command=mult_upgradefunct)
            mult_upgrade.grid(row=1, column=0)
            amount = Label(upgrader, text=f'You have purchased this {mult-1} times')
            amount.grid(row=2, column=0)
    geoclicker = Label(interface_frame, text='GeoClicker', bg='light grey', font=('Helvetica', 32))
    geoclicker.grid(row=0, column=0, columnspan=5)
    mine_geo = Button(interface_frame, text='Mine Geo', width=10, height=5, font=('Helvetica', 12), command=mine)
    mine_geo.grid(row=5, column=2)
    upgrades = Button(interface_frame, text='Upgrades', width=20, height=2, command=upgrade_win)
    upgrades.grid(row=6, column=1)
    rebirth = Button(interface_frame, text='Rebirth', width=20, height=2)
    rebirth.grid(row=6, column=3)
    def mine_auto():
        global miners, geo, bank, pick, end, lifeblood
        if end == True:
            return
        geo += miners * pick
        bank.destroy()
        bank = Label(interface_frame, text=f'Geo: {geo}', fg='black', bg='light grey')
        bank.grid(row=2, column=2)
        clicker_win.after(int(lifeblood), mine_auto)
        
    mine_auto()
    clicker_win.mainloop()



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
    clicker_scores = Label(root, text='clicker Highscores', font=('Helvetica', 24, 'bold'))
    clicker_scores.grid(row=9, column=2)
    clicker_scores = Label(root, text=f"First place: {clicker_top3['first'][1]} with {clicker_top3['first'][0]} points", font=('Helvetica', 10, 'italic'))
    clicker_scores.grid(row=10, column=2)
    clicker_scores = Label(root, text=f"Second place: {clicker_top3['second'][1]} with {clicker_top3['second'][0]} points", font=('Helvetica', 10, 'italic'))
    clicker_scores.grid(row=11, column=2)
    clicker_scores = Label(root, text=f"Third place: {clicker_top3['third'][1]} with {clicker_top3['third'][0]} points", font=('Helvetica', 10, 'italic'))
    clicker_scores.grid(row=12, column=2)
    root.mainloop()
# This code creates a Tkinter window with a menu bar containing File and Help menus.


def create_menu():
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
    navmenu.add_command(label='clicker', command=clicker_start)
    navmenu.add_command(label='Scoreboard', command=scoreboard_start)
    navmenu.add_separator()
    navmenu.add_command(label='Exit', command=menu_win.destroy)
    namemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Change username', menu=namemenu)
    namemenu.add_command(label='Change name', command=change_name)
    scoremenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Scoreboard', menu=scoremenu)
    scoremenu.add_command(label='Wordle Leaderboard')
    scoremenu.add_command(label=f"First place: {wordle_top3['first'][1]} with {wordle_top3['first'][0]} guesses", font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Second place: {wordle_top3['second'][1]} with {wordle_top3['second'][0]} guesses", font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Third place: {wordle_top3['third'][1]} with {wordle_top3['third'][0]} guesses", font=('Helvetica', 10, 'italic'))
    scoremenu.add_separator()
    scoremenu.add_command(label='Blackjack Leaderboard')
    scoremenu.add_command(label=f"First place: {blackjack_top3['first'][1]} with {blackjack_top3['first'][0]} tiddlywinks", font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Second place: {blackjack_top3['second'][1]} with {blackjack_top3['second'][0]} tiddlywinks", font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Third place: {blackjack_top3['third'][1]} with {blackjack_top3['third'][0]} tiddlywinks", font=('Helvetica', 10, 'italic'))
    scoremenu.add_separator()
    scoremenu.add_command(label='clicker Leaderboard')
    scoremenu.add_command(label=f"First place: {clicker_top3['first'][1]} with {clicker_top3['first'][0]} points", font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Second place: {clicker_top3['second'][1]} with {clicker_top3['second'][0]} points", font=('Helvetica', 10, 'italic'))
    scoremenu.add_command(label=f"Third place: {clicker_top3['third'][1]} with {clicker_top3['third'][0]} points", font=('Helvetica', 10, 'italic'))
    title_label = Label(menu_frame, text=f"Hello {username}! Welcome to \n{title}", font=('Helvetica', 32, 'bold'))
    title_label.grid(row=0, column=0, columnspan=3)
    # button for each of the game windows
    buttonw = Button(menu_frame, text='Play Wordle', width=button_width, height=button_height, command=wordle_start)
    buttonb = Button(menu_frame, text='Play BlackJack', width=button_width, height=button_height, command=gamble_start)
    buttons = Button(menu_frame, text='Play clicker', width=button_width, height=button_height, command=clicker_start)
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
# Sets up some global variables for the wordle game
guesses = 0
guess = ''
correct_word = ''
wordle_top3 = {'first':[6, 'Computer'], 'second':[6, 'Computer'], 'third':[6, 'Computer']}
blackjack_top3 = {'first':[0, 'Computer'], 'second':[0, 'Computer'], 'third':[0, 'Computer']}
clicker_top3 = {'first':[0, 'Computer'], 'second':[0, 'Computer'], 'third':[0, 'Computer']}
# Sets up widths and heights for some buttons
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
# setup frame grid
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
