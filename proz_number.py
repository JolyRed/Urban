def test(a=1, b='True', c=True, d=12.32):
    print(a, b, c, d)


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


number = int(input('введите число: '))

print(factorial(number))