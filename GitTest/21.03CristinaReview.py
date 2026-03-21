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


