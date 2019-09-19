inputfile = open('input.txt', 'r', encoding='utf8')
lines = []
dic = {}
for i in inputfile:
    lines.append(i.strip().split(' '))
for elem in lines:
    for i in elem:
        dic[i] = dic.get(i, 0) + 1
maxf = max(dic.values())
more_freq = []
for k in dic.items():
    if k[1] == maxf:
        more_freq.append(k)
print(min(more_freq)[0])
