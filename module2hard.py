num = int(input('Введите число: '))

list_ = [i for i in range(1, num)]
new_list = []


def password(num):
    for i in list_:
        for j in list_:
            if num % (i + j) == 0:
                new_list.append([j, i])
    print(new_list)

    for i in new_list:
        i.sort()
    print(new_list)

    new_list_2 = []
    for i in new_list:
        while i not in new_list_2 and i[0] != i[1]:
            new_list_2.append(i)
        else:
            continue

    return new_list_2

print(password(num))
