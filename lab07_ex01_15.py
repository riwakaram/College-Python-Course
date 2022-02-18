def sum_positive(a):
    if not a:
        return 0

    sum = 0

    for i in range(0, len(a)):
        if a[i] > 0:
            sum += a[i]

    return sum


lst = [3, -3, 5, 2, -1, 2]
print(lst)
print(sum_positive(lst))
