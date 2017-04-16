from Levenshtein import distance
from pymystem3 import Mystem

run = 'both'

m = Mystem()

with open('./0_results/aligned_{}.tsv'.format(run), 'r') as f:
    lines = [line.rstrip().lower() for line in f.readlines()]

words_total = len([line for line in lines if '*' not in line])
lev_csmt = {}
lev_csmt_spell = {}

right_lemma = 0

w = open('accuracy.tsv', 'w')
w.write('tool\tdist\n')

w_spell = open('accuracy_spell.tsv', 'w')
w_spell.write('tool\tdist\n')

i = 0
wrong = 0
total = 0

for line in lines:
    gold, csmt, csmt_spell = line.split('\t')
    gold = gold.replace('ё', 'е')
    csmt = csmt.replace('none', '').replace('ё', 'е')
    csmt_spell = csmt_spell.replace('none', '').replace('ё', 'е')
    if gold != '***':
        if gold != 'none':
            total += 1
            dist = distance(gold, csmt)
            w.write('{}\t{}\n'.format("CSMT", dist))
            if dist not in lev_csmt:
                lev_csmt[dist] = 1
            else:
                lev_csmt[dist] += 1

            dist = distance(gold, csmt_spell)
            if dist:
                wrong += 1
                # print(gold, csmt_spell)
            w_spell.write('{}\t{}\n'.format("CSMT", dist))
            if dist not in lev_csmt_spell:
                lev_csmt_spell[dist] = 1
            else:
                lev_csmt_spell[dist] += 1
            if csmt_spell:
                gold_lemma = m.lemmatize(gold)[0]
                csmt_lemma = m.lemmatize(csmt_spell)[0]
                if gold_lemma == csmt_lemma:
                    right_lemma += 1
                # else:
                    # print(gold, gold_lemma, csmt_spell, csmt_lemma)

for key in lev_csmt:
    lev_csmt[key] = [lev_csmt[key], round(lev_csmt[key]/total*100, 1)]

for key in lev_csmt_spell:
    lev_csmt_spell[key] = [lev_csmt_spell[key], round(lev_csmt_spell[key]/total*100, 1)]

lemma_acc = round(right_lemma/total*100, 1)


print(lev_csmt)
print(lev_csmt_spell)
print('lemma acc: {}'.format(lemma_acc))
print('wrong: {}'.format(wrong))

print('{}\t{}\t{}'.format(lev_csmt[0][1], lev_csmt_spell[0][1], lemma_acc))

right = total - wrong
print('{}\t{}'.format(right, wrong))

w.close()
w_spell.close()
