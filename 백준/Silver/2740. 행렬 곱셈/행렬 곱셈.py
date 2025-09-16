import sys

def divide_Conquer():
    n, m = map(int, sys.stdin.readline().split())
    matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    m, k = map(int, sys.stdin.readline().split())
    matrix_b = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    matrix_c = [[0] * k for _ in range(n)]

    for i in range(n):
        for j in range(k):
            for l in range(m):
                matrix_c[i][j] += matrix_a[i][l] * matrix_b[l][j]

    for row in matrix_c:
        print(*row)

divide_Conquer()