import itertools
from pyaspeller import Word

run = 'both'

with open('./0_results/gold', 'r') as f:
    gold_norm = [line.rstrip() for line in f.readlines()]

with open('./0_results/{}'.format(run), 'r') as f:
    csmt_norm = [line.rstrip() for line in f.readlines()]

w = open('./0_results/aligned_{}.tsv'.format(run), 'w')

for gold, csmt in zip(gold_norm, csmt_norm):
    gold_words = gold.split()
    csmt_words = csmt.split()
    csmt_spellcheck = []

    for word in csmt_words:
        sp = Word(word)
        checked = sp.spellsafe
        if checked:
            csmt_spellcheck.append(checked)
        else:
            csmt_spellcheck.append(word)

    # if len(gold_words) == len(csmt_words):
    for line in itertools.zip_longest(
            gold_words, csmt_words, csmt_spellcheck):
        w.write('{}\t{}\t{}\n'.format(*line))

w.close()
