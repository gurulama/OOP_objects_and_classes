class Student:
    def __init__(self, name, surname):
        """Overloading the __init__ method to define attributes of the Student class
        Contains attributes:
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_ratind = float() 
        
        """
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_ratind = float()

    def __str__(self):
        """Overloading the __str__ method. Implements the definition 
        of the average score and returns the characteristics 
        of an instance of a class of the form:
        print(some_student)
        Имя: Ruoy
        Фамилия: Eman
        Средняя оценка за домашние задания: 9.9
        Курсы в процессе изучения: Python, Git
        Завершенные курсы: Основы программирования 
        
        """
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades [k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
                 f'Завершенные курсы: {finished_courses_string}'
        return result

    def rate_hw(self, lecturer, course, grade):
        """Implements the possibility of grading a lecturer by a student, if this lecturer is lecturing 
        on this course with this student. Accepts the variables rate_hw(self, lecturer, course, grade) as input
        
        """
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __lt__(self, other):
        """Implements a comparison through the operators '<,>' of students among themselves 
        according to the average grade for homework
        
        """
        if not isinstance(other, Student):
            print("Данное сравнение некорректно")
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        """Overloading the _init_ method to define the attributes of the Mentor class
        Contains attributes:
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
        """
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        """Overloading the _init_ method to define the attributes of the Mentor class
        Contains attributes:
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_rating = float()
        self.grades = {}

        """
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        """Returns the characteristics of an instance of a class of the form:
        print(some_reviewer)
        Имя: Some
        Фамилия: Buddy

        """
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades [k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_rating}'
        return result

    def __lt__(self, other):
        """Implements comparison through the operators '<,>' of lecturers among 
        themselves according to the average grade for lectures
    
        """
        if not isinstance(other, Lecturer):
            print("Данное сравнение некорректно")
            return
        return self.average_rating < other.average_rating
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Implements the possibility of grading a student for homework, if this examiner is assigned
        to this student for this course, or returns an error.
        Accepts the variables rate_hw(self, student, course, grade) as input
    
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Implements the definition of the average score and returns the characteristics of an instance 
        of a class of the form:
        print(some_lecturer)
        Имя: Some
        Фамилия: Buddy
        Средняя оценка за лекции: 9.9
    
        """
        result = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return result


# We create lecturers and assign them to the course
best_lecturer_1 = Lecturer("Tony", "Stark")
best_lecturer_1.courses_attached += ["Python"]

best_lecturer_2 = Lecturer("Bruce", "Banner")
best_lecturer_2.courses_attached += ["C++"]

best_lecturer_3 = Lecturer("Stephen", "Strange")
best_lecturer_3.courses_attached += ["Python"]


# We create reviewer and assign them to the course
cool_reviewer_1 = Reviewer("Natasha", "Romanov")
cool_reviewer_1.courses_attached += ["Python"]
cool_reviewer_1.courses_attached += ["C++"]

cool_reviewer_2 = Reviewer("Steve", "Rogers")
cool_reviewer_2.courses_attached += ["Python"]
cool_reviewer_2.courses_attached += ["C++"]


# We create students and define the studied and completed courses for them
student_1 = Student("Peter", "Parker")
student_1.courses_in_progress += ["Python"]
student_1.finished_courses += ["Основы программирования"]

student_2 = Student("Jane", "Foster")
student_2.courses_in_progress += ["C++"]
student_2.finished_courses += ["Основы программирования"]

student_3 = Student("Hank", "Pym")
student_3.courses_in_progress += ["Python"]
student_3.finished_courses += ["Основы программирования"]


# We rate lecturers for lectures
student_1.rate_hw(best_lecturer_1, "Python", 10)
student_1.rate_hw(best_lecturer_1, "Python", 10)
student_1.rate_hw(best_lecturer_1, "Python", 10)

student_1.rate_hw(best_lecturer_2, "Python", 7)
student_1.rate_hw(best_lecturer_2, "Python", 5)
student_1.rate_hw(best_lecturer_2, "Python", 8)

student_1.rate_hw(best_lecturer_1, "Python", 8)
student_1.rate_hw(best_lecturer_1, "Python", 9)
student_1.rate_hw(best_lecturer_1, "Python", 7)

student_2.rate_hw(best_lecturer_2, "C++", 10)
student_2.rate_hw(best_lecturer_2, "C++", 8)
student_2.rate_hw(best_lecturer_2, "C++", 9)

student_3.rate_hw(best_lecturer_3, "Python", 6)
student_3.rate_hw(best_lecturer_3, "Python", 7)
student_3.rate_hw(best_lecturer_3, "Python", 5)


# We give grades to students for their homework
cool_reviewer_1.rate_hw(student_1, "Python", 10)
cool_reviewer_1.rate_hw(student_1, "Python", 9)
cool_reviewer_1.rate_hw(student_1, "Python", 8)

cool_reviewer_2.rate_hw(student_2, "C++", 7)
cool_reviewer_2.rate_hw(student_2, "C++", 9)
cool_reviewer_2.rate_hw(student_2, "C++", 8)

cool_reviewer_2.rate_hw(student_3, "Python", 9)
cool_reviewer_2.rate_hw(student_3, "Python", 8)
cool_reviewer_2.rate_hw(student_3, "Python", 7)
cool_reviewer_2.rate_hw(student_3, "Python", 7)
cool_reviewer_2.rate_hw(student_3, "Python", 8)
cool_reviewer_2.rate_hw(student_3, "Python", 9)


# We display the characteristics of the created and evaluated students in the required form
print(f'Список студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# We display the characteristics of the created and evaluated lecturers in the required form
print(f'Список лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()

# We output the result of comparing students by average grades for homework
print(f'Cравнение студентов по средним оценкам за домашнюие задания: '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# We output the result of comparing lecturers by average grades for lectures
print(f'Сравнение лекторов по средним оценкам за лекции: '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Creating a list of students
student_list = [student_1, student_2, student_3]

# Creating a list of lecturers
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]


# Creating a function to calculate the average grade for homework 
# for all students in a particular course, the list of students 
# and the name of the course are taken as arguments
def student_rating(student_list, course_name):
    """The function for calculating the average grade for homework
    for all students in a particular course
    takes as arguments a list of students and the name of the course

    """
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Creating a function to calculate the average grade for lectures 
# of all lecturers within the course, the list of lecturers and 
# the name of the course are taken as an argument
def lecturer_rating(lecturer_list, course_name):
    """The function for calculating the average grade for the lectures of all lecturers 
    within the course takes as an argument the list of lecturers and the name of the course

    """
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# We output the result of calculating the average grade for all students for this course
print(f"Средняя оценка всех для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

# We output the result of calculating the average grade for all lectures for this course
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")