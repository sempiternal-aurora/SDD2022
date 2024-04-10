import datetime

def validate_date(dob):
    #Verifies that the date is a valid date
    if len(dob) == 10: #Checks to see if it is only as long as it is supposed to be
        if dob[0:2].isnumeric() and dob[3:5].isnumeric and dob[6:].isnumeric(): #Checks to see that the day month and year are valid integers
            if 0 < int(dob[6:]) < 10000: #Checks to see if the day is less then or equal to 31
                if 0 < int(dob[3:5]) <= 12: #Makes sure the month is a valid month
                    if int(dob[3:5]) in {4, 6, 9, 11}: #checks to see if the number of days is okay for the 30 day months
                        if 0 < int(dob[0:2]) <= 30: 
                            return True
                        else:
                            return False
                    elif int(dob[3:5]) == 2: #checks number of days for februrary
                        if calc_leap_year(int(dob[6:])) == True: #Leap year
                            if 0 < int(dob[0:2]) <= 29:
                                return True
                            else:
                                return False
                        else:
                            if 0 < int(dob[0:2]) <= 28: #Common year
                                return True
                            else:
                                return False
                    else:
                        if 0 < int(dob[0:2]) <= 31: #Other months with 31 days, checks to see if it's less then 31
                            return True
                        else:
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
    day = int(dob[0:2]) #Takes the day out
    month = int(dob[3:5]) #Takes the months out
    year = int(dob[6:]) #Takes the year out
    return day, month, year

def user_input():
    #Asks the user oh so kindly for their name and date of birth. Making sure that it is infact a valid date of birth before parsing it
    name = input("What is your name? ") #asks the user for their name
    dob = input(f"When were you born, {name} (dd/mm/yyyy)? ") #Asks for their date of birth
    is_valid_date = validate_date(dob) #Checks to see if it is a valid date
    while is_valid_date == False: #Asks the user again slightly less kindly to please enter a valid date of birth until it is valid
        dob = input(f"That is not a valid date, please enter your date of birth, {name} (dd/mm/yyyy). ")
        is_valid_date = validate_date(dob) 
    day, month, year = date_parser(dob) #parses the date into day, month and year as seperate integers
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
        return True #Exceptions again, turns out if it's divisible by 400, it is actually a leap year

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
        first_day_of_year = c % 7 #Returns the remainder, or, the day of the week as a numerical value
    return first_day_of_year

def calc_first_day_of_month(month, first_day_of_year, is_leap_year):
    #uses a lot of if and elif statements using the relationships between the first days of the month and the first day of the year to 
    #find the first day of the year
    if is_leap_year == True:    #Taken from the wikipedian list of days of the days that a month starts on, but modified so that january always is at the first of the month
        if month == 1 or month == 4 or month == 7: #For jan, apr and jul, first day is the same
            a = 0
        elif month == 10: #For oct, the first day is one more then jan
            a = 1
        elif month == 5: #for may, the first day is two more then jan
            a = 2
        elif month == 2 or month == 8: #for feb, aug, the first day is 3 more then jan
            a = 3
        elif month == 3 or month == 11: #for mar, nov, the first day is 4 more then jan 
            a = 4
        elif month == 6: #for jun, the first day is 5 more then jan
            a = 5
        elif month == 9 or month == 12: #for sep, dec, the first day is 3 more then jan
            a = 6
    else:   #its different in leap and common years, jan and feb are the same, but the others aren't
        if month == 1 or month == 10: #the first day is the same for jan and oct
            a = 0
        elif month == 5: #for may the first day is 1 more then jan
            a = 1
        elif month == 8: #for aug, the first day is 2 more then jan
            a = 2
        elif month == 2 or month == 3 or month == 11: #for feb, mar, nov the first day is 3 more then jan
            a = 3
        elif month == 6: #for jun, the first day is 4 more then jan
            a = 4
        elif month == 9 or month == 12: #for sep, dec the first day is 5 more then jan
            a = 5
        elif month == 4 or month == 7: #for apr, jul the first day is 6 more then jan
            a = 6
    b = a + first_day_of_year #adds them together to find a number 
    first_day_of_month = b % 7 #takes the remainder of dividing that number by 7 to find the first day of the month
    return first_day_of_month

def calc_day_of_month(day, first_day_of_month):
    b = day + first_day_of_month - 1 #adds the first day of the month to the day of the month and then subtracts 1 because day starts at 0 and day of the month starts at 1
    c = b % 7 #Divides this by 7 and the remainder is the day of the week
    if c == 0: #replaces a integer value for day of the week with an actual string day of the week
        dayob = "Monday" #0 is monday
    elif c == 1: #1 is tuesday
        dayob = "Tuesday"
    elif c == 2: #2 is wednesday
        dayob = "Wednesday"
    elif c == 3: #3 is thursday
        dayob = "Thursday"
    elif c == 4: #4 is friday
        dayob = "Friday"
    elif c == 5: #5 is saturday
        dayob = "Saturday"
    elif c == 6: #6 is sunday
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
    dayob_statement = f"You were born on a {dayob} {name}." #Creates a statement to tell the user what day of the year they were born on
    print(dayob_statement) #Prints said statement

def main():
    day, month, year, name = user_input() #gets the date of birth and name of the user
    dayob = calculate_birthday(day, month, year) #gets what day of the week they were born on
    output(dayob, name) #prints this out to them

if __name__ == "__main__":
    main()  #calls the main function by default whenever the code is run