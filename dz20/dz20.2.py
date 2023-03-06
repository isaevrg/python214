with open('dz20.2.txt', 'w+') as f:
    f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')

with open('dz20.2.txt', 'r+') as f:
    lst = f.readlines()
    print(lst)

lst.reverse()
with open('dz20.2.txt', 'w+') as f:
    f.write(''.join([*lst]))

print(lst)
