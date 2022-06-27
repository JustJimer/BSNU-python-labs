def task1_1(a, b):
    print(max(a, b))


def task1_2(a='first', b='second', c='third', d='fourth'):
    print(a)
    print(b)
    print(c)
    print(d)
    print('\n')


def task1_3(a, b, c):
    print(a)
    print(b)
    print(c)
    print('\n')


def task1_4(*params):
    sum_ = 0
    for i in params:
        sum_ += i
    print(sum_)


def task1_5(a, b):
    return b, a


def task1_6(a):
    b = [x * 2 for x in a]
    return b


def task1_7(a):
    b = [x[0] for x in a.split()]
    return b


def task1_8(a):
    sum_ = 0
    mult = 1

    for digit in str(a):
        sum_ += int(digit)
        mult *= int(digit)

    print('sum -', sum_)
    print('multiply -', mult)


def task1_9(n):
    list_ = list(map(int, input(f"\nEnter the {n} numbers: ").strip().split()))[:n]
    print('Minimum number is', min(list_))
    print('It repeats',  list_.count(min(list_)), 'times')


def task1_10(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return task1_10(n - 1) + task1_10(n - 2)


x = 10


def task1_11():
    global x
    print(x)
    x = 20
    print(x)
    y = 15

    def inside_func():
        print()
        nonlocal y
        print(y)
        y = 289
        print(y)
    inside_func()


def main():
    print('TASK1.1')
    task1_1(1, 5)
    task1_1(5.3, 2.1)
    task1_1(5.5, 6)

    print('\n\nTASK1.2')
    task1_2()
    task1_2('1')
    task1_2('1', '2')
    task1_2('1', '2', '3')
    task1_2('1', '2', '3', '4')

    print('TASK1.3')
    task1_3(b='b', c='c', a='a')

    print('TASK1.4')
    task1_4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    print('\n\nTASK1.5')
    print(task1_5('first', 'second'))

    print('\n\nTASK1.6')
    print(task1_6([1, 2, 3, 4, 5]))

    print('\n\nTASK1.7')
    print(task1_7('some random text to check function'))

    print('\n\nTASK1.8')
    task1_8(12345)

    print('\n\nTASK1.9')
    task1_9(5)

    print('\n\nTASK1.10')
    print(task1_10(7))

    print('\n\nTASK1.11')
    task1_11()

    print('\n\nTASK2')

    def func1(a, l=[]):
        # Так як список - змінний тип, то кожного разу до кінця списку буде додаватись значення змінної a
        # l = [] #----> Для уникнення результату, список потрібно оголошувати в тілі функції
        l.append(a)
        print(l)
    for i in range(4, 9):
        func1(i)

    print('\n\nTASK3')

    def func2(a, t=()):
        # Так як кортеж - незмінний тип, то кожного разу створюється новий кортеж
        t = t + (a,)
        print(t)
    for i in range(4, 9):
        func2(i)

    print('\n\nTASK4')

    def f(a, *, b):
        print(a, b)

    f(1, b=2)

    print('\n\nTASK5')

    def f(a, *c, b):
        print(a, b, c)

    f(1, 2, b=3)
    f(1, 2, 3, 4, 5, b=6)

    print('\n\nTASK6')

    def f333(x, *y, z, **w):
        print(x, y, z, w)

    f333(1, 2, z=3, w=4)

    print('\n\nTASK7')
    t = (21, 34, 56)

    def func4(a, b, c):
        print(a, b, c)
    func4(*t)

    print('\n\nTASK8')
    d = dict(fio='Ivanov', age=19, group=200)

    def func3(fio, age, group):
        print(fio, age, group)
    func3(**d)
