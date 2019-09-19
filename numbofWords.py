counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(len(list(counter[word] - 1) - sum(list(counter[word] - 1))))

