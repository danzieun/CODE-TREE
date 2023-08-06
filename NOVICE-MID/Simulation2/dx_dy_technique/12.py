n = int(input())
nmap = [[0] * n for _ in range(n)]

row, column = n // 2, n // 2
dir_num, move_num = 0, 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def move():
    global row, column
    drows, dcolumns = [0, -1, 0, 1], [1, 0, -1, 0]
    row, column = row + drows[dir_num], column + dcolumns[dir_num]


def end():
    return not in_range(row, column)


cnt = 1
while not end():
    for _ in range(move_num):
        nmap[row][column] = cnt
        cnt += 1

        move()
        
        if end():
            break

    dir_num = (dir_num + 1) % 4
    
    if dir_num == 0 or dir_num == 2:
        move_num += 1

for i in range(n):
    for j in range(n):
        print(nmap[i][j], end = ' ')
    print()