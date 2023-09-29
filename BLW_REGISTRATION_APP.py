from tkinter import *

class BLUE_LIGHT_WAVES_FORM1:

    
    def __init__(self,firstname,lastname,email,contact,gender,country,password):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.contact=contact
        self.gender=gender
        self.country=country
        self.password=password


      
homewindow=Tk()
homewindow.title('BLUE LIGHT WAVES')
homewindow.configure(background='grey')
homewindow.geometry("620x620")



#FRAME1---------------------------------

frame1=Frame(homewindow,background='grey',height=100, width=200,bd=10)
frame1.grid(row=2,column=1)
#TOP SPACE----------------------------------------

TOPLABEL=Label(homewindow,text='BLUE LIGHT WAVES',font='Helvetica 18 bold',background='grey',fg='lightblue')
TOPLABEL.grid(row=0,column=1,columnspan=2,rowspan=1)

TOPLABEL1=Label(homewindow,text='REGISTRATION  FORM',font='Helvetica 18 bold',background='grey',fg='white')
TOPLABEL1.grid(row=1,column=1,columnspan=2,rowspan=1)
#FIRSTNAME------------------------------------------

fname=Label(frame1,text='          Enter First Name    :      ',background='grey',font='Helvetica 15 bold')
fname.grid(row=2,column=0)

fname_entry=Entry(frame1,font='Helvetica 15 bold',relief=RAISED)
fname_entry.grid(row=2,column=1,padx=10)

#SPACE-----------------------------------------

space=Label(frame1,background='grey',font='Helvetica 15 bold')
space.grid(row=3,column=0)

#LASTNAME-----------------------------------------

lname=Label(frame1,text='          Enter Last Name    :      ',background='grey',font='Helvetica 15 bold')
lname.grid(row=4,column=0)

lname_entry=Entry(frame1,font='Helvetica 15 bold',relief=RAISED)
lname_entry.grid(row=4,column=1,padx=10)

#SPACE------------------------------------------

space=Label(frame1,background='grey',font='Helvetica 15 bold')
space.grid(row=5,column=0)

#EMAIL------------------------------------------

lemail=Label(frame1,text='     Enter Email Address    :      ',background='grey',font='Helvetica 15 bold')
lemail.grid(row=6,column=0)

lemail_entry=Entry(frame1,font='Helvetica 15 bold',relief=RAISED)
lemail_entry.grid(row=6,column=1,padx=10)

#SPACE--------------------------------------------

space=Label(frame1,background='grey',font='Helvetica 15 bold')
space.grid(row=7,column=0)
#GENDER--------------------------------------------


lgender=Label(frame1,text='              Select Gender    :      ',background='grey',font='Helvetica 15 bold')
lgender.grid(row=8,column=0)

male=IntVar()
female=IntVar()

checkmale=Checkbutton(frame1,text="Male",variable=male,onvalue=1,offvalue=0,height=2,width=5)
checkmale.grid(row=8,column=1,columnspan=2)

checkfemale=Checkbutton(frame1,text="Female",variable=female,onvalue=1,offvalue=0,height=2,width=5)
checkfemale.grid(row=8,column=2)

#SPACE-----------------------------------------------

space=Label(frame1,background='grey',font='Helvetica 15 bold')
space.grid(row=9,column=0)

#LCOUNTRY---------------------------------------------

lcountry=Label(frame1,text='             Select Country    :      ',background='grey',font='Helvetica 15 bold')
lcountry.grid(row=10,column=0)

lcountry=Menubutton(frame1,text='Select',bd=7,font='Helvetica 15 bold',relief=RAISED,width=14,activeforeground="grey",activebackground='lightblue')
lcountry.grid(row=10,column=1)
lcountry.menu=Menu(lcountry,tearoff=0)
lcountry['menu']=lcountry.menu

lcountry.menu.add_checkbutton(label='SIERRA LEONE')
lcountry.menu.add_checkbutton(label='FANCE')
lcountry.menu.add_checkbutton(label='FRANCE')
lcountry.menu.add_checkbutton(label='USA')
lcountry.menu.add_checkbutton(label='ENGLAND')
lcountry.menu.add_checkbutton(label='GAMBIA')

lcountry.grid(row=10,column=1)

#SPACE-------------------------------------------------
space=Label(frame1,background='grey',font='Helvetica 15 bold')
space.grid(row=11,column=0)

#PASSWORD----------------------------------------------

lpassword=Label(frame1,text='            Enter Password    :      ',background='grey',font='Helvetica 15 bold')
lpassword.grid(row=12,column=0)

lpassword_entry=Entry(frame1,font='Helvetica 15 bold',relief=RAISED)
lpassword_entry.grid(row=12,column=1,padx=10)

#SPACE-------------------------------------------------
space=Label(frame1,background='grey',font='Helvetica 15 bold')
space.grid(row=13,column=0)

#RE-ENTER-PASSWORD-------------------------------------

lrpassword=Label(frame1,text='      Re-Enter Password    :      ',background='grey',font='Helvetica 15 bold')
lrpassword.grid(row=14,column=0)

lrpassword_entry=Entry(frame1,font='Helvetica 15 bold',relief=RAISED)
lrpassword_entry.grid(row=14,column=1,padx=10)

#SPACE-------------------------------------------------
space=Label(frame1,background='grey',font='Helvetica 15 bold')
space.grid(row=15,column=0)


#SUBMIT------------------------------------------------

lsubmit=Button(frame1,text='Register',bd=7,width=14,font='Helvetica 15 bold',activeforeground="grey",activebackground='lightblue')
lsubmit.grid(row=16,column=1)
'''
#LISTBOX--------------------------------

country=Listbox(frame1)
country.insert(1,'SIERRA  LEONE')
country.insert(2,'FRANCE')
country.insert(3,'ENGLAND')
country.insert(4,'USA')
country.insert(5,'GAMBIA')
country.insert(6,'CANADA')
country.grid(row=11,column=1)
'''
homewindow.mainloop()

