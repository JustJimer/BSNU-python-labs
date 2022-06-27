import copy


def task1_1():
    print("TASK1_1")
    tup1 = tuple()
    print(tup1)
    tup2 = ()
    print(tup2)
    tup3 = ('x',)
    print(tup3)
    tup4 = 'y'
    print(tup4)
    tup5 = tuple('Something')
    print(tup5)


def task1_2():
    print("\n\nTASK1_2")
    tup1 = (123, 234, 345)
    tup2 = tup1
    print(tup1)
    print(tup2)
    tup1 = (111, 222, 555)
    print(tup1)
    print(tup2)
    tup3 = (5, 6, [7, 8])
    tup4 = copy.deepcopy(tup3)
    tup3[2][1] = 9999
    print(tup3)
    print(tup4)


def task1_3():
    print("\n\nTASK1_3")
    tup1 = (10, 20, 30)
    tup2 = (70, 80, 90)
    tup1 += tup2
    print(tup1)
    l1 = list(tup1)
    l1.extend(tup1)
    tup1 = tuple(l1)
    print(tup1)


def task1_4():
    print("\n\nTASK1_4")
    t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 100)
    print(t1[0])
    l1 = list(t1)
    l1[1] = [11, 22, 33]
    t2 = tuple(l1)
    print(t2)
    print(t1)


def task1_5():
    print("\n\nTASK1_5")
    t = (22, ('ogo', 3, 88), 'apple')
    print(t[1][0])


def task1_6():
    print("\n\nTASK1_6")
    t1 = (1, 2, 3, 4, 5, 6)
    t2 = t1[len(t1) // 2:]
    print(t2)


def task1_7():
    print("\n\nTASK1_7")
    tup = (3, 1, 5, 2, 6, 7)
    tup = tuple(sorted(tup, reverse=True))
    print(tup)


def task1_8():
    print("\n\nTASK1_8")
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    sum_ = 0
    for i in tup:
        print(i)
        sum_ += i
    print(f"sum = {sum_}")


def task1_9():
    print("\n\nTASK1_9")
    t1 = ((342, 12), (34, 4), (21,))
    print(t1)
    t1 = tuple(sorted(t1, key=lambda item: item[0]))
    print(t1)


def task1_10():
    print("\n\nTASK1_10")
    t1, t2, t3 = False, False, False
    if True in (t1, t2, t3):
        print('YES')
    else:
        print('NO')


def task1_11():
    print("\n\nTASK1_11")
    for i in range(1, 4):
        print(i)
        break
    else:
        print("No Break")


def task1_12():
    print("\n\nTASK1_12")
    t1 = (['a', 'b'], 'hello')
    t2 = copy.deepcopy(t1)
    t2[0][1] = 'not_original'
    print(f't1={t1}')
    print(f't2={t2}')
    t3 = ('a', 'b', 'hello')
    t4 = t3
    print(f't3={t3}')
    print(f't4={t4}')

############################################


def task2_1():
    print("\n\nTASK2_1")
    a = tuple(x + 1 for x in range(0, 10))
    print(a)


def task2_2():
    print("\n\nTASK2_2")
    s = 'spam'
    ss = tuple([ch * 2 for ch in s])
    print(ss)


def task2_3():
    print("\n\nTASK2_3")
    s = "spam"
    t1 = tuple(s[x] for x in range(0, len(s)) if x % 2 == 0)
    print(t1)


def task2_4():
    print("\n\nTASK2_4")
    l1 = [(x, x * x) for x in range(0, 5)]
    print(l1)


def task2_5():
    print("\n\nTASK2_5")
    PI = 3.14159
    l1 = [f'{round(PI, n)}' for n in range(1, 6)]
    print(l1)


def task2_6():
    print("\n\nTASK2_6")
    l = [[1, 2, 3], [4, 7, 8], [5, 4, 3]]
    l1 = [(i, j) for i in range(3) for j in range(3) if l[i][j] == 4]
    print(l1)


def task2_7():
    print("\n\nTASK2_7")
    n1 = int(input("enter first value: "))
    n2 = int(input("enter second value: "))
    if n1 < n2:
        l1 = [x for x in range(n1, n2)]
        print(l1)
    else:
        print("second value smaller then first one")


def task2_8():
    print("\n\nTASK2_8")
    l = [[3, 2, 1], [7, 5, 3], [4, 4, 7], [1, 3, 2], [9, 7, 4], [5, 7, 9]]
    g = (l[i][j] for i in range(len(l)) for j in range(len(l[i])) if i % 2 != 0 and j % 2 != 0)
    v = next(g, "end")
    while v != "end":
        print(v)
        v = next(g, "end")


def task2_9():
    print("\n\nTASK2_9")
    l = [-1, 3, -5, 6, 7, 6, -7, 8]
    l1 = [x if x > 0 else x * (-1) for x in l]
    print(l1)


def main():
    task1_1()
    task1_2()
    task1_3()
    task1_4()
    task1_5()
    task1_6()
    task1_7()
    task1_8()
    task1_9()
    task1_10()
    task1_11()
    task1_12()

    task2_1()
    task2_2()
    task2_3()
    task2_4()
    task2_5()
    task2_6()
    task2_7()
    task2_8()
    task2_9()
