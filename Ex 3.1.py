#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
except:
    print('Invalid hrs')
    h=0
try:
    r = float(rate)
except:
    print('Invalid rate')
    r=0
if h<=40:
    pay = h*r
    
elif h>40:
    bal=h-40
    pay1=40*r
    pay2=bal*1.5*r
    pay=pay1+pay2
print(pay)
