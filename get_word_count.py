words = 0

with open('./diff_sizes/1500_norm.txt', 'r') as f:
    for line in f:
        line = line.rstrip().split()
        words += len(line)

print(words)
