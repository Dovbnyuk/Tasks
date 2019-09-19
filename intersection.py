w = set(map(int, input().split()))
q = set(map(int, input().split()))
print(*sorted(w.intersection(q)))
