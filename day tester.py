from PBirthday import calculate_birthday
from PBirthday import calc_leap_year
import datetime

def test(start, end):
    error = 0
    for year in range(start, end):
        print("Testing:", year)
        for i in range(1, 13):
            if i in {4, 6, 9, 11}:
                if calculate_birthday(1, i, year) != datetime.datetime(year, i, 1).strftime("%A"):
                    print(year, i, 1)
                    error += 1
                if calculate_birthday(30, i, year) != datetime.datetime(year, i, 30).strftime("%A"):
                    print(year, i, 30)
                    error += 1
            elif i == 2:
                if calc_leap_year(year) == True:
                    if calculate_birthday(1, i, year) != datetime.datetime(year, i, 1).strftime("%A"):
                        print(year, i, 1)
                        error += 1
                    if calculate_birthday(29, i, year) != datetime.datetime(year, i, 29).strftime("%A"):
                        print(year, i, 29)
                        error += 1
                else:
                    if calculate_birthday(1, i, year) != datetime.datetime(year, i, 1).strftime("%A"):
                        print(year, i, 1)
                        error += 1
                    if calculate_birthday(28, i, year) != datetime.datetime(year, i, 28).strftime("%A"):
                        print(year, i, 28)
                        error += 1
            else:
                if calculate_birthday(1, i, year) != datetime.datetime(year, i, 1).strftime("%A"):
                    print(year, i, 1)
                    error += 1
                if calculate_birthday(31, i, year) != datetime.datetime(year, i, 31).strftime("%A"):
                    print(year, i, 31)
                    error += 1
    print(error)

if __name__ == "__main__":
    #main()  #calls the main function by default whenever the code is run
    #I'm never not using this, fight me
    #print(calc_first_day_of_month(12, 4, False))
    test(1, 1000)