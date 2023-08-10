n = int(input())
n_list = list(input())

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if n_list[i] == 'C' and n_list[j] == 'O' and n_list[k] == 'W':
                cnt += 1

print(cnt)