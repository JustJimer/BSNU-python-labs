def task2():
    print("TASK2")
    set1 = {'one', 'two', 'three'}
    print('set1', set1)
    set2 = set()
    print('set2', set2)
    set3 = set("example")
    print('set3', set3)


def task3():
    print("\n\nTASK3")
    set1 = {'one', 'two'}
    print(set1)
    set1.add('three')
    print(set1)


def task4():
    print("\n\nTASK4")
    set1 = {1, 2}
    set2 = {7, 9}
    set3 = {*set1, *set2}
    print(set3)


def task5():
    print("\n\nTASK5")
    set1 = {1, 2, 3, 4, 5, 6, 7, 8}
    for i in set1:
        print(i, end=' ')
    n1 = int(input("\nenter any value: "))
    if n1 in set1:
        print(n1, 'is in set')
    else:
        print(n1, 'was not found in set')


def task6():
    print("\n\nTASK6")
    set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set2 = {1, 3, 5, 7, 9}
    set3 = set1 - set2
    print(set1)
    print(set2)
    print(set3)


def task7():
    print("\n\nTASK7")
    set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set2 = {1, 3, 5, 7, 9}
    set3 = set1 - (set1 - set2)
    print(set1)
    print(set2)
    print(set3)


def task8():
    print("\n\nTASK8")
    set1 = set((x, x * x * x) for x in range(1, 5))
    print(set1)


def task9():
    print("\n\nTASK9")
    set1 = set()
    set1.add(1)
    set1.add(10.5)
    set1.add('str')
    set1.add((10, 20))
    print(set1)


def task10_11_12():
    print("\n\nTASK10-12")
    set1 = {1, 2, 3, 4, 5}
    print(set1)
    set1.remove(2)
    set1.discard(8)
    print(set1)
    set1.clear()
    print(set1)
    del set1


def task13():
    print("\n\nTASK13")
    fs = frozenset("something")
    print(fs)


def task14():
    print("\n\nTASK14")
    l = [x for x in range(6)] + [x for x in range(3, 12)]
    print(l)
    l = list(set(l))
    print(l)


###########################################


def task16():
    print("\n\nTASK16")
    d = {"name": "Valerii", "age": 18}
    print(d)


def task17():
    print("\n\nTASK17")
    d = dict(name="Valerii", age=18)
    print(d)


def task18():
    print("\n\nTASK18")
    d1 = {"name": "Valerii", "age": 18}
    d2 = {"nationality": "ukranian", "sex": 'male'}
    d3 = dict(d1)
    d3.update(d2)
    print(d3)


def task19():
    print("\n\nTASK19")
    d1 = {
        "name": "Valerii",
        "age": 18,
        "nationality": "ukranian",
        "sex": 'male'
    }

    for key in d1:
        print(key, d1[key])
    print('\n')
    for key in d1.keys():
        print(key, d1[key])

    inp = input("\nenter value to check: ")
    if inp in d1:
        print(inp, 'is in dictionary')
    else:
        print(inp, "wasn't found in dictionary")


def task20():
    print("\n\nTASK20")
    d1 = dict.fromkeys(("one", "two", "three"), 33)
    for key in d1:
        print(key, d1[key])


def task21():
    print("\n\nTASK21")
    d1 = dict.fromkeys(("one", "two", "three"), (33, 44))
    for key in d1:
        print(key, d1[key])


def task22():
    print("\n\nTASK22")
    d1 = {x: x*2 for x in range(5)}
    print(d1)


def task23():
    print("\n\nTASK23")
    d = dict(a="hello", b=2, c=3, d="hello")
    list_key = [key for key in d if d[key] == 'hello']
    print(list_key)


def task24():
    print("\n\nTASK24")
    d1 = {
        4: "Integers",
        1.5: "Floating-Point numbers",
        True: "Booleans",
        "str": "Strings",
        (10, 20): "Tuples"
    }
    for key in d1:
        print(key, d1[key])


def task25():
    print("\n\nTASK25")
    t1 = ((1,'one'),(2,'two'))
    d1 = dict(t1)
    print(d1)


def task26():
    print("\n\nTASK26")
    l1 = [(1,'one'),(2,'two')]
    d1 = dict(l1)
    print(d1)


def task27():
    print("\n\nTASK27")
    d1 = {'1': 'one', '2': 'two'}
    print(d1)
    d2 = dict((v, k) for k, v in d1.items())
    print(d2)


def task28_29():
    print("\n\nTASK28-29")
    d1 = {
        "name": "Valerii",
        "age": 18
    }
    print(d1)
    d1.pop('name')
    print(d1)
    d1.clear()
    print(d1)


def task30():
    print("\n\nTASK30")
    d1 = {
        "name": "Valerii",
        "age": 18
    }
    print(d1)
    check = d1.get('nationality', 'error')
    print(check)


def main():
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10_11_12()
    task13()
    task14()

    task16()
    task17()
    task18()
    task19()
    task20()
    task21()
    task22()
    task23()
    task24()
    task25()
    task26()
    task27()
    task28_29()
    task30()
