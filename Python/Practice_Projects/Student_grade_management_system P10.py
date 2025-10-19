# Student Grade Management System Project With Learning the Concept of Dictionary 

# initilizing the empty dic coz user dalega values 
student_grade = { }

# Adding new Students

def add_student(name,grade):
    student_grade[name] = grade
    print(f"Student {name} Info is Added with Grade 😉: {grade}")

def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        #ager name student_gerade me hai toh key dia toh uski value shwo krdo 
        print(f"{name} with marks are updated 😏{grade}")
    else:
        print(f"{name} Student is not found!! 🫥 ")

# delete student
def delete_student(name,grade):
    if name in student_grade:
        del student_grade[name] 
        print(f"{name} is deleted successfully 🫡")
    else:
        print(f"{name} is not found, check once again! ☺️")

# view all students

def view_all_student():
    if student_grade:
        for name, grade in student_grade.items():
         print(f"{name} : {grade}")
    else:
         print("Student not found/added !")
# now the main program or taking input from user
def main():
    while True:
        print("\n----- STUDENT GRADE MANAGEMENT SYSTEM -----")
        print = input("1. Add Student")     
        print = input("2. Update Student")     
        print = input("3. Delete Student")     
        print = input("4. View Student")     
        print = input("5. Exit")     

        choice = int(input("Enter Your Choice"))
        if choice == 1:
           name = input("Enter Student Name 🧑‍🎓= ")
           grade = int(input("Enter Student Grade 🔢= "))
           add_student(name, grade)
            # student function ko call kia hai and passed 2 arguments 
        
        elif choice == 2:
            name = input("Enter Student Name 🧑‍🎓 =")    
            grade = int(input("Enter Student Grade 🔢= "))
            update_student(name,grade)

        elif choice == 3:
            name = input("Enter Student Name 🧑‍🎓 =")   
            delete_student(name)

        elif choice == 4:
            view_all_student()
            
        elif choice == 5:
            print("Closing the Program.... 👋")
            break
        
        else:
            print("Invalid Choice, Please select form 1-5 🐱")

    main()
