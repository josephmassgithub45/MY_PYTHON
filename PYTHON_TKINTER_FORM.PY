import tkinter as area
import pyodbc  


man=area.Tk()
man.title('JOSEPH MASSAQUOI')
man.configure(background='lightblue')
man.geometry("680x540")

#FUNCTIONS1111111111111111111FUNCTIONS111111111111111111111FUNCTIONS1111111111111111FUNCTIONS

def output1():
    print('hello good friends')
def output2():
    print('this is programming')
def output3():
    print('thanks for reading this')
def output4():
        firstvalue = firstentry.get()
        secondvalue = secondentry.get()
        thirdvalue = thirdentry.get()
        addressvalue = addressentry.get()
        contactvalue = contactentry.get()
        emailvalue = emailentry.get()
        identryvalue = id_numberentry.get()
        print(firstvalue)
        print(secondvalue)
        print(thirdvalue)
        print(addressvalue)
        print(contactvalue)
        print(emailvalue)
        print(identryvalue)

def dataupdate():
    conn = pyodbc.connect('driver={sql server};'
                           'server=DESKTOP-6TT9F9L;' 
	     		           'database=GPL_DATABASE;'
			               'Trusted_Connection=yes;')

    firstvalue = firstentry.get()
    secondvalue = secondentry.get()
    thirdvalue = thirdentry.get()
    addressvalue = addressentry.get()
    contactvalue = contactentry.get()
    emailvalue = emailentry.get()
    identryvalue = id_numberentry.get()

    process = "execute gpl_update '"+identryvalue+"','"+firstvalue+"','"+secondvalue+"','"+thirdvalue+"','"+addressvalue+"',"+contactvalue+",'"+emailvalue+"'"
    
    cursor=conn.cursor()
    cursor.execute(process)
    conn.commit()

    heading = area.Label(man, text="DATA HAVE BEEN UPDATED SUCCESSFULLY",font='Helvetica 13 bold', background='lightblue')
    heading.pack(side='top')
    heading.place(x=250, y=380)


def datadrop():
    conn = pyodbc.connect('driver={sql server};'
                          'server=DESKTOP-6TT9F9L;' 
	     		          'database=GPL_DATABASE;'
			              'Trusted_Connection=yes;')
    
    identryvalue = id_numberentry.get()

    process = "execute GPL_DROP '"+identryvalue+"'"
    cursor=conn.cursor()
    cursor.execute(process) 
    conn.commit()

    heading = area.Label(man, text="DATA HAVE BEEN DELETED SUCCESSFULLY",font='Helvetica 13 bold', background='lightblue')
    heading.pack(side='top')
    heading.place(x=250, y=380)

def datasubmit():
    conn = pyodbc.connect('driver={sql server};'
                          'server=DESKTOP-6TT9F9L;' 
	     		          'database=GPL_DATABASE;'
			              'Trusted_Connection=yes;')

    firstvalue = firstentry.get()
    secondvalue = secondentry.get()
    thirdvalue = thirdentry.get()
    addressvalue = addressentry.get()
    contactvalue = contactentry.get()
    emailvalue = emailentry.get()
    identryvalue = id_numberentry.get()

    process = "execute GPL_INPUT '"+identryvalue+"','"+firstvalue+"','"+secondvalue+"','"+thirdvalue+"','"+addressvalue+"',"+contactvalue+",'"+emailvalue+"'"
    
    cursor=conn.cursor()
    cursor.execute(process)
    conn.commit()

    heading = area.Label(man, text="DATA HAVE BEEN SUBMITTED SUCCESSFULLY",font='Helvetica 13 bold', background='lightblue')
    heading.pack(side='top')
    heading.place(x=250, y=380)
    
#BUTTONS1111111111111111111111BUTTONS1111111111111111111111111BUTTONS111111111111111111111111111111
redbutton = area.Button(man, background='lightblue',text='UPDATE', command=dataupdate)
redbutton.pack(side='right')
redbutton.place(bordermode='outside' , height=50, width=100, relx=0.2, rely=0.8)

greenbutton = area.Button(man, background='red', text='DELETE', command=datadrop)
greenbutton.pack(side='top')
greenbutton.place(bordermode='outside' , height=50, width=100, x=170, y=490)

bluebutton = area.Button(man, background='lightgreen', text='SUBMIT', command=datasubmit)
bluebutton.pack(side='right')
bluebutton.place(bordermode='outside' , height=50, width=100, x=290, y=490)

#LABEL111111111111111111111LABEL111111111111111111111111LABEL11111111111111111111111111LABEL1111111

heading = area.Label(man, text="GRAND PROGRAMMERS LAND",font='Helvetica 24 bold', background='lightblue')
heading.pack(side='top')
heading.place(x=100, y=20)

id_number = area.Label(man, text='ID_NUMBER',font='Helvetica 18 bold', background='lightblue')
id_number.pack( side='left')
id_number.place(x=45, y=340)

firstname = area.Label(man, text='FIRST NAME',font='Helvetica 18 bold', background='lightblue')
firstname.pack( side='left')
firstname.place(x=40, y=100)

secondname = area.Label(man, text='MIDDLE  NAME',font='Helvetica 18 bold', background='lightblue')
secondname.pack(side='right')
secondname.place(x=247, y=100)

thirdname = area.Label(man, text='LAST NAME',font='Helvetica 18 bold', background='lightblue')
thirdname.pack( side='left')
thirdname.place(x=485, y=100)

address = area.Label(man, text='ADDRESS',font='Helvetica 18 bold', background='lightblue')
address.pack( side='left')
address.place(x=60, y=220)

contact = area.Label(man, text='CONTACT',font='Helvetica 18 bold', background='lightblue')
contact.pack( side='left')
contact.place(x=275, y=220)

email = area.Label(man, text='EMAIL',font='Helvetica 18 bold', background='lightblue')
email.pack( side='left')
email.place(x=515, y=220)

#ENTRIES11111111111111ENTRIES11111111111111111111ENTRIES111111111111111111111ENTRIES11111111111111

id_numberentry = area.Entry(man, bd=7,font='Helvetica 14 bold')
id_numberentry.pack(side='right')
id_numberentry.place(bordermode='outside', height=40, width=180, x=30, y=380 )

firstentry = area.Entry(man, bd=7,font='Helvetica 14 bold')
firstentry.pack(side='right')
firstentry.place(bordermode='outside', height=40, width=180, x=30, y=140 )

secondentry= area.Entry(man, bd=7,font='Helvetica 14 bold')
secondentry.pack(side='right')
secondentry.place(bordermode='outside', height=40, width=180, x=250, y=140)

thirdentry=area.Entry(man, bd=7,font='Helvetica 14 bold')
thirdentry.pack(side='left')
thirdentry.place(bordermode='outside', height=40, width=180, x=470, y=140)

addressentry = area.Entry(man,bd=7, font='Helvetica 14 bold')
addressentry.pack(side='left')
addressentry.place(bordermode='outside', height=40, width=180, x=30, y=260)

contactentry = area.Entry(man, bd=7, font='Helvetica 14 bold')
contactentry.pack(side='left')
contactentry.place(bordermode='outside', height=40, width=180, x=250, y=260)

emailentry = area.Entry(man, bd=7, font='Helvetica 14 bold')
emailentry.pack(side='left')
emailentry.place(bordermode='outside', height=40, width=180, x=470, y=260)


man.mainloop()