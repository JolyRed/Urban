def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=1, b='строка', c=True, d=[1,2,3,4])

print_params(b=25)
print_params(c=[1,2,3])


values_list = [1, True, 'строка']
values_dict = {1: 'авпвап', 'строка': 1, True: False}

print_params(*values_list)
print_params(**values_dict)


values_list2 = [1, 'строка']

print_params(*values_list2, 42)

