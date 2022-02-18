def count_evens(lst):
    if not lst:
        return 0

    count = 0

    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            count += 1

    return count


a = [3, 5, 4, -1, 0]
print(a)
print(count_evens(a))
