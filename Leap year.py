#A normal year has 365 days but a leap year has 366 days
#the logic behind is:
#A year is a leap year-
#every year is evenly divided by 4
#EXCEPT every year that is evenly divided by 100
#UNLESS every year that is evenly divided by 400
year = int(input("Enter the year you want to check: "))
if (year % 4 == 0):
    if(year % 100 != 0):
        if(year % 400 == 0):
            print(f"{year} is a LEAP year.")
        else:
            print(f"{year} is not a LEAP year.")
    else:
        print(f"{year} is a LEAP year.")
else:
    print(f"{year} is not a LEAP year.")