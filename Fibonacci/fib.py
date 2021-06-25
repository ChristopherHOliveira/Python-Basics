def fib(n):
    cont = 0
    list_fib = []
    n1 = 0
    n2 = 1

    if n == 0:
        return list_fib

    elif n == 1:
        list_fib.append(n1)
        return list_fib

    elif n == 2:
        list_fib.append(n1)
        list_fib.append(n2)
        return list_fib

    else:
        list_fib.append(n1)
        list_fib.append(n2)
        while cont < n-2:
            n3 = n1 + n2
            list_fib.append(n3)
            n2 = n1
            n1 = n3
            cont += 1

    return list_fib


# exemplos
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(13))
