import datetime as dt

x = dt.datetime.now()

print(x)  # Real date and time
print(x.year) # print year
print(x.strftime("%A")) # print day of the week
print(x.strftime("%B")) # print of a full mouth name
print(x.strftime("%b")) # print of a  short mouth name
print(x.strftime("%y")) # print of a short year number
print(x.strftime("%Y")) # print of a full year number
print(x.strftime("%M")) # print a minute 00 - 59
print(x.strftime("%S")) # print a second 00 - 59
print(x.strftime("%j")) # print a 365 day
print(x.strftime("%p")) # print a AM and PM 
print(x.strftime("%I")) # print 00 - 12 hour
print(x.strftime("%H")) # print 00 - 23 hour
print(x.strftime("%f")) # micro second show
print(x.strftime("%d")) # Day of mouth 1 - 31
print(x.strftime("%c")) # print week , Mouth , Date and time
print(x.strftime("%C")) # showing century
print(x.strftime("%u")) # print day of week 1 - 7
print(x.strftime("%V")) # print week number 1 - 53
print(x.strftime("%x")) # print date
print(x.strftime("%X")) # print time
