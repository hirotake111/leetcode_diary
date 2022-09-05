# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = []
for arr in matrix:
    result += [i for i in arr]

print(result)

print([i for arr in matrix for i in arr])
