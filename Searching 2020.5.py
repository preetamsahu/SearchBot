from tkinter import *
import wikipedia
import time
import speech_recognition as sr
from PIL import ImageTk,Image
from tkinter import simpledialog as sm
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import asksaveasfilename
from gtts import gTTS
from win32com.client import Dispatch
from tkinter.font import Font

window=Tk()
window.geometry("500x600")
window.title("Search Bot")
window.config(background="#72dbdb")
window.minsize(600,700)

fox_list=[]
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

def save_file():
    global file
    desigion = tmsg.askyesno("Save","Want to Save This Information")
    try:
        if desigion:
            if text.Text=="":
                tmsg.showwarning("Waring", "There is No information to Save")

            else:
                file = asksaveasfilename(initialfile="Search Bot info", defaultextension=".txt",filetypes=[("All files", "*.*"), ("Text Document", ".txt")])
                fh = open(file, "w")
                fh.write(text.get(1.0, END))
                fh.close()
                status_var.set("Saved")
    except Exception as e:
        text.insert(INSERT,e)

def sound():
    def speak(str):
        speak = Dispatch(('SAPI.SpVoice'))
        speak.Speak(str)

    speak(text.get(1.0,END))
    #status_var.set("Done")
    #status_bar.update()


#Creating Search bot label
img_1=Image.open("back2.jpg")
resized3=img_1.resize((1536,60),Image.ANTIALIAS)
top_img=ImageTk.PhotoImage(resized3)
Label(window,image=top_img).pack()
print(window.winfo_screenwidth())
frame0=Frame(window,bg="#72dbdb")
frame0.pack()
#spelling=['S','e','a','r','c','h',"  ",'B','o','t']
#color=['blue','red','yellow','blue','green','red',"cadet blue", 'blue','red','green']
#count=0
#bot_var=StringVar()
#for spe in spelling:
#    for clr in range(1):
#        bot_label = Label(frame0,text=f"{spe}", font="Times 27 bold", borderwidth=0, bg="cadet blue", fg=f"{color[count]}")
#        bot_label.pack(side=LEFT)
       # bot_var.set(bot_var.get()+f"{spe}")
        #bot_label.config(fg=f"{color[count]}"

#    count+=1
#print(bot_label.getvar())
#Cretaing Entry Label
frame1=Frame(window,bg="#72dbdb")
frame1.pack(side=TOP)

#Adding Image in voice Button
image_btn=Image.open("mic.png")
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

#Creating Save Button
file=None
img=Image.open("save.ico")
resized=img.resize((25,20),Image.ANTIALIAS)
save_img=ImageTk.PhotoImage(resized)
save_btn=Button(frame1,image=save_img,command=save_file,borderwidth=0)
save_btn.pack(side=LEFT,padx=5)

#Creating Sound Button
img2=Image.open("sound.ico")
resized2=img2.resize((25,20),Image.ANTIALIAS)
sound_img=ImageTk.PhotoImage(resized2)
sound_btn=Button(frame1,image=sound_img,borderwidth=0,command=sound)
sound_btn.pack()


#Creating Text

scroll=Scrollbar(window)
scroll.pack(side=RIGHT,fill=Y)
text_var=StringVar()
text=Text(window,yscrollcommand=scroll.set,fg="#000000",font="Times 15 ",wrap=WORD)
text.pack(expand=True,fill=BOTH)
scroll.config(command=text.yview)
#Creating Statu Bar
status_var=StringVar()
status_var.set("Search")
status_bar=Label(window,text="Search",textvariable=status_var,bg="#72dbdb",font="Times 15 italic")
status_bar.pack(side=LEFT,fill=X)
window.mainloop()
