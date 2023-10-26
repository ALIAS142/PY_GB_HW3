# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3 -> 2


# Вариант 1:
n = int(input("Enter quantity:  "))
# from random import randint
# list = [randint(0, 9) for i in range(n)]
list = []
for i in range(n):
    x = int(input("Enter number:  "))
    list.append(x)
print(list)
y = int(input("Enter checking digit: "))
count = 0
for i in list:
    if y == i:
     count += 1
print(count)


# Вариант 2:
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count = 0
# for i in list_1:
#     if k == i:
#      count += 1
# print(count)

