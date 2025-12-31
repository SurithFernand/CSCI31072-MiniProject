# Validate student ID format
def validate_student_id(student_id):
    assert (student_id.startswith("CS/") 
    and student_id[3:7].isdigit() and student_id[3:7].startswith('20')
    and student_id[7] == '/' 
    and student_id[8:11].isdigit()), "Invalid student ID format."


# Custom exception for invalid marks
class InvalidMarksError(Exception):
    pass

# Validate marks
def validate_student_marks(marks):
    for mark in marks:
        if mark<0 or mark>100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
        

#


