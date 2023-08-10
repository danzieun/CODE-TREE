n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
for i in range(n - m + 1):
    if sorted(a[i:i+m]) == sorted(b):
        cnt += 1

print(cnt)