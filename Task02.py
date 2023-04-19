# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8 -> 9

n = int(input("Enter number:  "))
from random import randint
list = [randint(0, 9) for i in range(n)]
print(list)
y = int(input("Enter digit: "))
count = 0

for i in list:
    if y == i-1:
        print(i)