def validate_date(dob):
    #Uses a bunch of if statements to tell if the date is in a valid dd/mm/yyyy format and that the days and months are also valid
    if len(dob) == 10:
        if dob[0:2].isnumeric() and dob[3:5].isnumeric and dob[6:].isnumeric():
            if 0 < int(dob[0:2]) <= 31:
                if 0 < int(dob[3:5]) <= 12:
                    if 0 < int(dob[6:]) < 10000: #I don't know How it will even get to here if it is, infact 10000 or over
                        #this is slightly redundant, but we do need to make sure
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def date_parser(dob):
    #converts the very nice date to a usable day month and year format as integers
    day = int(dob[0:2])
    month = int(dob[3:5])
    year = int(dob[6:])
    return day, month, year

def user_input():
    #Asks the user oh so kindly for their name and date of birth. Making sure that it is infact a valid date of birth before parsing it
    name = input("What is your name? ")
    dob = input(f"When were you born, {name} (dd/mm/yyyy)? ")
    is_valid_date = validate_date(dob)
    while is_valid_date == False: #Asks the user again slightly less kindly to please enter a valid date of birth
        dob = input(f"That is not a valid date, please enter your date of birth, {name} (dd/mm/yyyy). ")
        is_valid_date = validate_date(dob)
    day, month, year = date_parser(dob) #Such a nifty little program to seperate out this nice juicy data
    return day, month, year, name

def calc_leap_year(year):
    #Uses a simple series of deductions to test if a year is a leap year
    if (year % 4) != 0: #if it's not divisible by 4, then its a common year
        return False
    elif (year % 100) != 0: #if its not divisible by 100, then its a leap year
        return True
    elif (year % 400) != 0: #however, if it is also not divisible by 400, then it is actually not a leap year
        return False
    else:
        return True #Exceptions again, turns out if it's divisible by 400, it is actually a leap year. Why?

def calc_first_day_of_year(year):
    #Calculates the first day of the year by finding the difference between 
    #the first day of it and 2001 and then dividing that by 7 and taking the remainder
    if year == 2001:
        first_day_of_year = 0   #We calculate it all from 2001, so, there isn't really anything to do here
    else:
        if year > 2001:
            a = 2001
            b = year
            d = 1   
        else:
            a = year
            b = 2001
            d = -1  #counting backwards when going backwards, so we need this, otherwise, its fine
        c = 0
        for i in range(a, b): #iterates through the years, adding 1 if its a common year, 2 if its a leap year.
            is_leap = calc_leap_year(i)
            if is_leap == True:
                c += 2 * d
            else:
                c += 1 * d
        first_day_of_year = c % 7
    return first_day_of_year

def calc_first_day_of_month(month, first_day_of_year, is_leap_year):
    #uses a lot of if and elif statements using the relationships between the first days of the month and the first day of the year to 
    #find the first day of the year
    if is_leap_year == True:    #Taken from the wikipedian list of days of the days that a month starts on, but modified so that january always is at the first of the month
        if month == 1 or month == 4 or month == 7:
            a = 0
        elif month == 10:
            a = 1
        elif month == 5:
            a = 2
        elif month == 2 or month == 8:
            a = 3
        elif month == 3 or month == 11:
            a = 4
        elif month == 6:
            a = 5
        elif month == 9 or month == 12:
            a = 6
    else:   #its different in leap and common years, jan and feb are the same, but the others aren't
        if month == 1 or month == 10:
            a = 0
        elif month == 5:
            a = 1
        elif month == 8:
            a = 2
        elif month == 2 or month == 3 or month == 11:
            a = 3
        elif month == 6:
            a = 4
        elif month == 9 or month == 12:
            a = 5
        elif month == 4 or month == 7:
            a = 6
    b = a + first_day_of_year
    first_day_of_month = b % 7
    return first_day_of_month

def calc_day_of_month(day, first_day_of_month):
    b = day + first_day_of_month - 1
    c = b % 7
    if c == 0:
        dayob = "Monday"
    elif c == 1:
        dayob = "Tuesday"
    elif c == 2:
        dayob = "Wednesday"
    elif c == 3:
        dayob = "Thursday"
    elif c == 4:
        dayob = "Friday"
    elif c == 5:
        dayob = "Saturday"
    elif c == 6:
        dayob = "Sunday"
    return dayob


def calculate_birthday(day, month, year):
    #really just a function that calls all the more exciting functions, like main, but Mr. Marsh needs this one to test if it works
    #first goes is it a leap year, then what is it's first day, then what is the first day of this specific month
    #Then what the kriff is the day this person was actually born on
    is_leap_year = calc_leap_year(year)
    first_day_of_year = calc_first_day_of_year(year)
    first_day_of_month = calc_first_day_of_month(month, first_day_of_year, is_leap_year)
    dayob = calc_day_of_month(day, first_day_of_month)
    return dayob

def output(dayob, name):
    #Creates a handy statement to tell the user what day they were born on, before printing it to the console
    dayob_statement = f"You were born on a {dayob} {name}." 
    print(dayob_statement)

def main():
    #Just calls the user_input function, then the calculate_birthday function, then the output function, nothing special here
    day, month, year, name = user_input()
    dayob = calculate_birthday(day, month, year)
    output(dayob, name)

if __name__ == "__main__":
    main()  #calls the main function by default whenever the code is run
    #I'm never not using this, fight me
    #print(calc_first_day_of_month(12, 4, False))