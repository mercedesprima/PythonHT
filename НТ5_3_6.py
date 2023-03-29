# Задача 3.
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам".

# def group_letter(input_list):
#     word_dic = {}
#     for word in input_list:
#         if frozenset(word), len(word) not in word_dic:
#             word_dic[frozenset(word)] = [len(word), word]
#         else:
#             if len(word) == word_dic[frozenset(word)][0]:
#                 word_dic[frozenset(word)].append(word)
#     res_list = []
#     for value in word_dic.values():
#         res_list.append(value[1:])
#     return res_list
# print(group_letter(["eat", "tea", "tan", "ate", "nat", "bat"]))

# input_words = ("eat", "tea", "tan", "ate", "nat", "bat")
# print(input_words)
# def letter_groups(input_words):
#     word_dict = {}
#     for word in input_words:
#         if (frozenset(word), len(word)) not in word_dict:
#             word_dict[(frozenset(word), len(word))] = [word]
#         else:
#             word_dict[(frozenset(word), len(word))].append(word)
#     res_list = []
#     for value in word_dict.values():
#         res_list.append(value)
#     return res_list
#
# print(letter_groups(input_words))


input_words = ("eat", "tea", "tan", "ate", "nat", "bat", "ant", "batt", "tab")

def letter_groups(input_words):
    dic = {}
    for i in input_words:
        key = "".join(sorted(i))
        if key not in dic:
            dic[key] = []

        dic[key].append(i)

    return list(dic.values())

print(input_words)
print(letter_groups(input_words))

# # Задача 6.
# Дана строка (возможно, пустая),состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку,
# если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений


# def rle(some_str):
#     res_list = []
#     some_str += ' '
#     temp_letter = some_str[0]
#     count_letter = 1
#     for ind in range(1, len(some_str)):
#         if some_str[ind] == temp_letter:
#             count_letter += 1
#         else:
#             if count_letter == 1:
#                 res_list.append(f'{temp_letter}')
#             else:
#                 res_list.append(f'{temp_letter}{count_letter}')
#             count_letter = 1
#             temp_letter = some_str[ind]
#     print(res_list)
#     print(*res_list, sep='')
#
# rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')


input_str = str(input("Введите строку, состоящую из букв A-Z:  ").upper())

def rle(input_str):
    result_list = []
    last_letter = ''
    count = 0

    for i in input_str:
        if i != last_letter:
            if last_letter:
                result_list += last_letter + str(count)
            count = 1
            last_letter = i

        else:
            count += 1
    else:
        result_list += last_letter + str(count)
        return result_list

result_list = rle(input_str)

import re
if re.match(r'^[a-zA-Z] + $', input_str ):
    print(*result_list, sep='')
else:
    print('Строка должна содержать только латинские буквы')
