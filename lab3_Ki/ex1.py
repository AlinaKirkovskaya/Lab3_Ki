from datetime import date

class Person:
    def __init__(self, surname, first_name, nickname=None, birth_date=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        if birth_date:
            year, month, day = map(int, birth_date.split('-'))
            self.birth_date = date(year, month, day)
        else:
            self.birth_date = None

    def get_age(self):
        if self.birth_date:
            today = date.today()
            age_in_years = today.year - self.birth_date.year
            if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
                age_in_years -= 1
            return str(age_in_years)
        else:
            return "Дата народження не вказана"

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"

person1 = Person("Іванов", "Іван", "Вано", "1990-05-15")
print("Прізвище та ім'я:", person1.get_fullname())
print("Вік:", person1.get_age())

person2 = Person("Петренко", "Петро", birth_date="1985-12-31")
print("\nПрізвище та ім'я:", person2.get_fullname())
print("Вік:", person2.get_age())

person3 = Person("Сидоренко", "Сидір")
print("\nПрізвище та ім'я:", person3.get_fullname())
print("Вік:", person3.get_age())