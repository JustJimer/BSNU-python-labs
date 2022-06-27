from math import *
from abc import *


class Base:
    def __init__(self, x=22):
        print('init Base')
        self.x = x


class A(Base):
    def __init__(self, x=1, y=2):
        print(f'init A')
        super().__init__(self)
        self.y = y


class B:
    def __init(self):
        print('init B')


class C1(A, B):
    def __init__(self, c):
        print('init C1')
        super().__init__()
        self.c = c


class C2(B, A):
    def __init__(self, c):
        print('init C2')
        super().__init__()
        self.c = c


class Base1():
    def __init__(self):
        print('init Base')


class A1(Base1):
    def __init__(self, x=1, y=2):
        print(f'init A')
        super().__init__()


class B1(Base1):
    def __init__(self):
        print('init B')


class D1(Base1):
    pass


class C3(A1, B1):
    def __init__(self):
        print('init C1')
        super().__init__()


class C4(B1, A1):
    def __init__(self):
        print('init C2')
        super().__init__()


class C5(D1, A1):
    pass


class Figure:
    @abstractmethod
    def square(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, high):
        self.width = width
        self.high = high

    def square(self):
        return self.width * self.high


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def square(self):
        return pi * self.r * 2


if __name__ == "__main__":
    c1 = C1(43)
    print()
    c2 = C2(34)
    c3 = C3()
    print()
    c4 = C4()
    print()
    c5 = C5()

    print(C3.mro())
    print(C4.mro())
    print(C5.mro())

    shape = [Rectangle(13, 32), Circle(7)]

    sum_ = 0

    for item in shape:
        sum_ += item.square()
    print(sum_)

    sum_ = sum(item.square() for item in shape)
    print(sum_)
