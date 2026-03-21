# Создайте класс Book с атрибутами title, author, pages.
# Добавьте метод info(), который выводит строку “Книга: …, Автор: …, Страниц: …”
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.autor = author
#         self.pages = pages
#
#     def info(self):
#         print(f"Книга: {self.title} \n"
#               f"Автор: {self.autor}  \n"
#               f"Страниц: {self.pages}")
#
# info_book = Book("War and Peace", "Толстой", "1300")
# info_book.info()

# Task 2 Создайте класс BancAccount с атрибутами owner, balance и методами deposit(amount) - пополнение счёта,
# withdraw(amount) - снятие денег со счёта (не забудьте проверить, что баланс положительный),
# info() - выводит полную информацию об аккаунте.

# class BancAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         if balance > 0:
#             self.balance = balance
#         else:
#             print("Нельзя внести отрицательную сумму!")
#
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Недостаточно средств!")
#
#     def info(self):
#         print(f"У {self.owner} на счету {self.balance} денег")
#
# info_account = BancAccount("Owner Account", 10000)
# info_account.deposit(5000)
# info_account.info()
#
# info_account.withdraw(4500)
# info_account.info()
#
# info_account.withdraw(160000)
# info_account.info()


# Создайте класс Student с атрибутами name, grades (список с оценками).
# Создайте 2 метода: add_grade(grade) - добавить оценку, average() - возвращает средний балл.
# class Student:
#     def __init__(self, name, grades):
#         if all(type(x) == int for x in grades):
#             self.name = name
#             self.grades = grades
#         else:
#             print("Некорректный тип данных!")
#
#     def add_grade(self,grade):
#         if type(grade) == int:
#             self.grades.append(grade)
#         else:
#             print("Некорректный тип данных!")
#
#     def average_grade(self):
#         return sum(self.grades)/len(self.grades)
#
# student1 = Student("John Smith", [1, 2, 3, 4, 5])
# student1.add_grade(5)
# print(student1.grades)
# print(student1.average_grade())

# Создайте класс Calculator с атрибутом value (по умолчанию 0). Создайте методы add(x) - прибавить число, sub(x) - вычесть число,
# mul(x) - умножить на число, div(x) - разделить на число (с проверкой на 0) и show() - выводит текущее значение.

class Calculator:
    def __init__(self, value = 0):
        self.value = value

    def add(self, x):
        self.value += x

    def sub(self, x):
        self.value -= x

    def mul(self, x):
        self.value *= x

    def div(self, x):
        if(x == 0):
            print("На 0 делить нельзя")
        else:
            self.value /= x

    def show(self):
        print(self.value)

a = Calculator(10)
a.add(5)
a.show()
a.mul(2)
a.show()
a.div(9)
a.show()
a.sub(6)
a.show()

