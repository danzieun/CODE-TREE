import sys

n = int(input())
checkpoint = [list(map(int, input().split())) for _ in range(n)]

min_num = sys.maxsize
for i in range(1, n - 1):
    num = 0
    idx = 0

    for j in range(1, n):
        if i == j:
            continue
        num += abs(checkpoint[idx][0] - checkpoint[j][0]) + abs(checkpoint[idx][1] - checkpoint[j][1])
        idx = j
    
    min_num = min(min_num, num)

print(min_num)