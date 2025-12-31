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

    
# Search student records by ID
def search_student_by_id():
    try:
        # Check the provided student ID format
        studentID = input("Enter student ID to search: ").strip()
        validate_student_id(studentID)

        # Search for the student record and display it
        with open(FILE_NAME, "r") as file:
            found = False
            for line in file:
                if line.startswith(studentID + ","):
                    sid, name, math, science, english, avg, grade = line.strip().split(", ")
                    print(f"ID: {sid}, \nName: {name}, \nMath: {math}, Science: {science}, English: {english}, \nAverage: {avg}, \nGrade: {grade}")
                    found = True
                    break
            
            if not found:
                print("Student ID not found.")

    except AssertionError as e:
        print("Error:", e)
    except FileNotFoundError:
        print("File not found.")
                   

# Class statistics
def class_statistics():
    try:
        all_marks = []

        # Callculate class average using recursive function
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                marks = list(map(int, parts[2:5]))
                all_marks.extend(marks)

        if not all_marks:
            print("No marks available to calculate statistics.")
            return
        
        class_avg = calculate_average_recursive(all_marks, len(all_marks))
        print("--- Class Statistics ---")
        print("Class Average: ", round(class_avg, 2))

        # Finding highest and lowest marks using lambda expressions
        highest_mark = lambda marks: max(marks)
        lowest_mark = lambda marks: min(marks)
        print("Highest Mark: ", highest_mark(all_marks))
        print("Lowest Mark: ", lowest_mark(all_marks))

    except FileNotFoundError:
        print("File not found.")


# Delete student records by ID
def delete_student_by_id():
    found = False
    updated_records = []

    try:
        # Check the provided student ID format
        deleteID = input("Enter student ID of the record to delete: ").strip()
        validate_student_id(deleteID)

        # Read existing records and filter out
        with open(FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(deleteID + ","):
                    updated_records.append(line)
                else:
                    found = True
            
        if not found:
            print("Student ID not found.")
            return
        
        # Write updated records back to the file
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
        print("Student record deleted successfully.")

    except AssertionError as e:
        print("Error:", e)
    except FileNotFoundError:
        print("File not found.")


# Generate summary report
def generate_report():
    try:
        total_students = 0
        total_avg = 0

        with open(FILE_NAME, "r") as file, open("summary_report.txt", "w") as report:
            report.write("Student Summary Report\n")
            report.write("----------------------\n")

            for line in file:
                parts = line.strip().split(", ")
                report.write(f"{parts[0]} - {parts[1]} | Avg: {parts[5]} | Grade: {parts[6]}\n")
                total_students += 1
                total_avg += float(parts[5])

            if total_students > 0:
                report.write("\nClass Average: " + str(round(total_avg / total_students, 2)))

        print("Summary report generated (summary_report.txt)")

    except FileNotFoundError:
        print("File not found")



# Main function (Interf)
def main():
    while True:
        print("---- Student Information & Grades Processing System ----".center(120))
        print("1. Add Student Record")
        print("2. View Student Records")
        print("3. Search Student by ID")
        print("4. Class Statistics")
        print("5. Delete Student by ID")
        print("6. Generate Summary Report")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student_by_id()
        elif choice == '4':
            class_statistics()
        elif choice == '5':
            delete_student_by_id()
        elif choice == '6':
            generate_report()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.") 


# Run the main function
if __name__ == "__main__":
    main()



