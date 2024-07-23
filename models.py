class Course:
    def __init__(self, name, trimester, credits):
        """
        Initialize a new Course object.

        :param name: The name of the course.
        :param trimester: The trimester in which the course is offered.
        :param credits: The number of credits the course is worth.
        """
        self.name = name
        self.trimester = trimester
        self.credits = credits


class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def register_for_course(self, course, grade):
        self.courses_registered.append({course: grade})
        self.calculate_GPA()

    def calculate_GPA(self):
        if not self.courses_registered:
            return self.GPA

        total_gpa = 0.0
        for course_dict in self.courses_registered:
            for grade in course_dict.values():
                gpa = grade * 4 / 100
                total_gpa += gpa
        self.GPA = total_gpa / len(self.courses_registered)
        return self.GPA

