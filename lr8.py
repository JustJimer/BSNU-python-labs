import re


def task1_1():
    print('TASK1.1')
    l = [[1, 8], [5, 3], [2, 6]]
    print(l)
    l.sort(key=lambda l:l[1])
    print(l)


def task1_2():
    print('\n\nTASK1.2')
    string = "This is a test string from Andrew"
    word = string.split()
    result = ""
    for word_ in sorted(word):
        result = result + " " + word_
    print(result)


def task1_3():
    print('\n\nTASK1.3')
    l = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
    print(l)
    l.sort(key=lambda x: x[2])
    print(l)


def task1_4():
    print('\n\nTASK1.4')
    ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
    print(ids)
    ids.sort(key=lambda x: float(x[2:]))
    print(ids)


def task1_5():
    print('\n\nTASK1.5')
    l = ['cat', 'dog', 'cow']
    print(l)
    l = list(map(str.upper, l))
    print(l)


def task1_6():
    print('\n\nTASK1.6')
    l = ['cat', 'dog', 'cow']
    print(l)
    l = list(filter(lambda x: x != 'cat', l))
    print(l)


def task1_7():
    print('\n\nTASK1.7')
    s = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
    print(s)
    s = sorted(s.items(), key=lambda value: float(value[1]))
    print(s)


def task2():
    print('\n\nTASK2')
    l = [10, 20, 40, 80]
    print(l)
    result1 = list(map(lambda x: x * 2, l))
    print(result1)
    result2 = [i * 2 for i in l]
    print(result2)


def task3():
    print('\n\nTASK3')
    n = input("Enter any float number - ")
    temp = re.sub(',', '', n)
    result = sum(list(map(int, temp)))
    print(result)


def task4():
    print('\n\nTASK4')
    t = ((2, 3), (1, 2))
    result = sum([x for item in t for x in item])
    print(result)


def task5():
    print('\n\nTASK5')
    result = list(map(int, input("Enter separated umber sequence - ").split()))
    print(result)


def task6():
    print('\n\nTASK6')
    l1 = [2, 3, 4, 1]
    l2 = [0, 3, 2, 1]
    result = list(map(lambda x, y: pow(x, y), l1, l2))
    print(result)


def main():
    task1_1()
    task1_2()
    task1_3()
    task1_4()
    task1_5()
    task1_6()
    task1_7()
    task2()
    task3()
    task4()
    task5()
    task6()
