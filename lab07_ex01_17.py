def print_big_enough(lst, num):
    if not lst:
        return 0

    for i in range(0, len(lst)):
        if lst[i] >= num:
            print(lst[i])


a = [3, 5, 4, -1, 0]
print(a)
print_big_enough(a, 3)
