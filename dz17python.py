import re


# def valid_name(name):
#     return re.findall(r"[\+\d\s*\(\)-]{11,}", name)
#
#
# print(valid_name("+7 499 456-45-78"))
# print(valid_name("+74994564578"))
# print(valid_name("7 (499) 456 45 78"))
# print(valid_name("7 (499) 456-45-78"))


# sz19


a = [5, 9, 6, 7]
b = [3, 11, 8]
c = [2, 4]
d = [10, 1, 12]
print(a, b, c, d)


def sort(s):
    dan = int(input("1 - сортировать по убыванию\n2 - сортировать по возрастанию\n-> "))
    if dan == 1:
        e.sort(reverse=True)
    if dan == 2:
        e.sort()
    return e


e = a + b + c + d
sort(e)
print(e)



def seq_search(s, item):
    found = item
    pos = 0
    while pos < len(s) and not found:
        if s[pos] == item:
            found = item
        else:
            pos += 1

    return "Значение " + found + " найдено"



poisk = input("Введите значение для поиска: ")
print(seq_search(e, poisk))

