import sys

min_dist = sys.maxsize

n = int(input())
n_list = [int(input()) for _ in range(n)]

dist = 0
for i in range(n):   
    for j in range(n):
        if i == j:
            continue
        elif j < i:
            dist += (n - abs(i - j)) * n_list[j]
        else:
            dist += (j - i) * n_list[j]
           
    min_dist = min(min_dist, dist)
    dist = 0

print(min_dist)