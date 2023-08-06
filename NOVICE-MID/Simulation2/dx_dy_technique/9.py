n = int(input())
n_list = [list(input()) for _ in range(n)]
k = int(input())

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

dir_num = ((k - 1) // n + 1) % 4
dir_num_2 = 0
row, column = 0, 0
drows, dcolumns = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(k - 1):
    drow, dcolumn = row + drows[dir_num_2], column + dcolumns[dir_num_2]
    if not in_range(drow, dcolumn):
        dir_num_2 = (dir_num_2 + 1) % 4
    else:
        row, column = row + drows[dir_num_2], column + dcolumns[dir_num_2]

cnt = 0
while in_range(row, column):
    if n_list[row][column] == '/':
        if dir_num == 0:
            dir_num = 3
        elif dir_num == 1:
            dir_num = 2
        elif dir_num == 2:
            dir_num = 1
        elif dir_num == 3:
            dir_num = 0
    elif n_list[row][column] == '\\':
        if dir_num == 0:
            dir_num = 1
        elif dir_num == 1:
            dir_num = 0
        elif dir_num == 2:
            dir_num = 3
        elif dir_num == 3:
            dir_num = 2
    row, column = row + drows[dir_num], column + dcolumns[dir_num]
    cnt += 1
    
print(cnt)