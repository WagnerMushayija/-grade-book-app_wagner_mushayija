from models import Student, Course
import csv


class GradeBook:
    def __init__(self, csv_file='students.csv'):
        """
        Initialize a new GradeBook object.
        """
        self.csv_file = csv_file
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        """
        Add a new student to the student list.

        :param email: The email of the student.
        :param names: The names of the student.
        """
        new_student = Student(email, names)
        self.student_list.append(new_student)
        print(f"Student {names} added successfully.")
        self.write_student_to_csv(new_student)

    def write_student_to_csv(self, student):
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student.email, student.names, "", student.GPA])

    def add_course(self, name, trimester, credits):
        """
        Add a new course to the course list.

        :param name: The name of the course.
        :param trimester: The trimester in which the course is offered.
        :param credits: The number of credits the course is worth.
        """
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)
        print(f"Course {name} added successfully.")

    def display_courses(self):
        if not self.course_list:
            print("No courses available.")
        else:
            print("\nList of Courses:")
            for course in self.course_list:
                print(f"Course Name: {course.name}, Trimester: {course.trimester}, Credits: {course.credits}")

    def register_student_for_course(self, student_email, course_name, grade):
        """
        Register a student for a course.

        :param student_email: The email of the student.
        :param course_name: The name of the course.
        :param grade: The grade of the student in the course.
        """
        # Find the student by email
        student = next((s for s in self.student_list if s.email == student_email), None)
        if not student:
            print(f"Student with email {student_email} not found.")
            return

        # Find the course by name
        course = next((c for c in self.course_list if c.name == course_name), None)
        if not course:
            print(f"Course with name {course_name} not found.")
            return

        # Register the student for the course with the given grade
        student.register_for_course(course_name, grade)
        print(f"Student {student.names} registered for course {course_name} with grade {grade}.")
        self.update_student_in_csv(student)

    def update_student_in_csv(self, student):
        rows = []
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == student.email:
                    row[2] = ', '.join(
                        course for course_dict in student.courses_registered for course in course_dict.keys())
                    row[3] = student.GPA
                writer.writerow(row)

    def calculate_GPA_for_all_students(self):
        """
            Calculate the GPA for each student in the GradeBook.
        """
        for student in self.student_list:
            student.calculate_GPA()
        print("GPAs calculated for all students.")

    def calculate_ranking(self):
        """
        Calculate and display the ranking of students based on their GPA.
        """
        # Sort the student_list by GPA in descending order
        sorted_students = sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

        # Display the rankings
        print("Student Rankings:")
        for index, student in enumerate(sorted_students, start=1):
            print(f"{index}. {student.email} - GPA: {student.GPA}")

    def search_by_grade(self, min_gpa, max_gpa):
        """
        Search for students whose GPA falls within the specified grade range.

        :param min_gpa: The minimum GPA.
        :param max_gpa: The maximum GPA.
        :return: A list of students whose GPA is within the specified range.
        """
        # Debug: Show all students and their GPAs
        print("All students and their GPAs:")
        for student in self.student_list:
            print(f"Name: {student.names}, GPA: {student.GPA}")

        filtered_students = [
            student for student in self.student_list
            if min_gpa <= student.GPA <= max_gpa
        ]
        return filtered_students

        # Debug: Show filtered students

        print("Filtered students:")
        if filtered_students:
            for student in filtered_students:
                print(f"Name: {student.names}, GPA: {student.GPA}")
        else:
            print("No students found with GPA in the specified range.")

        return filtered_students

    def generate_transcript(self):
        """
        Generate and display the transcript for each student.
        """
        for student in self.student_list:
            print(f"Transcript for {student.names} ({student.email}):")
            for course_dict in student.courses_registered:
                for course, grade in course_dict.items():
                    print(f"  Course: {course}, Grade: {grade}")
            print(f"  GPA: {student.GPA}\n")

    def display_students(self):
        try:
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                students = list(reader)
        except FileNotFoundError:
            print("No students to display.")
            return

        print(f"\n{'Name':<20}{'Email':<30}{'Courses':<40}{'GPA':<5}")
        print("=" * 95)

        for student in students:
            print(f"{student[1]:<20}{student[0]:<30}{student[2]:<40}{student[3]:<5}")
