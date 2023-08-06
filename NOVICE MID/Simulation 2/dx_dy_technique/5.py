n, m = map(int, input().split())

answer = [[0] * m for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m


row, column = 0, 0
dRows, dColumns = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0

answer[row][column] = 1
for i in range(2, n * m + 1):
    dRow, dColumn = row + dRows[dir_num], column + dColumns[dir_num]
    if not in_range(dRow, dColumn) or answer[dRow][dColumn] != 0:
        dir_num = (dir_num + 1) % 4
    row, column = row + dRows[dir_num], column + dColumns[dir_num]
    answer[row][column] = i


for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()