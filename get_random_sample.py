import random


with open('./diff_lm_size/raw.txt', 'r') as f:
    raw = f.readlines()

with open('./diff_lm_size/norm.txt', 'r') as f:
    norm = f.readlines()

pairs = list(zip(raw, norm))

s = random.sample(pairs, 300)

with open('./diff_lm_size/300_raw.txt', 'w') as w:
    w.write(''.join([x[0] for x in s]))

with open('./diff_lm_size/300_norm.txt', 'w') as w:
    w.write(''.join([x[1] for x in s]))
