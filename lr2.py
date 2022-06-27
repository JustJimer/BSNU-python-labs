def task1():
    print("TASK1")
    num1 = int(input("Please, enter first number: "))
    num2 = int(input("Please, enter second number: "))
    num3 = int(input("Please, enter third number: "))
    num4 = int(input("Please, enter fourth number: "))
    sum1 = num1 + num2
    sum2 = num3 + num4
    result = sum1 / sum2
    print("Result 1.1 = " + '%.2f' % result)
    result = sum1 // sum2
    print(f"Result 1.2 = {result}")
    result = sum1 % sum2
    print(f"Result 1.3 = {result}")


def task2():
    print("\n\nTASK2")
    txt = 'Hello, world'
    string1 = txt[1:4]  # ell
    print(string1)
    string2 = txt[:2]  # He
    print(string2)
    string3 = txt[1:]  # ello, world
    print(string3)
    string4 = string2[:1] + string3[2:4] + string3[5] + string3[3] + string1[1]  #Hlo ol
    print(string4)
    string5 = txt.upper()  # HELLO, WORLD
    print(string5)
    string6_1 = 'J' + txt[1:]  # Jello, world
    print(string6_1)
    string6_2 = txt.replace('H', 'J')  # Jello, world
    print(string6_2)
    # string7 = txt + 2 - ERROR -> INT TO STR
    string8 = txt * 2
    print(string8)  # Hello, worldHello, world


def task3():
    print("\n\nTASK3")
    while True:
        string = input("Please, enter something [type exit to exit]: ")
        if "exit" in string:
            return
        else:
            print(string)
            continue


def task4():
    print("\n\nTASK4")
    string = 'Hello, world'
    ch = input("Please, enter any character: ")
    if ch in string:
        print("YES")
    else:
        print("NO")
    ###########
    ch = input("Please, enter any character: ")
    if string.find(ch) == -1:
        print("NO")
    else:
        print("YES")


def task5():
    print("\n\nTASK5")
    s1 = "qwerty"
    s2 = s1
    s3 = s1[:]
    print(f"id s1={id(s1)} id s2={id(s2)} id s3={id(s3)}")


def task6():
    print("\n\nTASK6")
    string1 = "q,w,e,r,t,y"
    string2 = ""
    string2 = string2.join(string1.split(','))
    print(string1)
    print(string2)


def task7():
    print("\n\nTASK7")
    n = int(input("Please, enter any number: "))
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        print("prime number")


def task8():
    print("\n\nTASK8")
    for i in range(3, 12, 3):
        print(i)


def task9():
    print("\n\nTASK9")
    string = input("Please, enter something: ")
    for i in string:
        print(i.upper())


def task10():
    print("\n\nTASK10")
    string1 = input("Please, enter your Name and Surname: ")
    print(string1)
    temp = string1.split()
    temp.reverse()
    string2 = " ".join(temp)
    print(string2)


def task11():
    print("\n\nTASK11")
    string1 = "camel_case"
    string1 = string1.title()
    string2 = ''.join(string1.split('_'))
    print(string1)
    print(string2)


def task12():
    print("\n\nTASK12")
    string1 = "camel_case"
    string2 = string1.capitalize()
    print(string1)
    print(string2)


def task13():
    print("\n\nTASK13")
    string = input("Please, enter any sequence: ")
    if string.isdecimal():
        string = int(string)
        print(string)
    else:
        print("ERROR, string contains not decimal characters")


def task14():
    print("\n\nTASK14")
    string = input("Please, enter something: ")
    if string.isupper():
        print("All characters is capitals")
    else:
        print("Not all characters is capitals")


def task15():
    print("\n\nTASK15")
    string = "Qw12Vb"
    count1 = 0
    count2 = 0
    for i in string:
        if i.islower():
            count1 = count1 + 1
        elif i.isupper():
            count2 = count2 + 1
    print("The number of lowercase characters is:")
    print(count1)
    print("The number of uppercase characters is:")
    print(count2)


def task16():
    print("\n\nTASK16")
    string1 = input("Please, enter something: ")
    string2 = string1[::-1]
    print(string1)
    print(string2)


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
    task15()
    task16()
