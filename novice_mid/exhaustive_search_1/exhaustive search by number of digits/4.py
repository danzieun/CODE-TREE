n = int(input())
nmap = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for i in range(n):
    for j in range(n - 2):
        max_sum = max(max_sum, nmap[i][j] + nmap[i][j + 1] + nmap[i][j + 2])

print(max_sum)