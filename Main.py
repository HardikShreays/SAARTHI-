from tkinter import *
import os
import threading

def Bot_thread(fumc):
    thread = threading.Thread(target=fumc)
    thread.start()

def Chabot():
    os.system("python3 Chatbot.py")

def Assing():
    os.system("python3 assinments.py")
def explore():
    os.system("python3 Explore.py")

root = Tk()
root.geometry("900x700")
root.configure(bg="#628B48")
root.title("SAARTHI - HARDIK")
Label(text = "Hey there wassup \n What do you Want to do you:",font ="lucica 28",bg = "#F3F9E3",fg = "black").place(x=250, y=250)

Button(text="Assisments", font="lucica 28", relief=RAISED,command=lambda:Bot_thread(Assing)).place(x=150, y=360)
Button(text=" Let's Talk", font="lucica 28", relief=RAISED,command=lambda:Bot_thread(Chabot)).place(x=350, y=360)
Button(text="Explore", font="lucica 28", relief=RAISED,command=lambda:Bot_thread(explore)).place(x=550, y=360)

root.mainloop()