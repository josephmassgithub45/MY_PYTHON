from email.headerregistry import MessageIDHeader
from tkinter import *
import pyodbc

JOSEPH MASSAQUOI
window=Tk()
window.geometry('1150x550')
window.title("BLW FIRST-FORM")
window.resizable(False,False)
window.configure(background="lightblue")
window.iconbitmap("")

def clear_text():
    firstname_entry.delete(0, END)
    middlename_entry.delete(0, END)
    lastname_entry.delete(0, END)
    gender_entry.delete(0, END)
    date_of_birth_entry.delete(0, END)
    contact_entry.delete(0, END)
    emailaddress_entry.delete(0, END)
    contactaddress_entry.delete(0, END)

def datasubmit():
    firstnamedata=firstname_entry.get()
    middlenamedata=middlename_entry.get()
    lastnamedata=lastname_entry.get()
    genderdata=gender_entry.get()
    dateofbirthdata=date_of_birth_entry.get()
    contactdata=contact_entry.get()
    emailaddressdata=emailaddress_entry.get()
    contactaddressdata=contactaddress_entry.get()

    conn = pyodbc.connect('driver={sql server};'
                           'server=DESKTOP-6TT9F9L;' 
	     		           'database=FIRSTFORM_DATABASE;'
			               'Trusted_Connection=yes;')
    
    process = "execute firstform_input '"+firstnamedata+"','"+middlenamedata+"','"+lastnamedata+"','"+genderdata+"','"+dateofbirthdata+"',"+contactdata+",'"+emailaddressdata+"','"+contactaddressdata+"'"
    
    firstname_entry.delete(0, END)
    middlename_entry.delete(0, END)
    lastname_entry.delete(0, END)
    gender_entry.delete(0, END)
    date_of_birth_entry.delete(0, END)
    contact_entry.delete(0, END)
    emailaddress_entry.delete(0, END)
    contactaddress_entry.delete(0, END)

    cursor=conn.cursor()
    cursor.execute(process)
    conn.commit()
    

title=Label(window,text='BLUE LIGHT WAVES',font='times 20 bold',bg='lightblue')
title.place(x=420,y=5)

#creation of first frame
frame1=Frame(window, width='200px',height='200px',bg='lightblue')
frame1.place(x=50,y=50)

firstname=Label(frame1,text="        First Name :",font='times 20 bold ',bg='lightblue')
firstname.grid(row=1,column=0)

firstname_entry=Entry(frame1, font='times 17 bold ' )
firstname_entry.grid(row=1,column=1)

middlename=Label(frame1,text="    Middle Name :",font='times 20 bold ',bg='lightblue')
middlename.grid(row=2,column=0)

middlename_entry=Entry(frame1, font='times 17 bold ' )
middlename_entry.grid(row=2,column=1)

lastname=Label(frame1,text="         Last Name :",font='times 20 bold ',bg='lightblue')
lastname.grid(row=3,column=0)

lastname_entry=Entry(frame1, font='times 17 bold ' )
lastname_entry.grid(row=3,column=1)

gender=Label(frame1,text="               Gender :",font='times 20 bold ',bg='lightblue')
gender.grid(row=4,column=0)

gender_entry=Entry(frame1, font='times 17 bold ' )
gender_entry.grid(row=4,column=1)

date_of_birth=Label(frame1,text="    Date Of Birth :",font='times 20 bold ',bg='lightblue')
date_of_birth.grid(row=5,column=0)

date_of_birth_entry=Entry(frame1, font='times 17 bold ' )
date_of_birth_entry.grid(row=5,column=1)

contact=Label(frame1,text="              Contact :",font='times 20 bold ',bg='lightblue')
contact.grid(row=6,column=0)

contact_entry=Entry(frame1, font='times 17 bold ' )
contact_entry.grid(row=6,column=1)

emailaddress=Label(frame1,text="    EmailAddress :",font='times 20 bold ',bg='lightblue')
emailaddress.grid(row=7,column=0)

emailaddress_entry=Entry(frame1, font='times 17 bold ' )
emailaddress_entry.grid(row=7,column=1)

contactaddress=Label(frame1,text="Contact Address :",font='times 20 bold ',bg='lightblue')
contactaddress.grid(row=8,column=0)

contactaddress_entry=Entry(frame1, font='times 17 bold ' )
contactaddress_entry.grid(row=8,column=1)

#creation of exception label and frame

exceptions=Label(window,text="EXCEPTIONS",font='times 30 bold ',bg='lightblue')
exceptions.place(x=165,y=390)

exceptions_frame=Frame(window,height='50px',width='377px',bg='grey', borderwidth='10px')
exceptions_frame.place(x=50,y=450)

#creation of the second frame

frame2=Frame(window,height='250px',width='500', bg='grey')
frame2.place(x=600,y=50)

id_number2=Label(window,text="         ID Number :",font='times 20 bold ',bg='lightblue')
id_number2.place(x=580,y=400)

id_number2_entry=Entry(window, font='times 20 bold ' )
id_number2_entry.place(x=816,y=400)

#creation of buttons

button1=Button(window,text='EXCEPTION',height=2,width=15, font='times 10 bold ',bg='lightblue')
button1.place(x=600,y=475)

button2=Button(window,text='FETCH',height=2,width=15, font='times 10 bold ',bg='lightblue')
button2.place(x=728,y=475)

button3=Button(window,text='REFRESH',height=2,width=15 ,font='times 10 bold ',bg='lightblue',command=clear_text)
button3.place(x=856,y=475)

button4=Button(window,text='SUBMIT',height=2,width=15, font='times 10 bold ',bg='lightblue',command=datasubmit)
button4.place(x=985,y=475)
window.mainloop()
