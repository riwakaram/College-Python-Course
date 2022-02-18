def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


a, b = map(int, input("Input the range [a, b] => ").split())
lst = [fibonacci(x) for x in range(a, b+1)]
print(lst)
