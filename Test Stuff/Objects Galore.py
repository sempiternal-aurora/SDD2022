class student_record():
    def __init__(self, lN, fN, dob1, yr):
        print("Making new student:", fN, lN)
        self.lastName = lN
        self.firstName = yN
        self.dob = dob1
        self.year = yr
        self.grades = []

    def __str__(self):
        output_string = self.firstName + " " + self.lastName + " " + self.dob + " " + self.year + " " + self.grades
        return output_string
    
    def view_record(self):
        return self.lastName, self.firstName, self.dob, self.year, self.grades

    def print_record(self):
        print("Name:", self.firstName, self.lastName)
        print("Date of Birth:", self.dob)
        print("Year Group:", self.year)
        print("Grades:", self.grades)

    def set_grade(self, grade):
        self.grades.append(grade)

def make_class_set():
    number_of_students = int(input("How many students: "))