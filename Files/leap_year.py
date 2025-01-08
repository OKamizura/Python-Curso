def is_leap_year(year):
    is_leap = False
    if(year % 4 == 0):
        is_leap = True
        if(year % 100 == 0 and year % 400 != 0):
            is_leap = False
            return False
        else:
            is_leap = True
            return True
            
        
if(is_leap_year(2400)):
    print("True")
else:
    print("False")
