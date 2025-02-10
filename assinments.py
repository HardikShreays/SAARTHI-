from tkinter import *
import pickle
def submit():
    pass

root = Tk()
f = open("Ass.bin",'rb')
root.geometry("900x700")
root.configure(bg="#628B48")
root.title("SAARTHI - Assignments ")
text = pickle.load(f)
Label(text = text ,font ="lucica 28",bg = "#F3F9E3",fg = "black").place(x=30, y=20)
submission = StringVar()
Entry(textvariable=submission,font="lucica 15", relief=GROOVE, width=70, borderwidth=4).place(x = 30, y = 80,height=70)

Button(text = "Submit", relief=RAISED,command=submit).place(x = 30, y = 150)
root.mainloop()