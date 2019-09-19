in_file = open('input.txt', 'r', encoding='utf8')
a = []
for i in in_file.read().split('\n'):
    a += i.split()
print(len(set(a)))
