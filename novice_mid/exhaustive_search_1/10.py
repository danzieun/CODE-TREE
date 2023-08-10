import sys

max_num = -sys.maxsize

n = int(input())
n_list = list(map(int, input().split()))

for i in range(n - 2):
    for j in range(i + 2, n):
        num_diff = n_list[i] + n_list[j]    
        max_num = max(max_num, num_diff)

print(max_num)