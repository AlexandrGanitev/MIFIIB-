N = 2
M = 3
# заполнили матрицу последовательными числами
matrix = [
    [0, 1, 2],
    [3, 4, 5],
]

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()  # перенос на новую строку

# 0 1 2
# 3 4 5