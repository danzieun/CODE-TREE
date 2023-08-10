import sys

min_sum = sys.maxsize

n = int(input())
n_list = list(map(int, input().split()))

for i in range(n):

    sum_diff = 0
    for j in range(n):
        sum_diff += n_list[j] * abs(i - j)
    
    min_sum = min(min_sum, sum_diff)

print(min_sum)