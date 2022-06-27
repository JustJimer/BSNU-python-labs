try:
    test = 1 / 0
    raise ZeroDivisionError('code0')
except ZeroDivisionError as e:
    test = 666
    print(str(e))
    print(e.__class__)
print(test)

f = open('lr6.txt')
list_ = []
try:
    for line in f:
        list_.append(int(line))
except ValueError:
    print('errrrrrrror')
except Exception:
    print("it's impossible to see this")
else:
    print('all corect')
finally:
    f.close()
    print('finally closing file')


class CustomExceptionClass(Exception):
    pass


try:
    n = int(input("enter positive value - "))
    if n < 0:
        raise CustomExceptionClass("it's not positive - " + str(n))
    print(n + 5)
except CustomExceptionClass as e:
    print(e)
