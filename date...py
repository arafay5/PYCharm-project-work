date_format=input("Enter the date format dd/mm/yy or mm/dd/yy")
if date_format =='dd/mm/yy':
    for char in range(11):
        date=input("Enter the date: ")
        dd,mm,yy=date.split('/')
        dd=int(dd)
        mm=int(mm)
        yy=int(yy)
        if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            max_days=31
        elif(mm==4 or mm==6 or mm==9 or mm==11):
            max_days=30
        elif(yy%4==0 or yy%400==0):
            max_days=29
        else:
            max_days=28
        if(mm<1 or mm>12):
            print("Date is invalid.")
        elif(dd<1 or dd>max_days):
            print("Date is invalid.")
        else:
            print('Date is valid.')
else:
    for char in range(11):
        date=input("Enter the date: ")
        mm,dd,yy=date.split('/')
        dd=int(dd)
        mm=int(mm)
        yy=int(yy)
        if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            max_days=31
        elif(mm==4 or mm==6 or mm==9 or mm==11):
            max_days=30
        elif(yy%4==0 or yy%400==0):
            max_days=29
        else:
            max_days=28
        if(mm<1 or mm>12):
            print("Date is invalid.")
        elif(dd<1 or dd>max_days):
            print("Date is invalid.")
        else:
            print('Date is valid.')
