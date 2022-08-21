from matplotlib import font_manager

font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

font_manager.findfont("Special Elite")

from cProfile import label

from distutils.command.config import config

from json.tool import main

from tkinter import * 

from tkinter.ttk import *

from time import strftime

from matplotlib import ticker

from matplotlib.pyplot import text

main = Tk()

main.title('The Digital Clock In Python')

def clock():

    tick = strftime('%H:%M:%S %p')

    clock_label .config(text =tick)
    
    clock_label .after(1000, clock)

clock_label = Label(main, font=('Special Elite', 80), background='black', foreground='red')

clock_label.pack(anchor='center')

clock()

mainloop()