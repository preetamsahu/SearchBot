from tkinter import *
import wikipedia
import time
import speech_recognition as sr
from PIL import ImageTk,Image

window=Tk()
window.geometry("500x600")
window.title("Search Information abouter any thing")
window.config(background="cadet blue")

#Definig answer
def get_answer(event):
    enter_value=entry.get()
    text.delete(1.0,END)
    status_var.set(f"Searching.......... {event.x} {event.y}")
    status_bar.update()
    if entry.get()=="preetam" or entry.get()=="Preetam Sahu" or entry.get()=="Preetam" or entry.get()=="preetam sahu" or entry.get()=="PREETAM SAHU":
        text.insert(INSERT,"Preetam , his complete name is Preetam Sahu , he is an CS student in BIT college i.e Bhilai Institue of technology.  He is participating  in BITSHINE with his three friends kushal,Nikhil and rahul . They made Search bot that can put the information infront of you in very concise manner.")
    else:
        try:
            status_var.set("Searching..........")
            text_value=wikipedia.summary(enter_value)
            text.insert(INSERT,text_value)
        except Exception as e:
            text.insert(INSERT,e)
    status_var.set("Result")

def vice():
    text.delete(1.0,END)
    status_var.set("Speak Now...............")
    status_bar.update()
    audio=sr.Recognizer()
    with sr.Microphone() as source:
        try:
            speech=audio.listen(source)
            get=audio.recognize_google(speech,language="eng-in")
            status_var.set("Searching.........")
            status_bar.update()
            text.insert(INSERT,f"Aboute {get}\n")
            value=wikipedia.summary(get)
            text.insert(INSERT,value)
        except Exception as e:
            text.insert(INSERT,e)
    status_var.set("Result")
#Cretaing Entry Label
frame1=Frame(window,bg="cadet blue")
frame1.pack(side=TOP)

#Adding Image in voice Button
image_btn=Image.open("mic.ico")
resized_image=image_btn.resize((30,20),Image.ANTIALIAS)
mic_btn=ImageTk.PhotoImage(resized_image)

#Creating Vice Reconizer
Button(frame1,image=mic_btn,borderwidth=0,command=vice).pack(side=LEFT)

Label(frame1,text="Type Here").pack(side=LEFT)
entry=Entry(frame1,width=40,font="Times 12")
entry.pack(side=LEFT)

#Adding Image in Search Button
search_imag=Image.open("search.png")
resized=search_imag.resize((25,20),Image.ANTIALIAS)
new_searchpic=ImageTk.PhotoImage(resized)

#Creating Searchh Butto

search_btn=Button(frame1,image=new_searchpic,borderwidth=0)
search_btn.pack(side=LEFT)
search_btn.bind("<Button-1>",get_answer)


#Creating Text

scroll=Scrollbar(window)
scroll.pack(side=RIGHT,fill=Y)

text=Text(window,yscrollcommand=scroll.set,fg="midnight blue",font="Times 15 italic",wrap=WORD)
text.pack(expand=True,fill=BOTH)
scroll.config(command=text.yview)
#Creating Statu Bar
status_var=StringVar()
status_var.set("Search")
status_bar=Label(window,text="Search",textvariable=status_var,bg="cadet blue",font="Times 15 italic")
status_bar.pack(side=LEFT,fill=X)
window.mainloop()
