names = [-2, 3, 8, -11, -4, 6]

print(names)


def count_items(item_list):
    count = 0
    for item in item_list:
        if item < 0:
            count += 1
        else:
            count += 0
    return count


print("n =", count_items(names))



