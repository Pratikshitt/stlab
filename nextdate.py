def check( day, month):
    if((month==4 or month==6 or month==9 or month==11) and day==31):
        return 1
    else:
        return 0
def isleap( year):
    if((year%4==0 and year%100!=0) or year%400==0):
        return 1
    else:
        return 0 
flag='n'        
while(flag=='n'):
    flag='y' 
    print("\nEnter the  date in the form of dd mm yyyy\n")
   
    day=int(input())
    month=int(input())
    year=int(input())
    tom_day=day+1
    tom_month=month
    tom_year= year
    if(day<1 or day>31):
        print("Day is not in the range 1 to 31\n")
        flag='n'
    if(month<1 or month>12):
        print("Month is not in the range 1....12\n")
        flag='n'
    elif(check(day,month)):
        print("Day is not in the range day<=30")
        flag='n'
    if(year<1812 or year>2014):

        print(" Year is not in the range 1812 to 2014\n")
        flag='n'                
    if(month==2):
        if(isleap(year) and day>29):
            print("Wrong  date input for leap year")
            flag='n'
        elif(not(isleap(year)) and day>28):
            print("Wrong date input for not a leap year")
            flag='n'    

if(month==10):
    if(day<31):
        tom_day=day+1
    else:
        tom_day=1
        tom_month=month+1
if(month==11):
    if(day<30):
        tom_day=day+1
    else:
        tom_day=1
        tom_month=month+1
if(month==6):
    if(day<30):
        tom_day=day+1
    else:
        tom_day=1
        tom_month=month+1        

if(month==12):
    if(day<31):
        tom_day=day+1
    else:
        tom_day=1
        tom_month=1
        if(year==2014):
            print("The next day is out of boundary value of year\n")
            tom_year=year+1
        else:
            tom_year=year+1  
if(month==2):
    if(day<28):
        tom_day=day+1
    elif(isleap(year) and day==28):
        tom_day=day+1
    elif(day==28 or day==29):
        tom_day=1
        tom_month=3
print("Next day is : ",tom_day,tom_month,tom_year)                                
