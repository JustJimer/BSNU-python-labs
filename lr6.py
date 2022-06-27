import json


def task1():
    l1 = ['task1.2', 'one', 'two', 'three']
    with open('lr6.txt', 'w') as f:
        f.write('task1.1\n')
        f.writelines('\n'.join(l1))


def task2():
    print("TASK2")
    with open('lr6.txt', 'r') as f:
        print('file.name - ', f.name)
        print('file.mode - ', f.mode)


def task3():
    print("\n\nTASK3")
    print('TASK3.1 read()')
    with open('lr6.txt') as f:
        print(f.read())

    print('\nTASK3.2 readline(5)')
    with open('lr6.txt') as f:
        print(f.readline(5))

    print('\nTASK3.3 readlines(10)')
    with open('lr6.txt') as f:
        print(f.readlines(10))

    print('\nTASK3.4')
    with open('lr6.txt') as f:
        for line in f:
            print(f'line={line}', end='')


def task4():
    print("\n\nTASK4")
    data = {3: 'three', 1: 'one', 2: 'two'}
    with open('lr6.js', 'w') as f:
        str_ = json.dumps(data)
        f.write(str_)


def task5():
    print("\n\nTASK5")
    with open('lr6.js', 'r') as f:
        data = json.load(f)
        data = [(int(key), value) for key, value in data.items()]
        print(data)


def task6():
    print("\n\nTASK6")
    # менеджер контексту використовувався у всіх завданнях вище


def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
