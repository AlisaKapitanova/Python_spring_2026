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

class BancAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        if balance > 0:
            self.balance = balance
        else:
            print("Нельзя внести отрицательную сумму!")


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств!")

    def info(self):
        print(f"У {self.owner} на счету {self.balance} денег")

info_account = BancAccount("Owner Account", 10000)
info_account.deposit(5000)
info_account.info()

info_account.withdraw(4500)
info_account.info()

info_account.withdraw(160000)
info_account.info()


# Создайте класс Student с атрибутами name, grades (список с оценками).
# Создайте 2 метода: add_grade(grade) - добавить оценку, average() - возвращает средний балл.
class Student:
    def __init__(self, name, grades):
        if all(type(x) == int for x in grades):
            self.name = name
            self.grades = grades
        else:
            print("Некорректный тип данных!")

    def add_grade(self,grade):
        if type(grade) == int:
            self.grades.append(grade)
        else:
            print("Некорректный тип данных!")

    def average_grade(self):
        return sum(self.grades)/len(self.grades)

student1 = Student("John Smith", [1, 2, 3, 4, 5])
student1.add_grade(5)
print(student1.grades)
print(student1.average_grade())


