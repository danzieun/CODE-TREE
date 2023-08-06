s_list = list(input())
dir_num = 3
row, column = 0, 0
dRows, dColumns = [0, 1, 0, -1], [1, 0, -1, 0]

time, result = 0, -1
for s in s_list:
    if s == 'L':
        dir_num = (dir_num + 3) % 4
        time += 1
    elif s == 'R':
        dir_num = (dir_num + 1) % 4
        time += 1
    elif s == 'F':
        row, column = row + dRows[dir_num], column + dColumns[dir_num]
        time += 1
    if row == 0 and column == 0:
        result = time
        break

print(result)