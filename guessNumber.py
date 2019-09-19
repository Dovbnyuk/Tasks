n = int(input())
q = set(map(int, range(1, n+1)))

while True:
    ans = input()
    if ans == 'HELP':
        break
    ans = {int(x) for x in ans.split()}
    answer = input()
    if answer == 'YES':
        q &= ans
    else:
        q -= ans
print(*sorted(q))
