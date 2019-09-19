text = open('input.txt', 'r', encoding='utf8')
a = int(text.readline())
lines = text.readlines()
dick = {}
for line in lines[:a]:
    dick[line.strip().split()[1]] = line.strip().split()[0]
    dick[line.strip().split()[0]] = line.strip().split()[1]
print(dick[lines[a].strip()])
