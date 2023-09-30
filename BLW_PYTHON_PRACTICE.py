#CREATION OF REGISTRATION FORM

from sqlite3 import DateFromTicks
from tkinter import *
from turtle import bgcolor
from PIL import ImageTk, Image

def test():
    fnamev=fname_entry.get()
    lnamev=lname_entry.get()
    agev=age_entry.get()
    genderv=gender_entry.get()
    passwordv=password_entry.get()
    message1=" Your first name is "+fnamev+" and your last name is "+lnamev
    message2=" Your age is "+str(agev)+" and your gender is "+genderv
    message3=" your password is "+str(passwordv)
    output1=Label(window,text=message1, font='Helvetica 12 bold', bg="lightblue")
    output1.place(x=20,y=10)
    output2=Label(window,text=message2, font='Helvetica 12 bold', bg="lightblue")
    output2.place(x=20,y=40)
    output3=Label(window,text=message3, font='Helvetica 12 bold', bg="lightblue")
    output3.place(x=20,y=70)


window=Tk()
window.geometry("630x559")
window.title("MY PAGE")
window.iconbitmap('')
window.resizable(False,False)
window.configure(background="grey")
window.iconbitmap("image12.jpeg")

#creation of name
name=Label(window,text="BLUE LIGHT WAVES", font='times 30 bold ',background="grey")
name.place(x=115,y=10)

#creation of the main frame
mainframe=Frame(window, bg="blue",width=550 , height=476)
mainframe.place(x=39,y=60)

#creation of the form

#getting the BLW LOGO image inside the window

image = ImageTk.PhotoImage(Image.open("bLWLOGONEW.jpg"))

pic1=Label(mainframe, image=image, width=240, height=122)
pic1.place(x=0,y=350)

#creation of the heading

heading=Label(mainframe,  text="REGISTRATION  FORM",font='times 23 bold',background="blue")
heading.place(x=105,y=10)

#first name entry 

fname=Label(mainframe, text="First Name :", font='Helvetica 18 bold',background="blue" )
fname.place(x=100,y=65)

fname_entry=Entry(mainframe, font='Helvetica 18 bold' )
fname_entry.place(x=250,y=65)

#last name entry

lname=Label(mainframe, text="Last Name :", font='Helvetica 18 bold',background="blue")
lname.place(x=100,y=120)

lname_entry=Entry(mainframe, font='Helvetica 18 bold' )
lname_entry.place(x=250,y=125)

#gender entry

gender=Label(mainframe,  text="     Gender :", font='Helvetica 18 bold',background="blue")
gender.place(x=100,y=178)

gender_entry=Entry(mainframe, font='Helvetica 18 bold' )
gender_entry.place(x=250,y=180)

#age entry

age=Label(mainframe,  text="Age :", font='Helvetica 18 bold',background="blue" )
age.place(x=172,y=237)

age_entry=Entry(mainframe, font='Helvetica 18 bold' )
age_entry.place(x=250,y=240)

#new password entry

password=Label(mainframe, text=" Password :", font='Helvetica 18 bold',background="blue")
password.place(x=100,y=300)

password_entry=Entry(mainframe, font='Helvetica 18 bold')
password_entry.place(x=250,y=302)

#submit button

submit=Button(mainframe, text='SUBMIT', font='Helvetica 18 bold' ,bg="lightblue", command=test)
submit.place(x=398,y=350)

window.mainloop()


# TEST SUBMIT FUNCTION

'''
def submit(fn,ln,gn,ag,pas): 
    firstnamev=fn
    lastnamev=ln
    genderv=gn
    agev=ag
    passwordv=pas

    with open('database.txt','w') as file:
        text=file.write("Firstname:["+firstnamev+"]  Lastname:["+lastnamev+"]  Gender:["+genderv+"]  Age:["+str(agev)+"]  Password:["+str(passwordv)+"]")

'''
#GET IMAGE INTO TKINTER
'''
from tkinter import *
from PIL import ImageTk, Image

window=Tk()
window.geometry('500x500')
window.resizable(False,False)

image = ImageTk.PhotoImage(Image.open("bLWLOGO.jpg"))

pic1=Label(window, image=image, width=300, height=300)
pic1.place(x=100,y=50)
'''
