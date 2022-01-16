def task1():
    print("TASK1")
    a = 2
    b = 2
    print(f'id of a = {id(a)}')
    print(f'id of a = {id(b)}')
    if a is b:
        print("a and b are same")
    else:
        print("a and b are NOT same")


def task2and3():
    print("\n\nTASK2")
    name = input("Please, enter your name: ")
    age = input("Please, enter your age: ")
    place = input("Where are you live? ")
    print("Your name = " + name)
    print("Your age = " + age)
    print("You live in = " + place)
    print("\n\nTASK3")
    print(f'Doubled age = {int(age) * 2}')


def task4():
    print("\n\nTASK4")
    user_answer = input("Try to solve: 4 * 100 - 54: ")
    print("Your answer: " + user_answer)
    print(f'Right answer: {4 * 100 - 54}')


def task5():
    print("\n\nTASK5")
    num1 = int(input("Please, enter first number: "))
    num2 = int(input("Please, enter second number: "))
    num3 = int(input("Please, enter third number: "))
    num4 = int(input("Please, enter fourth number: "))
    sum1 = num1 + num2
    sum2 = num3 + num4
    result = sum1 / sum2
    print("Result = " + '%.2f' % result)


def task6():
    print("\n\nTASK6")
    a = 4
    b = 2
    c = a / b
    print(type(c))


def task7():
    print("\n\nTASK7")
    a = 2
    b = bool(a)
    print(f'a = {a}')
    print(f'a = {b}')


def task8():
    print("\n\nTASK8")
    a = 2
    b = 3.33
    c = a + b
    print(f'c = {c}')
    print(f'type of c = {type(c)}')

    c = a + int(b)
    print(f'c = {c}')
    print(f'type of c = {type(c)}')


def task9():
    print("\n\nTASK9")
    a = 1
    b = '1'
    c = chr(a)
    d = int(b)
    print(type(c))
    print(type(d))


def task10():
    print("\n\nTASK10")
    a: int = "ITS NOT INT"
    b: str = 1234
    print(type(a))
    print(type(b))


def task11():
    print("\n\nTASK11")


def run():
    task1()
    task2and3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()
