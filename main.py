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


corokin = Student("Сорокин Д.М.", "м", "17", "89379849855", "corolin34@mail.ru", "2")
doroshenova = Student("Дорошенова М.Л.", "ж", "16", "89279822855", "sorosh788@mail.ru", "3")
print(corokin < doroshenova)
print(corokin == doroshenova)
print(corokin >= doroshenova)
