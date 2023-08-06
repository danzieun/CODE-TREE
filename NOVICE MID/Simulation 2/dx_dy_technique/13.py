n, t = map(int, input().split())
ss = list(input())
nmap = []
for _ in range(n):
    nmap.append(list(map(int, input().split())))

row, column = n // 2, n // 2
drows, dcolumns = [-1, 0, 1, 0], [0, -1, 0, 1]
dir_num = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

result = nmap[row][column]
for s in ss:
    if s == 'L':
        dir_num = (dir_num + 1) % 4
    elif s == 'R':
        dir_num = (dir_num + 3) % 4
    elif s == 'F':
        drow, dcolumn = row + drows[dir_num], column + dcolumns[dir_num]

        if in_range(drow, dcolumn):
            row, column = row + drows[dir_num], column + dcolumns[dir_num]
            result += nmap[row][column]

print(result)