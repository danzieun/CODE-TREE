n = int(input())
n_list = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        length = 0
        sum_val = 0
        for k in range(i, j + 1):
            length = j - i + 1
            sum_val += n_list[k]

        if (sum_val / length) in n_list[i:j+1]:
            cnt += 1

print(cnt)