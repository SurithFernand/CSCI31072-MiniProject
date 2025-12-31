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
                
        # Append student record to file
        with open(FILE_NAME, "a") as file:
            file.write(f"\n{studentID},{name},{math_marks},{science_marks},{english_marks}")

        print("Student record added successfully.")

    except AssertionError as e:
        print("Error:", e)
    except InvalidMarksError as e:
        print("Error:", e)
    except FileNotFoundError:
        print(f"Error: The file {FILE_NAME} does not exist.")
    except ValueError:
        print("Error: Invalid input. Marks must be integers.")












