w = list(map(int, input().split()))
g = set()
for i in w:
    if i in g:
        print('YES')
    else:
        print('NO')
        g.add(i)
