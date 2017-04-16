words = 0

with open('./diff_gold_size/300_norm.txt', 'r') as f:
    for line in f:
        line = line.rstrip().split()
        words += len(line)

print(words)
