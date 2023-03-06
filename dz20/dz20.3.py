with open('dz20.1.txt', 'r') as fr, open('dz20.2.txt', 'r') as fw:
    lst1 = fr.readlines()
    lst2 = fw.readlines()

lst3 = lst1 + lst2
with open('dz20.3.txt', 'w+') as f:
    f.write(''.join([*lst3]))

print(lst3)
