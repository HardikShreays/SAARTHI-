from http.client import responses

from google.generativeai.notebook.post_process_utils import resolve_post_processing_tokens
from uritemplate import expand

from Gemini import send_message
from tkinter import *
CNT = 1



def sendmessage():
    global CNT
    msg = message.get()
    message.set("")
    if not msg:
        return
    log.insert(CNT, "YOU: " + msg)
    log.yview_moveto(1)
    CNT += 1
    respose = send_message(msg)

    log.insert(CNT, "AVIS: " + respose)
    log.yview_moveto(1)
    CNT += 1


ROOT = Tk()
ROOT.geometry("500x400")

ROOT.title("SAARTHI ")

log = Listbox(ROOT, width=25, height=15, relief=SUNKEN, borderwidth=4,font="lucica 15")
log.place(x=0, y=0, width = 1000)
scrollbar= Scrollbar(ROOT, orient= 'vertical')
scrollbar2= Scrollbar(ROOT, orient= 'horizontal')
scrollbar.pack(side= RIGHT, fill= BOTH)
scrollbar2.pack(side= BOTTOM, fill= BOTH)
log.config(yscrollcommand= scrollbar.set)
log.config(xscrollcommand= scrollbar2.set)
#Configure the scrollbar
scrollbar.config(command= log.yview)
scrollbar2.config(command= log.xview)

message = StringVar()
message_box = Entry(ROOT, textvariable=message, font="lucica 15", relief=GROOVE, width=20, borderwidth=4)
message_box.place(x=0, y=365)

Button(text="Send", font="lucica 16", relief=RAISED,
       command=sendmessage).place(x=210, y=367)


# log.insert(CNT, host_msg)
# CNT +=1
ROOT.mainloop()