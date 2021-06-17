 #importing library
from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Form")
#Declaring Window size
window.geometry('500x400')
#Declaring Window Color
window.configure(background = "orange");
#below four fields are declared
Firstname = Label(window ,text = "First Name",width = 20).grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name",width = 20).grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id",width = 20).grid(row = 2,column = 0)
Mobile = Label(window ,text = "Contact Number",width = 20).grid(row = 3,column = 0)
SchoolName = Label(window,text = "School Name",width = 20).grid(row = 4,column = 0)
CollegeName = Label(window,text = "College Name",width = 20).grid(row = 5,column = 0)
Pincode= Label(window,text = "Pincode",width = 20).grid(row = 6,column = 0)
selectstate= Label(window,text = "select state",width = 20).grid(row = 7,column = 0)

Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)
SchoolName = Entry(window).grid(row = 4,column = 1)
CollegeName = Entry(window).grid(row = 5,column = 1)
Pincode = Entry(window).grid(row = 6,column = 1)
StateName = Label(window,text="State",width=20).grid(row = 7,column = 0)


#list of states
list_of_states = ['Arunachal Pradesh','Bihar','Chandigarh','Himachal Pradesh','TamilNadu','Kerala','Karnataka','Delhi']

#drop down menu
a = StringVar()
dropdown =OptionMenu(window,a,*list_of_states)
dropdown.config(width=20)
a.set('Select State')
dropdown.grid(row = 7,column = 1)

#using radiobutton
Gender = Label(window,text = "Gender",).grid(row = 8,column = 0)

b = IntVar()
Radiobutton(window,text = "Male",padx = 25,variable = b,value = 1).grid(row = 8,column = 1)
Radiobutton(window,text = "Female",padx = 25,variable = b,value = 2).grid(row = 8,column = 2)


#fubction declaration
def clicked():
	window = "Welcome to " + txt.get()
label.configure(text= window)
button=Button(window ,text="Submit",width = 15).grid(row=12,column=2)
window.mainloop()
