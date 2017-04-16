import random


with open('./diff_lm_size/all', 'r') as f:
    lines = f.readlines()

s = random.sample(lines, 200000)

with open('./diff_lm_size/200K', 'w') as w:
    w.write(''.join(s))
