class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_ratind = float()

    def __str__(self):
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
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                print(lecturer.grades)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Данное сравнение некорректно")
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades [k])
        #print(grades_count)
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_rating}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Данное сравнение некорректно")
            return
        return self.average_rating < other.average_rating
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return result


# Лекторы и закрепленные за ними курсы
best_lecturer_1 = Lecturer("Tony", "Stark")
best_lecturer_1.courses_attached += ["Python"]

best_lecturer_2 = Lecturer("Bruce", "Banner")
best_lecturer_2.courses_attached += ["C++"]

best_lecturer_3 = Lecturer("Stephen", "Strange")
best_lecturer_3.courses_attached += ["Python"]


# Проверяющие и закрепленные за ними курсы
cool_reviewer_1 = Reviewer("Natasha", "Romanov")
cool_reviewer_1.courses_attached += ["Python"]
cool_reviewer_1.courses_attached += ["C++"]

cool_reviewer_2 = Reviewer("Steve", "Rogers")
cool_reviewer_2.courses_attached += ["Python"]
cool_reviewer_2.courses_attached += ["C++"]


#  Студенты и курсы: в процессе изучения и завершенные
student_1 = Student("Peter", "Parker")
student_1.courses_in_progress += ["Python"]
student_1.finished_courses += ["Основы программирования"]

student_2 = Student("Jane", "Foster")
student_2.courses_in_progress += ["C++"]
student_2.finished_courses += ["Основы программирования"]

student_3 = Student("Hank", "Pym")
student_3.courses_in_progress += ["Python"]
student_3.finished_courses += ["Основы программирования"]


# Оценки лекторам за лекции
student_1.rate_hw(best_lecturer_1, "Python", 10)
student_1.rate_hw(best_lecturer_1, "Python", 10)
student_1.rate_hw(best_lecturer_1, "Python", 10)

student_1.rate_hw(best_lecturer_2, "Python", 6)
student_1.rate_hw(best_lecturer_2, "Python", 9)
student_1.rate_hw(best_lecturer_2, "Python", 7)

student_1.rate_hw(best_lecturer_1, "Python", 5)
student_1.rate_hw(best_lecturer_1, "Python", 9)
student_1.rate_hw(best_lecturer_1, "Python", 6)

student_2.rate_hw(best_lecturer_2, "C++", 10)
student_2.rate_hw(best_lecturer_2, "C++", 6)
student_2.rate_hw(best_lecturer_2, "C++", 8)

student_3.rate_hw(best_lecturer_3, "Python", 4)
student_3.rate_hw(best_lecturer_3, "Python", 9)
student_3.rate_hw(best_lecturer_3, "Python", 6)


#  Оценки студентов за домашние задания
cool_reviewer_1.rate_hw(student_1, "Python", 8)
cool_reviewer_1.rate_hw(student_1, "Python", 6)
cool_reviewer_1.rate_hw(student_1, "Python", 6)

cool_reviewer_2.rate_hw(student_2, "C++", 9)
cool_reviewer_2.rate_hw(student_2, "C++", 10)
cool_reviewer_2.rate_hw(student_2, "C++", 5)

cool_reviewer_2.rate_hw(student_3, "Python", 8)
cool_reviewer_2.rate_hw(student_3, "Python", 5)
cool_reviewer_2.rate_hw(student_3, "Python", 9)
cool_reviewer_2.rate_hw(student_3, "Python", 4)
cool_reviewer_2.rate_hw(student_3, "Python", 6)
cool_reviewer_2.rate_hw(student_3, "Python", 8)


print(student_1)
print()
print(student_3)
print(student_1.name, student_1.surname, student_1.grades, student_1.finished_courses, student_1.courses_in_progress)
print()
print(best_lecturer_1.name, best_lecturer_1.surname, best_lecturer_1.courses_attached, best_lecturer_1.grades)
print()
print(cool_reviewer_1.name, cool_reviewer_1.surname, cool_reviewer_1.courses_attached)
print()
print(best_lecturer_2)
print()
print(cool_reviewer_2)
print()
print(student_1)
print()
print(student_2)
print()
print(student_1 > student_2)
print()
print(best_lecturer_1 > best_lecturer_2)

student_list_1 = [student_1, student_2, student_3]
lecturer_list_1 = [best_lecturer_1, best_lecturer_2, best_lecturer_3]



def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# print(student_rating(student_list_1, "Python"))
print()
print(lecturer_rating(lecturer_list_1, "Python"))
print()
print(best_lecturer_1.average_rating)
print()
print(best_lecturer_1.grades)
print()
print(best_lecturer_2.average_rating)
print()
print(best_lecturer_2.grades)
print()
print(best_lecturer_3.average_rating)
print()
print(best_lecturer_3.grades)