n = int(input())
lines = []
for i in range(n):
    oneline = input().strip().split()
    lines.append(oneline)
word = input()
dick = {}
for i in range(len(lines)):
    for p in range(len(lines[i])):
        if p == 0:
            dick[lines[i][0]] = lines[i][1]
        else:
            dick[lines[i][1]] = lines[i][0]
for k in dick:
    if word == k:
        print(dick[k])
