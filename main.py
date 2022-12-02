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


corokin = Student("Сорокин Д.М.", "м", "17", "89379849855", "corolin34@mail.ru", "3")
print(corokin)
