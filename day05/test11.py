score = [
    [90,80,100,92],
    [91,81,100,91],
    [92,82,100,92],
    [93,83,100,93],
    [94,84,100,94],
]

total = 0
cnt = 0
for data in score:
    sum = 0
    for i in data:
        sum += i
    print('%d, %.2f' % (sum, sum / len(data)))
    total += sum
    cnt += len(data)
print('%d, %.2f' % (total, total / cnt))
