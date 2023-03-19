# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X. 
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count). 
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
# *Пример:*
# 5
# 1 2 3 4 5 3 -> 1
                            # 1.
import time
start = time.perf_counter()
from random import randint
array_A = []
array_len = int(input("Введите количество элементов в массиве: "))
for i in range(array_len): 
    # array_A.append(int(input(f"Введите {i+1} число:  ")))
    array_A.append(randint(-100, 100))
x = int(input("Введите  число X: "))
print(array_A)
count = 0
for i in range(array_len):
    if x == array_A[i]: 
        count +=1 
print((f'Число {x} встречается {count} раз:'))
end = time.perf_counter()
first_time = end - start
print(first_time)

                                # 2.
import time
start = time.perf_counter()
from random import randint
array_A = []
array_len = int(input("Введите количество элементов в массиве: "))
for i in range(array_len): 
    # array_A.append(int(input(f"Введите {i+1} число:  ")))
    array_A.append(randint(-100, 100))
x = int(input("Введите  число X: "))
print(array_A)
count = array_A.count(x)
print(f'Число {x} встречается {count} раз:')
end = time.perf_counter()
second_time = end - start
print(second_time)

print(first_time / second_time)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5 6 -> 5

from random import randint
array = []
array_len = int(input("Введите количество элементов массива: "))
for i in range(array_len):
    # array.append(int(input(f"Введите {i+1} число:  ")))
    array.append(randint(-100, 100))
x = int(input("Введите число X: "))
min = 0
for i in range(array_len):
    if abs(array[i]-x) < abs(array[min]-x):
        min = i
print(array)
print(f"Самый близкий элемент: {array[min]}")

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# *Пример:*
# ноутбук
#     12
                    # Вариант единым словарем
dic = {
    1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r','а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'],
    2: ['d', 'g', 'д', 'к', 'л', 'м', 'п', 'у'], 
    3: ['b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я'], 
    4: ['f', 'h', 'v', 'w', 'y', 'й', 'ы'], 
    5: ['k', 'ж', 'з', 'х', 'ц', 'ч'],
    8: ['j', 'x', 'ш', 'э', 'ю'], 
    10: ['q', 'z', 'ф', 'щ', 'ъ']
    }
word = input("Введите слово:  ")
points = 0
for letter in word:
    for key in dic.items():
        if letter in key[1]:
            points += key[0]
print(word)
print(points)
                    # Вариант с 2-мя словарями и повторяющимся куском кода
# dic_en = {
#     1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'],
#     2: ['d', 'g'], 
#     3: ['b', 'c', 'm', 'p'], 
#     4: ['f', 'h', 'v', 'w', 'y'], 
#     5: ['k'],
#     8: ['j', 'x'], 
#     10: ['q', 'z']
#     }
# dic_ru = {
#     1: ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'] , 
#     2: ['д', 'к', 'л', 'м', 'п', 'у'], 
#     3: ['б', 'г', 'ё', 'ь', 'я'], 
#     4: ['й', 'ы'],
#     5: ['ж', 'з', 'х', 'ц', 'ч'],
#     8: ['ш', 'э', 'ю'], 
#     10: ['ф', 'щ', 'ъ']}
# word = input("Введите слово:  ")
# points = 0
# for letter in word:
#     for item in dic_ru.items():
#         if letter in item[1]:
#             points += item[0]
# if points == 0:
#     for letter in word:
#         for item in dic_en.items():
#             if letter in item[1]:
#                 points += item[0]
# print(word)
# print(points)