words = 0

with open('./by_wd/by.norm', 'r') as f:
    for line in f:
        line = line.rstrip().split()
        words += len(line)

print(words)
