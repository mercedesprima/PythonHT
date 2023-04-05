# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
#
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
#


                                            # 1 вариант
def show_table(table):
    print('\n'.join('\t'.join(map(str, row)) for row in table))

def print_operation_table(operation, num_columns, num_rows):
    table = [list(range(i, i+num_columns)) for i in range(1, num_rows+1)]
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            table[i][j] = operation(table[i][0], table[0][j])
    show_table(table)
num_rows = int(input("Введите количество строк: "))
num_columns = int(input("Введите количество столбцов: "))
print_operation_table(lambda x, y: x * y, num_rows, num_columns)


                                            # 2 вариант (Роман)
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             if i != 1 and j != 1:
#                 print(operation(j, i), end="\t")
#             elif i == 1:
#                 print(j, end="\t")
#             else:
#                 print(i, end="\t")
#         print()
#
# print_operation_table(lambda x, y: x * y)