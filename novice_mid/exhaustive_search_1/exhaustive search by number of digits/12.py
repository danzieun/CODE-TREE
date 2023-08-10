import sys

max_num = -sys.maxsize

n = int(input())
n_list = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            carry = 0

            if n_list[i] % 10 + n_list[j] % 10 + n_list[k] % 10 >= 10:
                carry = 1
            
            if n_list[i] % 100 // 10 + n_list[j] % 100 // 10 + n_list[k] % 100 // 10 >= 10:
                carry = 1
            
            if n_list[i] % 1000 // 100 + n_list[j] % 1000 // 100 + n_list[k] % 1000 // 100 >= 10:
                carry = 1
            
            if n_list[i] % 10000 // 1000 + n_list[j] % 10000 // 1000 + n_list[k] % 10000 // 1000 >= 10:
                carry = 1
            
            if carry == 0:
                max_num = max(max_num, n_list[i] + n_list[j] + n_list[k])

if max_num == -sys.maxsize:
    print(-1)
else:
    print(max_num)