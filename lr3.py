import copy


def task1():
    print("TASK1")
    l1 = [1, 2, 3]
    print(l1)
    l2 = list('test')
    print(l2)


def task2():
    print("\n\nTASK2")
    l1 = [1, 2, 3, 4, 5]
    print('l1 id = ', id(l1))
    l2 = l1
    print('l2 id = ', id(l2))
    l3 = l1[:]
    print('l3 id = ', id(l3))
    l4 = copy.copy(l1)
    print('l4 id = ', id(l4))
    l5 = copy.deepcopy(l1)
    print('l5 id = ', id(l5))


def task3():
    print("\n\nTASK3")
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 0]
    print(l1)
    l1.extend(l2)
    print(l1)


def task4():
    print("\n\nTASK4")
    l1 = [1, 2, 3, 444444, 5]
    print(l1)
    print(l1[0])
    l1[1] = [1, 2, 3]
    print(l1)
    l1.remove(l1[2])
    print(l1)
    l1 = [1, 2, 3, 444444, 5]
    print(max(l1))


def task5():
    print("\n\nTASK5")
    l = [22, ['ogo', 3, 88], 'apple']
    print(l[1][2])


def task6():
    print("\n\nTASK6")
    l1 = [1, 2, 3, 4, 5]
    l2 = l1[(len(l1) // 2):]
    print(l2)


def task7():
    print("\n\nTASK7")
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = l1[(len(l1) - 3):] + l1[:(len(l1) - 3)]
    print(l1)
    print(l2)


def task8():
    print("\n\nTASK8")
    l1 = [1, -2, 3, 0, -5, 6, 0, 8, 9]
    print(l1)
    for i in range(len(l1)):
        if l1[i] >= 0:
            l1[i] = 1
    print(l1)


def task9():
    print("\n\nTASK9")
    l1 = [1, -2, 3, 0, -5, 6, 0, 8, 9]
    print(l1)
    l1.sort(reverse=True)
    print(l1)


def task10():
    print("\n\nTASK10")
    l1 = [1, 2, 3, 4]
    for i in l1:
        print(i)

    print(f"sum = {sum(l1)}")


def task11():
    print("\n\nTASK11")
    s = "Hello"
    l = []
    for i in list(s):
        l.append(i * 3)
    print(l)


def task12():
    print("\n\nTASK12")
    l = [1, 9]
    l2 = []
    for i in range(l[0] + 1, l[1], 2):
        l2.append(i)
    print(l2)


def task13():
    print("\n\nTASK13")
    n1 = int(input("Please, enter first number: "))
    n2 = int(input("Please, enter last number: "))
    l1 = []
    for i in range(n1, n2 + 1):
        l1.append(i)
    print(l1)


def task14():
    print("\n\nTASK14")
    s = "Hello my dear friend"
    l1 = s.split()
    print(s)
    print(l1)


def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()
    task12()
    task13()
    task14()
