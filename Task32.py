# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

min = int(input("Введите минимальный элемент списка:  "))
max = int(input("Введите минимальный элемент списка:  "))

import random
list_1 = [random.randint(-10, 30) for _ in range(10)]
print(list_1)
# result_list = []
# for i in range(len(random_list)):
#     if min <= random_list[i] <= max:
#         # result_list.append([i])
#         print(random_list)
#         print(i, end=' ')
for i in range(len(list_1)):
        if min <= list_1[i] <= max:
            print(i)
