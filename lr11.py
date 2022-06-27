from abc import ABC, abstractmethod


# Додайте в код оголошення ще одного класу, який буде базовим або похідним до Вашого класу
# із попередньої лабораторної та продемонструйте  просте наслідування в мові Python:
class City:

    def __init__(self, district=" ", population=0, area=None):
        print("City class ctor")
        self.district = district
        self.population = population
        self.area = area or 0

    def test_base_method(self):
        print("I'm base class method")

    def __str__(self):
        return f'district - {self.district} | population - {self.population} | area - {self.area}'


# Додайте ще один базовий клас, можна без логічного обґрунтування
class Base:
    pass


# Наведіть приклад в коді використання абстрактних класів
class Visitor(ABC):
    def test(self):
        print("test def")

    @abstractmethod
    def road_to_place(self):
        pass


# Використати клас із попередньої лабораторної роботи.
class Place(City, Base, Visitor):

    def __init__(self, name=" ", seats=0, hours=None, district=" ", population=0, area=None):
        print("Place class ctor")
        super(City, self).__init__()
        self.name = name
        self.seats = seats
        self.hours = hours or 0

    # сеттери та геттери
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # властивості з використанням функції property()
    def set_seats(self, value):
        self.seats = value

    def get_seats(self):
        return self.seats

    seats = property(get_seats, set_seats)

    # властивості з використанням декораторів
    @property
    def hours(self):
        return self.hours

    @hours.setter
    def hours(self, hours):
        if hours != '':
            self.hours = hours
        else:
            raise ValueError

    def test_daughter_method(self):
        super().test_base_method()
        print("I'm daughter class method")

    # Перевизначення методу str
    def __str__(self):
        return super().__str__() + f'name - {self.name} | seats - {self.seats} | hours - {self.hours}'

    def road_to_place(self):
        print("route to place")

    def people_per_day(self):
        return self.seats * self.hours


if __name__ == "__main__":
    plc1 = Place()
    plc1.set_name("Bar")
    plc1.seats = 25
    plc1.hours = 8
    print(plc1.get_name(), plc1.seats, plc1.hours)

    city = City()
    city.test_base_method()
    plc1.test_daughter_method()
    plc1.test_base_method()

    plc1.road_to_place()

    list_ = [Place("Club1", 20, 6), Place("Bar1", 40, 12)]
    sum_ = 0
    for item in list_:
        sum_ += item.people_per_day()
    print(sum_)
