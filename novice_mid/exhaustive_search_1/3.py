n = int(input())
n_list = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if n_list[i] <= n_list[j] and n_list[j] <= n_list[k]:
                cnt += 1

print(cnt)