import re


# def login(a):
#     return re.findall(r'^[A-Za-z0-9_@-]{6,18}$', password)
#
#
# password = input("Задайте пароль: ")
# print(login(password))


s = r'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимальные ежемесячных осадков.'
reg = "[0-3][1-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]"
print(re.findall(reg, s))
