class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x - {self.x} | y - {self.y}'

    def __add__(self, additional):
        return Position(self.x + additional.x, self.y + additional.y)


class Place:
    def __init__(self, type_):
        self.type = type_

    def __call__(self, new_type):
        self.type = new_type

    def __str__(self):
        return f'self.type - {self.type}'


class A:
    def __init__(self, arg):
        self.arg = arg

        def __str__():
            return str(self.arg)


class B:
    def __init__(self, *args):
        self.list_ = []
        for i in args:
            self.list_.append(A(i))

    def __getitem__(self, key):
        return self.list_[key]

    def __setitem__(self, key, value):
        self.list_[key] = value


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person(' + self.name + ',' + str(self.age) + ')'
        return rep


if __name__ == "__main__":
    dot1 = Position(64, 23)
    dot2 = Position(72, 92)

    dot3 = dot1 + dot2
    print(f'dot3 - {dot3}')

    bar = Place("bar")
    club = Place("club")
    bar("bar")
    club("club")

    print(bar, club)

    b = B(64, 23, 'xyz')

    print(b.list_[1])
    print(b[1])

    b[1] = 666

    print(b.list_[1])

    person = Person("Valerii", 19)
    print(repr(person))
