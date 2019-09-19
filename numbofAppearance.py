inputfile = open('input.txt', 'r', encoding='utf8')
lines = []

for line in inputfile:
    oneline = line.strip().split()
    lines.append(oneline)
countDict = {}
for i in range(len(lines)):
    for j in lines[i]:
        countDict[j] = countDict.get(j, 0) + 1
        print(int(countDict[j]) - 1, end=' ')
