class TestCall:
    def __call__(self):
        return "hello world"


def multiply(a):
    def insider(b):
        return a * b
    return insider


def test1():
    print("Test function 1")


def test2():
    print("Test function 2")


def simple_decorator(obj):
    def runner():
        print("run")
        obj()
        print("break")
    return runner


@simple_decorator
def decorator_test():
    print("worlllld HelllOOOOOOOOO")


def method_decorator(fn):
    def wrapper(self):
        print("run method: " + str(fn.__name__))
        fn(self)
    return wrapper


class Position:
    def __init__(self, px=0, py=0):
        self.px = px
        self.py = py

    def norm(self):
        print((self.px ** 2 + self.py ** 2) ** 0.5)


def choose_class(name):
    if name == 'test':
        class Test(object):
            pass
        return Test
    else:
        class Bar(object):
            pass
        return Bar


def __init__(self, name='Steve', age=0):
    self.name = name
    self.age = age


def __str__(self):
    return 'name=' + self.name + ' age=' + str(self.age)


class Meta(type):
    def __new__(mcs, name_class, base_class, attrs):
        attrs.update({'nationality': "british"})
        return type.__new__(mcs, name_class, base_class, attrs)


class Person(metaclass=Meta):
    def show(self):
        print(f'show {self.name}')

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age


if __name__ == "__main__":
    string = TestCall()
    print(f'{string()}')
    x = multiply(2)(3)
    print(f'{x}')
    three_mul = multiply(3)
    x = three_mul(6)
    print(x)
    first_test_wrapped = simple_decorator(test1)
    second_test_wrapped = simple_decorator(test2)
    first_test_wrapped()
    second_test_wrapped()


    @method_decorator
    def norm(self):
        print((self.px ** 2 + self.py ** 2) ** 0.5)


    vector = Position(2, 3)
    vector.norm()
    choose_class1 = choose_class('test')
    print(choose_class1)
    choose_class2 = choose_class('bar')
    print(choose_class2)
    Person = type('Person', (), {'nationality': 'ukranian', '__init__': __init__, '__str__': __str__})
    person1 = Person()
    print(f'{person1.name}  age={person1.age}')
    person2 = Person('Mark', 99)
    print(f'{person2.name}  age={person2.age}')
    print(person2)
    print(Person.nationality)
    person = Person('Valerii')
    person.show()
    print(Person.nationality)
