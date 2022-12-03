import numbers as w


def str_to_well(self_well, other_well):
    w1 = self_well()
    w2 = other_well()
    self_well = w.Number()
    other_well = w.Number()
    return self_well, other_well


class Student:
    def __init__(self, fio, pol, age, tel, mail, well, est=False):
        self.fio = fio
        self.pol = pol
        self.age = age
        self.tel = tel
        self.mail = mail
        self.well = well
        self.est = est

    def move_up_a_course(self, summa):
        self.well += summa

    def __str__(self):
        return f"""Студент {self.fio} {self.pol} {self.age} {self.tel} {self.mail} курс: {self.well}, оценки: 
{'имеется' if self.est else 'не имеется'}"""

    def __lt__(self, other):  # <
        return self.well < other.well

    def __eq__(self, other):  # ==
        return self.well == other.well

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True
        if self.__lt__(other):
            return True
        return False

class Groups:
    def __init__(self, title, tel=None, students=None):
        self.title = title
        if students is None:
            students = list()
        self.students = students
        self.tel = tel

    def append(self, std):
        self.students.append(std)

    def __str__(self):
        return f"Группы: {self.title}, телефон: {self.tel}, кол-во студентов: {len(self.students)}"
    def print_employess(self):
        for std in self.students:
            print(std)
    def print_students_est(self, est=True):
        for std in self.students:
            if std.est == est:
                print(std)

corokin = Student("Сорокин Д.М.", "м", "17", "89379849855", "corolin34@mail.ru", "2")
doroshenova = Student("Дорошенова М.Л.", "ж", "16", "89279822855", "sorosh788@mail.ru", "3", True)
print(corokin < doroshenova)
print(corokin == doroshenova)
print(corokin >= doroshenova)

arhiv = Groups("Архив", students=[corokin])
arhiv.append(doroshenova)
arhiv.print_students_est(False)
