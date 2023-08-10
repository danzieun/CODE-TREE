n, k = map(int, input().split())
nkmap = [0] * 602

for _ in range(n):
    a, b = map(int, input().split())
    nkmap[b] += a

max_cnt = 0
for i in range(len(nkmap) - k):
    cnt = 0
    for j in range(i - k, i + k + 1):
        cnt += nkmap[j]
    
    max_cnt = max(cnt, max_cnt)

print(max_cnt)