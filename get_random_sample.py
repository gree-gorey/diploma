import random


with open('./diff_sizes/raw.txt', 'r') as f:
    raw = f.readlines()

with open('./diff_sizes/norm.txt', 'r') as f:
    norm = f.readlines()

pairs = list(zip(raw, norm))

s = random.sample(pairs, 3500)

with open('./diff_sizes/3500_raw.txt', 'w') as w:
    w.write(''.join([x[0] for x in s]))

with open('./diff_sizes/3500_norm.txt', 'w') as w:
    w.write(''.join([x[1] for x in s]))
