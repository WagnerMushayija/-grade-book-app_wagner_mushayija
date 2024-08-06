import csv
from gradebk import GradeBook


class Student:
    """
    A class to represent a student.

    Attributes:
    email (str): The student's email address.
    names (str): The student's names.
    courses_registered (list): List of courses the student is registered for.
    GPA (float): The student's GPA.
    """

    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0
        student = next((s for s in self.student_list if s.email == student_email), None)
    def register_for_course(self, course, grade):
        """
        Register the student for a course.

        Args:
        course (Course): The course to register the student for.
        """
        self.courses_registered.append({course: grade})
        self.calculate_GPA()

    def calculate_GPA(self):
        """
        Calculate the GPA of the student based on registered courses.
        For simplicity, we assume each course has a grade attribute.
        """
        if not self.courses_registered:
            return self.GPA

        total_gpa = 0.0
        for course_dict in self.courses_registered:
            for grade in course_dict.values():
                gpa = grade * 4 / 100
                total_gpa += gpa
        self.GPA = total_gpa / len(self.courses_registered)
        return self.GPA


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


def main_menu():
    """
    Display the main menu and prompt the user for an action.
    """
    menu_options = {
        "1": "Add Student",
        "2": "Add Course",
        "3": "Register Student for Course",
        "4": "Calculate GPA for All Students",
        "5": "Calculate Student Ranking",
        "6": "Search Students by GPA Range",
        "7": "Generate Transcripts",
        "8": "Display Students",
        "9": "Display Courses",
        "10": "Exit"
    }

    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "GRADEBOOK MENU")
        print("=" * 50)
        for key, value in menu_options.items():
            print(f"{key}. {value}")
        print("=" * 50)

        choice = input("Please select an option (1-10): ")

        if choice == "1":
            email = input("Enter student's email: ")
            names = input("Enter student's names: ")
            gradebook.add_student(email, names)
        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif choice == "3":
            student_email = input("Enter student's email: ")
            course_name = input("Enter course name: ")
            while True:
                try:
                    grade = int(input("Enter student's grade for the course: "))
                    break
                except ValueError:
                    print("Please enter a valid grade's number.")
            gradebook.register_student_for_course(student_email, course_name, grade)
        elif choice == "4":
            gradebook.calculate_GPA_for_all_students()
        elif choice == "5":
            gradebook.calculate_ranking()
        elif choice == "6":
            min_gpa = float(input("Enter minimum GPA: "))
            max_gpa = float(input("Enter maximum GPA: "))
            filtered_students = gradebook.search_by_grade(min_gpa, max_gpa)
            print("\n Filtered Students:")
            if filtered_students:
                for student in filtered_students:
                    print(f"Name: {student.names}, Email: {student.email}, GPA: {student.GPA}")
            else:
                print("No students found with GPA in the specified range.")
        elif choice == "7":
            gradebook.generate_transcript()
        elif choice == "8":
            gradebook.display_students()
        elif choice == "9":
            gradebook.display_courses()
        elif choice == "10":
            print("Exiting the GradeBook application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Create an instance of GradeBook
gradebook = GradeBook()

# Run the main menu
main_menu()
