r, c = map(int, input().split())
rcmap = [list(map(str, input().split())) for _ in range(r)]

cnt = 0
for i in range(1, r):
    for j in range(1, c):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                if rcmap[0][0] != rcmap[i][j] and rcmap[i][j] != rcmap[k][l] and rcmap[k][l] != rcmap[r - 1][c - 1]:
                    cnt += 1

print(cnt)