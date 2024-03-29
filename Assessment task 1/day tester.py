from PBirthday import calculate_birthday
from PBirthday import calc_leap_year
import datetime
import time

def test(start, end):
    now = time.time()
    error = 0
    for year in range(start, end):
        for month in range(1, 13):
            if month in {4, 6, 9, 11}:
                for day in range(1, 31):
                    bday1 = calculate_birthday(day, month, year)
                    bday2 = datetime.datetime(year, month, day).strftime("%A")
                    if bday1 != bday2:
                        error += 1
            elif month == 2:
                if calc_leap_year(year) == True:
                    for day in range(1, 30):
                        bday1 = calculate_birthday(day, month, year)
                        bday2 = datetime.datetime(year, month, day).strftime("%A")
                        if bday1 != bday2:
                            error += 1
                else:
                    for day in range(1, 29):
                        bday1 = calculate_birthday(day, month, year)
                        bday2 = datetime.datetime(year, month, day).strftime("%A")
                        if bday1 != bday2:
                            error += 1
            else:
                for day in range(1, 29):
                    bday1 = calculate_birthday(day, month, year)
                    bday2 = datetime.datetime(year, month, day).strftime("%A")
                    if bday1 != bday2:
                        error += 1
                for day in range(1, 29):
                    bday1 = calculate_birthday(day, month, year)
                    bday2 = datetime.datetime(year, month, day).strftime("%A")
                    if bday1 != bday2:
                        error += 1
        if year % 100 == 0:
            print("Testing:", year)
    end_time = time.time()
    run_time = end_time - now
    print(run_time)
    print(error)

if __name__ == "__main__":
    #main()  #calls the main function by default whenever the code is run
    #I'm never not using this, fight me
    #print(calc_first_day_of_month(12, 4, False))
    test(1000, 3001)