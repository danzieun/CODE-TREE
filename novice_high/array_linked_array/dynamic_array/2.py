n = int(input())
n_list = []

for _ in range(n):
    a = list(map(str, input().split()))

    if a[0] == 'push_back':
        n_list.append(int(a[1]))
    elif a[0] == 'pop_back':
        n_list.pop()
    elif a[0] == 'size':
        print(len(n_list))
    elif a[0] == 'get':
        print(n_list[int(a[1]) - 1])