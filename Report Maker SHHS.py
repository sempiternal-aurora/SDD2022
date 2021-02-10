def createGrade(marks):
    mark = (sum(marks)/len(marks))
    if mark >= 80 and mark <= 100:
        return "A", mark
    elif mark >= 60 and mark < 80:
        return "B", mark
    elif mark >= 50 and mark < 60:
        return "C", mark
    elif mark >= 0 and mark < 50:
        return "F", mark
    else:
        return "S", mark

def main():
    name = input("Please enter student's full name: ")
    year = input("Please enter student's year group: ")
    marks = []
    count = 1
    input1 = " "
    while input1 != "":
        input1 = input("Please enter student's mark " + str(count) + ": ")
        if input1 != "":
            marks.append(int(input1)) 
        count += 1
    grade, mark = createGrade(marks)
    
    print("\nStudent Name: " + name)
    print("Year Group: " + year)
    print("Grade: " + grade)
    print("Marks:", marks)
    print("Average Mark:", mark)

if __name__ == "__main__":
    main()
