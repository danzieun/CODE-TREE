n, t = map(int, input().split())
r, c, d = map(str, input().split())

dRow, dColumn = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

def in_range(x, y):
    return x > 0 and x <= n and y > 0 and y <= n

r, c = int(r), int(c)
move_dir = mapper[d]
for _ in range(t):
    if in_range(r + dRow[move_dir], c + dColumn[move_dir]):
        r = r + dRow[move_dir]
        c = c + dColumn[move_dir]
    else:
        move_dir = 3 - move_dir
    
print(r, c)