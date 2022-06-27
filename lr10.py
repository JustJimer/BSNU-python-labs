class Place:
    task4 = 'something'

    def __init__(self, name=" ", seats=0, hours=None):
        self.name = name
        self.seats = seats
        self.hours = hours or 0

    @staticmethod
    def static_test():
        print("static method demonstration")

    @classmethod
    def class_test(cls):
        print("class method demonstration")

    def __str__(self):
        return f'name - {self.name} | seats - {self.seats} | hours - {self.hours}'


#Створіть застосунок, який містить оголошення класу із Вашого варіанту(перелік класів в кінці файлу).
#Забезпечте можливість створювати екземпляри класу, використовуючи від 0 до 2 параметрів. Продемонструйте проблему та спосіб її вирішення, якщо аргумент, який має значення за замовчування,  змінного типу.
plc1 = Place()
plc2 = Place("Bar")
plc3 = Place("Club, 20")
plc4 = Place("Bar2", 30, 5.5)

#Додайте тільки до одного із створених об’єктів класу нове поле. Поясніть, як це діє.
plc4.new = 'task3'

#Додайте в клас змінну, член класу (не атрибут). Продемонструйте виведіть на друк значення цього роля. Змініть значення. Знову виведіть на друк.
print(Place.task4)
Place.task4 = 'something new'
print(Place.task4)

# Створіть в класі статичний та класовий методи, які мають сенс, тобто відображають суть їх використання.  Продемонструйте всі можливі виклики цих методів.
Place.static_test()
Place.class_test()
plc2.class_test()
plc2.static_test()

# Виведіть на друк всі члени класу (використати метод, який для цього призначений).
print(dir(plc1))

# Наведіть приклад коду, коли необхідно використовувати метод__new__
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
