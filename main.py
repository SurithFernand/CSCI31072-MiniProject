from utils import *

FILE_NAME = "students.txt"

# Add student records
def add_student():
    try:
        studentID = input("Input student's ID (e.g., CS/2021/001): ")
        validate_student_id(studentID)

        name = input("Input student's name: ")

        math_marks = int(input("Input math marks: "))
        science_marks = int(input("Input science marks: "))
        english_marks = int(input("Input english marks: "))
        marks = [math_marks, science_marks, english_marks]
        validate_student_marks(marks)

        # Prevent duplicate student IDs
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(studentID + ","):
                    print("Error: Student ID already exists.")
                    return
                
        # Calculate average and grade
        average = calculate_average(marks)
        average = round(average, 2)
        grade = calculate_grade(average)

        # Append student record to file
        with open(FILE_NAME, "a") as file:
            file.write(f"{studentID}, {name}, {math_marks}, {science_marks}, {english_marks}, {average}, {grade}\n")

        print("Student record added successfully.")

    except AssertionError as e:
        print("Error:", e)
    except InvalidMarksError as e:
        print("Error:", e)
    except FileNotFoundError:
        print(f"Error: The file {FILE_NAME} does not exist.")
    except ValueError:
        print("Error: Invalid input. Marks must be integers.")


# View student records
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n--- Student Records ---")
            for line in file:
                sid, name, math, science, english, avg, grade = line.strip().split(", ")
                print(f"ID: {sid}, Name: {name}, Math: {math}, Science: {science}, English: {english}, Average: {avg}, Grade: {grade}")
    except FileNotFoundError:
        print("No records found.")



            
    





def main():
    while True:
        print("---- Student Information & Grades Processing System ----".center(120))
        print("1. Add Student Record")
        print("2. View Student Records")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.") 



main()



