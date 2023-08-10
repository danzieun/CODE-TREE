n, k = map(int, input().split())
nmap = ['A'] * 10000

for _ in range(n):
    location, alpha = map(str, input().split())
    nmap[int(location)] = alpha

max_score = 0
for i in range(1, len(nmap) - k):
    score = 0
    for j in range(i, i + k + 1):
        if nmap[j] == 'G':
            score += 1
        elif nmap[j] == 'H':
            score += 2
        
    max_score = max(max_score, score)

print(max_score)