
from tkinter import *


text = """
1. Shloka 2.48 (Chapter 2, Verse 48)
In Sanskrit:
योगस्थः कुरु कर्माणि सङ्गं त्यक्त्वा धनञ्जय।

सिद्ध्यसिद्ध्योः समो भूत्वा समत्वं योग उच्यते।।

yogasthaḥ kuru karmāṇi saṅgaṃ tyaktvā dhanañjaya

siddhyasiddhyoḥ samo bhūtvā samatvaṃ yoga ucyate

Translation (Meaning in English): 
Be steadfast in yoga, O Arjuna. Perform your duty and abandon all attachments to success or failure. Such evenness of mind is called yoga.

Lessons:
In this shloka, Lord Krishna advises Arjuna to perform his duties with an evenness of mind, without getting attached to the outcome. He emphasizes the importance of detachment and encourages Arjuna to focus on the present moment and the task at hand, rather than worrying about the future or regretting the past. 

By doing so, one can achieve a state of balance and equanimity, which is the ultimate goal of yoga. This shloka from Bhagavad Gita teaches us the importance of being focused and present in our actions, and not getting bogged down by the fear of failure or the desire for success.
"""
ROOT = Tk()
ROOT.geometry("500x400")
ROOT.configure(bg="#628B48")
# ROOT.wm_maxsize(width=500, height=400)
# ROOT.wm_minsize(width=500, height=400)
ROOT.title("EXPLORE - SAARTHI")
scrollbar= Scrollbar(ROOT, orient= 'vertical')
scrollbar.pack(side= RIGHT, fill= BOTH)
Label(text = "Explore",font ="lucica 28",bg = "#F3F9E3",fg = "black").pack(side = TOP, anchor = 'n', fill = X)
Label(text = text,font ="lucica 28").pack(anchor = "w")

ROOT.mainloop()