
with open('dz20.1.txt', 'w+') as f:
    f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')

with open('dz20.1.txt', 'r+') as f:
    lst = f.readlines()
    print(lst)

num1 = int(input('Номер строки 1: ')) - 1
num2 = int(input('Номер строки 2: ')) - 1


if num1 == 0 and num2 == 1 or num1 == 1 and num2 == 0:
    lst[0], lst[1] = lst[1], lst[0]
elif num1 == 0 and num2 == 2 or num1 == 2 and num2 == 0:
    lst[0], lst[2] = lst[2], lst[0]
elif num1 == 1 and num2 == 2 or num1 == 2 and num2 == 1:
    lst[1], lst[2] = lst[2], lst[1]

with open('dz20.1.txt', 'w+') as f:
    f.write(''.join([*lst]))
print(lst)

