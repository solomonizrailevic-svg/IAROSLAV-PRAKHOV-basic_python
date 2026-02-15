matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9, 10, 11, 12]
]
print(matrix)
print(matrix[1])
print(matrix[2][0])

matrix[0] = [0]
print(matrix)
matrix[1][-1] = ["Python"]
print(matrix)
