class Student:
    def __init__(self, name, grade, age, school):
        self.name = name
        self.grade = grade
        self.age = age
        self.school = school
    def __str__(self):
        return f"Student name: {self.name}\n Grade: {self.grade}\n Age: {self.age}\n School: {self.school}\n"
    def save_student(self):
        file = open("students.txt", "a")
        file.write(f"{self.name} {self.grade} {self.age}\n")
        file.close()
        
class Teacher:
    def __init__(self, name, age, subject, school):
        self.name = name
        self.age = age
        self.subject = subject
        self.school = school
    def __str__(self):
        return f"Teacher name: {self.name}\n Age: {self.grade}\n Subject: {self.subject}\n School: {self.school}\n"
    def save_teacher(self):
        file = open("teachers.txt", "a")
        file.write(f"{self.name} {self.grade} {self.age}\n")
        file.close()

def sign_up_verification():
    password_verify = input("Please type in your password again.")
    if password_verify == password:
         return "Password verified."
    elif password_verify != password:
        return "Password unverified."
    
def login():
    print("You will now login.")
    username = input("Please enter your username.")
    password_input = input("Please type in your password.")
    if username != y:
         return "Login unsuccessful."
    elif password_input != password:
        return "Login unsuccessful."
    else:
        return "Login successful."
        
def students():
    firstname = input(str("What is your first name?"))
    lastname = input(str("What is your last name?"))
    age = input("How old are you?")
    grade = input("What grade are you in?")
    school = input("What is your school?")
    studentID = ""
    for i in range(6):
        import random
        studentID += str(random.randint(0,10))
    student_username = firstname + lastname[0] + lastname[-1] + studentID
    print("Here is your information.")
    print("name:" + firstname + lastname)
    print("age:" + age)
    print("grade:" + grade)
    print("school:" + school)
    print(studentID)
    print(student_username)
    print("Computer science, biology, chemistry, microbiology, human biology, physics")
    student_class_choice = input("Please choose the science class you are currently taking from the list provided.")

def teachers():
    firstname = input(str("What is your first name?"))
    lastname = input(str("What is your last name?"))
    age = input("How old are you?")
    subject = input("What subject do you teach?")
    school = input("Where do you work?")
    teacherID = ""
    for i in range(6):
        import random
        teacherID += str(random.randint(0,10))
    teacher_username = firstname[0] + lastname + teacherID
    print("Here is your information.")
    print("name:" + firstname + lastname)
    print("age:" + age)
    print("subject:" + subject)
    print("school:" + school)
    print("teacherID:" + teacherID)
    print("username:" + teacher_username)
    courses_taught()

def courses_taught():
    teacher_courses = input("What classes do you teach?")
    x = teacher_courses.split(", ")
    print(x)

y = input("Please type in your full name. This will be your username.")
password = input("Please create a password.")
sign_up = sign_up_verification()

if sign_up_verification() == "Password verified.":
    login_status = False
    trial_count = 3
    while login_status == False and trial_count >0:
        login_answer = login()
        if login_answer == "Login successful.":
            login_status = True
        else:
            trial_count -= 1
    if login_status == False:
        print("You dumb and can’t login.")
    else:
        account_type_politely_asking = input("Are you a Student or a Teacher?")
        if ("student" in account_type_politely_asking) or ("Student" in account_type_politely_asking):
            students()
        if ("teacher" in account_type_politely_asking) or ("Teacher" in account_type_politely_asking):
            teachers()
        else:
            print("Yes, this one, officer. This is the person signing into a school account who ain’t a student or working here.")