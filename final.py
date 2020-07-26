from tkinter import *
import os
from os import walk
from PIL import ImageTk, Image
from functions import *

from tkinter import messagebox

root = Tk()
root.geometry('800x500')

#Functations

def getpath():
     path = entry1.get()
     if vaildpath(path):
        listbox1.delete(0, 'end')
        for file in os.listdir(path):
          if file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".bmp") or file.endswith(".png"):
              listbox1.insert("end", file)
              
def showimage(path):
    getfile = listbox1.get("active")

    if entry1.get()[-1:] == "\\":
        im = Image.open(os.path.normpath(os.path.join(entry1.get() + getfile)))
    else:
        im = Image.open(os.path.normpath(os.path.join(entry1.get() + '\\' + getfile)))

    # resize
    while im.size[0] > 250 or im.size[1] > 300:
        x = int(im.size[0])
        y = int(im.size[1])
        im = im.resize((int(x*0.95), int(y*0.95)))

    tkimage = ImageTk.PhotoImage(im)


    imgLabel.configure(image=tkimage)
    imgLabel.image = tkimage
    imgLabel.place(x=400, y=55)

def vaildpath(path):
    return os.path.exists(os.path.normpath(path))

def vaildpath2(path2):
    return os.path.exists(os.path.normpath(path2))

def Saveimage (tkimage):
    path2=entry2.get()
    if vaildpath2(path2):
        listbox2.delete(0, "end")
        tkimage.save(getfile, "copy_of_img" + getfile)

#UI 
label1 = Label(root,text="Please enter image path:",font='Helvetica 10 bold')
label1.place(x=0,y=0)
entry1 = Entry(root, width=35)
entry1.place(x=0,y=25)
imgLabel = Label(root)
scrollbar1= Scrollbar(root)
scrollbar1.place(x=0, y=80)
listbox1 = Listbox(root, yscrollcommand=scrollbar1.set, selectmode=EXTENDED, height=10, exportselection=0)
scrollbar1.config(command=listbox1.yview)
listbox1.place(x=0, y=80)
listbox1.bind("<Button-1>", showimage)
button1=Button(root, text="Choose", bg="red", fg="white", font='Helvetica 10 bold', command = getpath)
button1.place(x=220, y=22)
label2 = Label(root, text="Please choose the images you would like to process:", font='Helvetica 10 bold')
label2.place(x=0, y=55)
label3 = Label(root, text="process operation selection:", font='Helvetica 10 bold')
label3.place(x=0, y=220)
listbox2 = Listbox(root, selectmode=EXTENDED, bd=4, height=4, bg='#CEFAD7')
listbox2.place(x=0, y=260)
label4 = Label(root,text="Please enter image path:", font='Helvetica 10 bold')
label4.place(x=0, y=360)
entry2 = Entry(root, width=35)
entry2.place(x=0, y=390)
button2=Button(root, text="Save", bg="green", fg="white", width = 7, font='Helvetica 10 bold', command=Saveimage)
button2.place(x=220, y=385)
#button2.bind("<Button-1>", Saveimage)







root.mainloop()


