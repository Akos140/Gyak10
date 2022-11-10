from tkinter import *

win = Tk()
win.title('Példa')
win.geometry('600x400')
win.minsize(width=300, height=200)

cimke1=Label(win, text='Szöveg', fg='blue')
cimke1.pack()
valtozo = stringvar