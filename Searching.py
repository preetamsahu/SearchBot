from tkinter import *
import wikipedia
import time

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
    try:
        status_var.set("Searching..........")
        text_value=wikipedia.summary(enter_value)
        text.insert(INSERT,text_value)
    except Exception as e:
        status_var.set("Searching..........")
        text.insert(INSERT,e)
    status_var.set("Result")
    pass


#Cretaing Entry Label
frame1=Frame(window,bg="cadet blue")
frame1.pack(side=TOP)
Label(frame1,text="Type Here").pack(side=LEFT)
entry=Entry(frame1,width=40,font="Times 12")
entry.pack(side=LEFT)

#Creating Searchh Butto

search_btn=Button(frame1,text="Search",borderwidth=12,bg="dodger blue",relief=SUNKEN,fg="black",padx=13)
search_btn.pack(side=LEFT,padx=12)
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
