n = int(input())
n_list = [list(map(str, input().split())) for _ in range(n)]

mapper = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

row, column = 0, 0
dRows, dColumns = [0, 1, 0, -1], [1, 0, -1, 0]

time, result = 0, -1

for n_li in n_list:
    for _ in range(int(n_li[1])):
        time += 1
        row, column = row + dRows[mapper[n_li[0]]], column + dColumns[mapper[n_li[0]]]
        if row == 0 and column == 0:
            result = time
            break
    if result != -1:
        break

print(result)