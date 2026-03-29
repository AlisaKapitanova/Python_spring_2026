# Домашнее задание (Занятие 7)
# 1
# Прямоугольник
# Создайте класс Rectangle, который принимает ширину и высоту прямоугольника при создании и должен иметь соответствующие атрибуты width и height (целые числа).
# Создайте метод area(), который возвращает площадь прямоугольника.
# Создайте метод perimeter(), который возвращает периметр прямоугольника.
# Пример:
# rect = Rectangle(2, 4)
# a = rect.area() # Вернул 8
# p = rect.perimeter() # Вернул 12
#
# def        → создаём функцию
# __init__   → конструктор класса
# self       → текущий объект
# width      → параметр
# height     → параметр

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# test = Rectangle(5, 2)
# print(test.area())
# print(test.perimeter())

# 2
# Автомобиль
# Создайте класс Car, который принимает марку автомобиля (make) в виде строки и максимально возможную скорость (max_speed) в виде целого числа при создании. Также при инициализации (в теле __init__) экземпляра Car должен быть автоматически создан атрибут speed, равный 0 (текущая скорость автомобиля). Подсказка: для speed в init можно написать так self.speed = 0
#
# Создайте метод display_speed(), который выводит в консоль текущую скорость автомобиля.
# Создайте метод accelerate(), который увеличивает скорость автомобиля на 10, при этом скорость автомобиля не должна превышать max_speed, если вызывается accelerate() при максимальной скорости, то скорость не должна увеличиваться.
# Создайте метод brake(), который уменьшает скорость автомобиля на 10, при этом скорость автомобиля не может быть меньше 0.
# Если вызывается метод brake() при скорости равной 0, то скорость не должна уменьшаться.
# Пример:
# my_toyota = Car("Toyota", 180)
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.display_speed() # вывел в консоль 30
#
#
# Повторение прошлого материала.
# Ответьте на следующие вопросы:
# Что такое and, or? Приведите пример их использования.
# Что такое цикл? Чем отличается for от while?
# Что такое функция? Зачем она нужна?

# Создайте класс Person с атрибутами name и age и методом introduce(),
# который выводит: Привет, меня зовут <name>, мне <age> лет.
# Создайте класс-наследник Student, который добавляет атрибут school
# и переопределяет метод introduce(), чтобы добавить информацию о школе.
# Пример: Привет, меня зовут Аня, мне 15 лет, я учусь в школе №123.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я учусь в школе {self.school}.")


student = Student("Аня", 15, "№123")

student.introduce()