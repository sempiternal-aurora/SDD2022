def extract_date(date):
    day = date[0:2]
    month = date[3:5]
    year = date[6:]
    print(day, month, year)
    return day, month, year

if __name__ == "__main__":
    extract_date("17/03/2004")