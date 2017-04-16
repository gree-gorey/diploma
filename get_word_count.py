words = 0

with open('./diff_lm_type/lm_both_old', 'r') as f:
    for line in f:
        line = line.rstrip().split()
        words += len(line)

print(words)
