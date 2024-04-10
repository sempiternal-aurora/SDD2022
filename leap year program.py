def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def leap_year_main():
    start = int(input("Please enter start: "))
    stop = int(input("Please enter stop: "))
    for year in range(start, stop):
        is_leap_year = is_leap(year)
        if is_leap_year:
            print(year)

if __name__ == "__main__":
    leap_year_main()