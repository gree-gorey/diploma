words = 0

with open('./diff_lm_size/200K', 'r') as f:
    for line in f:
        line = line.rstrip().split()
        words += len(line)

print(words)
