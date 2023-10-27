# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8 -> 9

# Вариант 1
# n = int(input("Enter number:  "))
# from random import randint
# list = [randint(0, 9) for i in range(n)]
# print(list)
# y = int(input("Enter digit: "))
# count = 0
# for i in list:
#     if y == i-1:
#         print(i)

# Вариант 2
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

# Вариант 3

n = int(input("Enter quantity of elements:   "))
list_1 = list()
for i in range(n):
    x = int(input("Enter elements of massive:"))
    list_1.append(x)

x = int(input("Enter closer number:"))
dist = abs(x - list_1[0])
number = list_1[0]
for i in range(1, n):
    if dist > abs(list_1[i] - x):
        dist = abs(list_1[i] - x)
        number = list_1[i]

print(number)
