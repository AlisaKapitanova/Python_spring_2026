# Christina review 8
# Task 1
# Создайте класс Person с атрибутами name и age и методом introduce(),
# который выводит: Привет, меня зовут <name>, мне <age> лет.
# Создайте класс-наследник Student, который добавляет атрибут school
# и переопределяет метод introduce(), чтобы добавить информацию о школе.
# Пример: Привет, меня зовут Аня, мне 15 лет, я учусь в школе №123.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")
#
#
# class Student(Person):
#     def __init__(self, name, age, school):
#         super().__init__(name, age)
#         self.school = school
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я учусь в школе {self.school}.")
#
#
# student = Student("Аня", 15, "№123")
#
# student.introduce()

# Task 2
# Создайте класс Person с приватным атрибутом _age.
# Сделайте геттер и сеттер для age: если в age присваивают число < 0, автоматически ставьте 0;
# если > 120, автоматически поставьте 120.

class Person:
    def __init__(self, age):
        self._age = age

    # getter
    @property
    def age(self):
        return self._age

    # setter
    @age.setter
    def set_age(self, new_age):
        if new_age < 0:
            self._age = 0
        elif new_age > 120:
            self._age = 120
        else:
            self._age = new_age


p = Person(25)
print(f"Начальный возраст: {p.age}")

p.set_age = -10
print(f"После -10: {p.age}")  # Выведет 0

p.set_age = 200
print(f"После 200: {p.age}")  # Выведет 120




