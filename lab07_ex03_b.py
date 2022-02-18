def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


lst = []
for i in range(15, 26):
    lst += [fibonacci(i)]

print(lst)