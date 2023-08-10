binary = list(map(int, list(input())))
length = len(binary)

max_num = 0
for i in range(length):
    binary[i] = 1 - binary[i]

    num = 0
    for j in range(length):
        num = num * 2 + binary[j]
    
    max_num = max(max_num, num)

    binary[i] = 1 - binary[i]

print(max_num)