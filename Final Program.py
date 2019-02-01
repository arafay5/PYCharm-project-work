import tkinter

from tkinter import messagebox

from tkinter import *

import tkcalendar

import datetime

from datetime import date,datetime,time,timedelta

from tkcalendar import Calendar, DateEntry



def flight_reg():

    screen = Tk()

    screen.geometry("500x500")

    screen.title("Airline Reservation System")

    screen.config(bg="gray60")

    title_screen= Label(screen,text="UIT AIRLINES",width=70,height=4,fg="white",bg="blue4",font=("Times 10 bold",16))

    icon = tkinter.PhotoImage(file ="C:/Users/rafay/Desktop/UITlogo.png")

    label = tkinter.Label(title_screen, image=icon)

    label.place(anchor=NW)

    title_screen.pack()

    pass_name= StringVar()

    NIC_no=StringVar()

    Passport_no= StringVar()

    L_name= StringVar()

    name=Label(screen,text="Name: ")

    name.config(bg="gray80")

    name.place(x=30,y=125)

    name_entry=Entry(screen,textvariable=pass_name)

    name_entry.config(bg="gray90")

    name_entry.place(x=30,y=155)

    Last=Label(screen,text="Last Name: ")

    Last.config(bg="gray80")

    Last.place(x=300,y=125)

    Last_entry=Entry(screen,textvariable=L_name)

    Last_entry.config(bg="gray90")

    Last_entry.place(x=300,y=155)

    Nic = Label(screen, text="NIC Number: ")

    Nic.config(bg="gray80")

    Nic.place(x=30, y=190)

    Nic_entry = Entry(screen, textvariable=NIC_no)

    Nic_entry.config(bg="gray90")

    Nic_entry.place(x=30, y=220)

    Passport = Label(screen, text="Passport Number")

    Passport.config(bg="gray80")

    Passport.place(x=300, y=190)

    Passport_entry = Entry(screen, textvariable=Passport_no)

    Passport_entry.config(bg="gray90")

    Passport_entry.place(x=300, y=220)

    calend=Label(screen, text='Choose date')
    calend.config(bg="gray80")

    calend.place(x=30,y=340)

    cal = DateEntry(screen, width=12, bg='blue',

                    fg='gray7', borderwidth=2)
    cal.place(x=30,y=369)


    a=datetime.now() + timedelta(hours=4)

    b=datetime.now() + timedelta(hours=7)
    c = datetime.now() + timedelta(hours=9)
    d=a.strftime("%H:%M %p")

    e=b.strftime("%H:%M %p")
    f = c.strftime("%H:%M %p")

    flight_time=Label(screen,text="Select flight timings")

    flight_time.config(bg="gray80")

    flight_time.place(x=300,y=340)

    timer=StringVar(screen)

    timer.set("-")

    option2=OptionMenu(screen, timer, d, e, f)

    option2.config(bg="gray80")

    option2.place(x=300, y=370)





    destination=Label(screen,text="Destination")

    destination.config(bg="gray80")

    destination.place(x=30,y=260)

    var = StringVar(screen)

    var.set("-")

    option = OptionMenu(screen, var, "Dubai", "Islamabad", "Lahore", "Abu Dhabi")

    option.config(bg="gray80")

    option.place(x=30,y=290)



    class_airline=Label(screen,text="Class Selection")

    class_airline.config(bg="gray80")

    class_airline.place(x=300,y=260)

    var1 = StringVar(screen)

    var1.set("-")

    option1 = OptionMenu(screen, var1, "Economy", "Business")

    option1.config(bg="gray80")

    option1.place(x=300,y=290)


    def output():

        import random

        lst=["A","B","C","D","E","F"]
        lst2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        oscreen = Tk()

        oscreen.geometry("580x270")

        oscreen.title("Airline Ticket")

        title_screen = Label(oscreen, text="UIT AIRLINES", width=60, height=2, fg="white", bg="navy",

                             font=("Times 10 bold", 20))

        icon = tkinter.PhotoImage(file='C:/Users/rafay/Desktop/UITlogo2.png')

        label = tkinter.Label(title_screen, image=icon)

        label.place(anchor=NW)

        title_screen.pack()

        ticket_num=Label(oscreen,text="Ticket No   :   "+(random.choice(lst2))+(random.choice(lst2))+' '+str(random.randint(1,999)), font=16)
        ticket_num.place(x=40,y=110)

        seat=Label(oscreen,text="Seat No         :  "+str(random.randint(0,30))+random.choice(lst), font=16)
        seat.place(x=380,y=110)

        output_name=pass_name.get()

        output_nic=NIC_no.get()

        Last_name=L_name.get()

        output_passport=Passport_no.get()

        output_var=var.get()

        output_var1=var1.get()
        timee= timer.get()
        time_enter=Label(oscreen,text="Time: "+timee, font=16)
        time_enter.place(x=230,y=110)
        departure=Label(oscreen,text="KARACHI >>>>>>>>>>>>>> "+(output_var).upper(),width=60,

                        font=("Times 10 bold",14))

        departure.config(bg="Skyblue",fg="navy")

        departure.pack()

        nme=Label(oscreen, text="First Name :  "+output_name.title(),font=14)
        nme.place(x=40,y=140)

        L_nme = Label(oscreen, text="Last Name  :  " + Last_name.title(),font=14)
        L_nme.place(x=380, y=140)

        cnic=Label(oscreen,text="CNIC            : "+str(output_nic),font=14)
        cnic.place_configure(x=40,y=170)

        passport=Label(oscreen,text="Passport No : "+str(output_passport),font=14)
        passport.place(x=380,y=170)

        '''flight_date=Label(oscreen,text=cal.cget(cal))
        flight_date.config(bg="gray80")
        flight_date.place(x=100,y=80)'''

        eco_buis=Label(oscreen,text="Class           :  "+output_var1.title(),font=14)
        eco_buis.place(x=40,y=200)



        def ticket_price():

            if var1.get() == "Business":
                if var.get() == "Abu Dhabi":
                    price = Label(oscreen, text="TOTAL : 90,000 Rs",font=15)
                    price.place(x=430, y=230)
                elif var.get()=="Dubai":
                    price = Label(oscreen, text="TOTAL : 80,000 Rs",font=15)
                    price.place(x=430, y=230)
                elif var.get()== "Islamabad":
                    price = Label(oscreen, text="TOTAL : 75,000 Rs",font=15)
                    price.place(x=430, y=230)
                elif var.get()=="Lahore":
                    price = Label(oscreen, text="TOTAL : 65,000 Rs",font=15)
                    price.place(x=430, y=230)

            else:

                if var.get() == "Abu Dhabi":
                    price = Label(oscreen, text="TOTAL : 70,000 Rs",font=15)
                    price.place(x=430, y=230)
                elif var.get()=="Dubai":
                    price = Label(oscreen, text="TOTAL : 60,000 Rs",font=15)
                    price.place(x=430, y=230)
                elif var.get()== "Islamabad":
                    price = Label(oscreen, text="TOTAL : 55,000 Rs",font=15)
                    price.place(x=430, y=230)
                elif var.get()=="Lahore":
                    price = Label(oscreen, text="TOTAL : 45,000 Rs",font=15)
                    price.place(x=430, y=230)

        ticket_price()







        oscreen.mainloop()





    def quit():

        if pass_name.get() and var.get() and var1.get() and cal.get_date() and NIC_no.get() and len(NIC_no.get())== 13 and cal.get_date() >= date.today() and timer.get():

            iexit = messagebox.askyesno("Confirm booking", "Are you sure you want to buy this ticket?")

            if iexit > 0:

                screen.destroy()

                output()

        else:

            tkinter.messagebox.showwarning("Error!!","Please fill the form completely.")

    confirm_button=Button(screen,text="Confirm Booking",command=quit)

    confirm_button.config(bg="gray80")

    confirm_button.place(x=400,y=450)



    screen.mainloop()



flight_reg()
