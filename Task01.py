# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3 -> 2

n = int(input("Enter number:  "))
from random import randint
list = [randint(0, 9) for i in range(n)]
print(list)
y = int(input("Enter digit: "))
count = 0
for i in list:
    if y == i:
     count += 1

print(count)

list_1 = [1, 2, 3, 4, 5]
k = 3


# Введите ваше решение ниже

count = 0
for i in list_1:
    if k == i:
     count += 1

print(count)

