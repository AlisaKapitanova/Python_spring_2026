# Создайте класс Book с атрибутами title, author, pages.
# Добавьте метод info(), который выводит строку “Книга: …, Автор: …, Страниц: …”
#
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.autor = author
        self.pages = pages

    def info(self):
        print(f"Книга: {self.title} \n"
              f"Автор: {self.autor}  \n"
              f"Страниц: {self.pages}")

info_book = Book("War and Peace", "Толстой", "1300")
info_book.info()

