import sys
max_num = -sys.maxsize

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

for i in range(n - k + 1):
    num = 0
    for j in range(i, i + k):
        num += n_list[j]
        
    max_num = max(max_num, num)

print(max_num)