def is_square(mat):
    return all([len(i) == len(mat) for i in mat])


def transpose(lst):
    return [[row[i] for row in lst] for i in range(len(lst[0]))]


def rowEqualCol(array):
    if not array or not is_square(array):
        return False

    t = transpose(array)

    for i in array:
        for j in t:
            if i == j:
                return True

    return False


A = [[1, 4, 3], [4, 5, 6], [7, 6, 9]]
print(rowEqualCol(A))

B = [[1, 4, 3], [4, 5, 6], [7, 5, 9]]
print(rowEqualCol(B))
