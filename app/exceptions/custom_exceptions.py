class StudentNotFoundException(Exception):

    def __init__(self):

        self.message = "Student not found"


class CourseNotFoundException(Exception):

    def __init__(self):

        self.message = "Course not found"


class DuplicateStudentException(Exception):

    def __init__(self):

        self.message = "Student with this email already exists"


class DuplicateCourseException(Exception):

    def __init__(self):

        self.message = "Course already exists"