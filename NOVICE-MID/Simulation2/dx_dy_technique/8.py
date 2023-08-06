n, m = map(int, input().split())
n_list = [[0] * n for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

drows, dcolumns = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(m):
    cnt = 0
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    n_list[r][c] = 1

    for i in range(4):
        dr, dc = r + drows[i], c + dcolumns[i]
        if in_range(dr, dc) and n_list[dr][dc] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)