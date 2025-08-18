"""11DGT Assessment 11.3.

stuff for doing the tkinter assessment
"""

# This code creates a simple Tkinter window.
import tkinter
m = tkinter.Tk()
m.mainloop()
""""""
# This code creates a simple Tkinter window with a label.
from tkinter import *
root = Tk()
w = Label(root, text="Silksong Tomorrow!")
w.pack()
root.mainloop()
""""""
# This code creates a Tkinter window with a button that closes the window when clicked.
import tkinter as tk
r = tk.Tk()
r.title('Silksong release date')
button = tk.Button(r, text='Now', width=25, command=r.destroy)
button.pack()
r.mainloop()
""""""
# This code creates a Tkinter window with two text entry fields for first name and last name.
from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
""""""
# This code creates a Tkinter window with two checkboxes for selecting options.
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='Believer', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='Denier', variable=var2).grid(row=1, sticky=W)
mainloop()
""""""
# This code creates a Tkinter window with two radio buttons for selecting a character.
from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='Champion of Fools', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Invincible, Fearless, Sensual, Mysterious, Enchanting, Vigorous, Diligent, Overwhelming, Gorgeous, Passionate, Terrifying, Beautiful, Powerful Grey Prince Zote', variable=v, value=2).pack(anchor=W)
mainloop()
""""""
# This code creates a Tkinter window with a listbox containing titles.
from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Hollow Knight')
Lb.insert(2, 'Silksong')
Lb.insert(3, 'Grimm Troupe')
Lb.insert(4, 'Godmaster')
Lb.insert(5, 'The White Lady')
Lb.insert(6, 'The Radiance')
Lb.pack()
top.mainloop()
""""""
# This code creates a Tkinter window with a scrollbar and a listbox that can be scrolled.
from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'Days waiting for Silksong: ' + str(line))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()
""""""
# This code creates a Tkinter window with a menu bar containing File and Help menus.
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()
""""""
# This code creates a Tkinter window with a combobox for selecting a game title.
import tkinter as tk
from tkinter import ttk
def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

# creating a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

# Create a Combobox Widget
combo_box = ttk.Combobox(root, values=["Hollow Knight", "Silksong", "Grimm Troupe", "Godmaster", "The White Lady", "The Radiance"], state='readonly')
combo_box.pack(pady=5)

# Set default value
combo_box.set("Select a game")

# Bind event to section
combo_box.bind("<<ComboboxSelected>>", select)
root.mainloop()
""""""
# This code creates a Tkinter window with two scales: one vertical and one horizontal.
from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()
""""""
# This code creates a Tkinter window with a top-level window titled "Silksong".
from tkinter import *
root = Tk()
root.title('Silksong release date')
top = Toplevel()
top.title('Silksong')
top.mainloop()
""""""
# This code creates a Tkinter window with a message widget displaying a message.
from tkinter import *
main = Tk()
ourMessage = 'Silksong comes out tomorrow!'
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()
""""""
# This code creates a Tkinter window with a menubutton containing two checkbuttons.
from tkinter import *
top = Tk()
mb = Menubutton(top, text = "Silksong")
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton(label = 'Champion of Fools', variable = cVar)
mb.menu.add_checkbutton(label = 'Invincible, Fearless, Sensual, Mysterious, Enchanting, Vigorous, Diligent, Overwhelming, Gorgeous, Passionate, Terrifying, Beautiful, Powerful Grey Prince Zote', variable = aVar)
mb.pack()
top.mainloop()
""""""
# This code creates a Tkinter window with a progress bar that simulates a download process.
import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # simulate a task that takes time to complete
    for i in range(101):
        # Simulate some work
        time.sleep(0.05)
        progress['Value'] = i
        # Update the GUI
        root.update_idletasks()
    progress.stop()

root = tk.Tk()
root.title("Silksong Download Progress")
# Create a progressbar widget
progress = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress.pack(pady=20)
# Button to start the progress
start_button = tk.Button(root, text="Start Download", command=start_progress)
start_button.pack(pady=10)
root.mainloop()
""""""
# This code creates a Tkinter window with a spinbox for selecting a number.
from tkinter import *   
master = Tk()
w = Spinbox(master, from_=0, to=10)
w.pack()
mainloop()
""""""
# This code creates a Tkinter window with a text widget that displays multiple lines of text.
from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'Silksong comes out tomorrow!\nNUH UH!\n\nYUH HUH!\n')
mainloop()
""""""
# This code creates a Tkinter window with a canvas that draws a horizontal line.
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()
