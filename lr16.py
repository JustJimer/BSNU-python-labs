import numpy
import sys

# Створіть із списку одновимірний масив
task1 = numpy.array([1, 2])
print(type(task1))
print(task1)

# Створіть із кортежу одновимірний масив
print()
task2 = numpy.empty((2, 2))
print(task2)

# Знайдіть суму  та добуток цих масивів
print()
task3 = task1 + task2
print(task3)

# Помножте всі елементи останнього масиву на 3
print()
task4 = task3 * 3
print(task4)

# Створіть  одновимірний масив, який містить 3000 елементів, значення починаються з 0 та до 2999
print()
print(numpy.arange(0, 3000, 1))

# Продемонструйте в коді виведення елементів масиву на екран за замовчуванням
numpy.set_printoptions(threshold=sys.maxsize)

# Виведіть всі елементи масиву на екран
print()
print(numpy.arange(0, 666, 1))

# Створіть пустий двовимірнй масив
array = numpy.empty((0, 4), int)

# Заповніть частину  масиву значеннями
print()
array = numpy.append(array, numpy.array([[6, 3, 72, 34]]), axis=0)
array = numpy.append(array, numpy.array([[74, 24, 56, 12]]), axis=0)
print(array)

# Виведіть на екран розмір масиву, визначену програмним способом
print()
print(array.size)

# Виведіть на екран кількість рядків та кількість стовпчиків, визначену програмним способом
print()
print(array.shape)

# Продемонструйте в коді способи копіювання масивів
task12_1 = numpy.array([[5, 2, 1], [1, 2, 5]])
task12_2 = task12_1

if task12_2 is task1:
    print('task12_2 is task1')
else:
    print("task12_2 isn't task1")

task12_2 = task12_1.view()

if task12_2 is task12_1:
    print('task12_2 is task12_1')

task12_2[0, 0] = 666
print(task12_1[0, 0])
task12_2 = task12_1.copy()

if task12_2 is task12_1:
    print('task12_2 is task12_1')
