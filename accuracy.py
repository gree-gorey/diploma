from Levenshtein import distance

with open('./0_results/aligned.tsv', 'r') as f:
    lines = [line.rstrip().lower() for line in f.readlines()]

words_total = len([line for line in lines if '*' not in line])
lev_csmt = {}
lev_csmt_spell = {}

w = open('accuracy.tsv', 'w')
w.write('tool\tdist\n')

w_spell = open('accuracy_spell.tsv', 'w')
w_spell.write('tool\tdist\n')

i = 0

for line in lines:
    # i+=1
    # print(i)
    # print(line)
    gold, csmt, csmt_spell = line.split('\t')
    csmt = csmt.replace('none', '')
    csmt_spell = csmt_spell.replace('none', '')
    if gold != '***':
        if gold != 'none':
            dist = distance(gold, csmt)
            w.write('{}\t{}\n'.format("CSMT", dist))
            if dist not in lev_csmt:
                lev_csmt[dist] = 1
            else:
                lev_csmt[dist] += 1

            dist = distance(gold, csmt_spell)
            w_spell.write('{}\t{}\n'.format("CSMT", dist))
            if dist not in lev_csmt_spell:
                lev_csmt_spell[dist] = 1
            else:
                lev_csmt_spell[dist] += 1

for key in lev_csmt:
    lev_csmt[key] = [lev_csmt[key], round(lev_csmt[key]/words_total*100, 1)]

for key in lev_csmt_spell:
    lev_csmt_spell[key] = [lev_csmt_spell[key], round(lev_csmt_spell[key]/words_total*100, 1)]

print(i)
print(lev_csmt)
print(lev_csmt_spell)

w.close()
w_spell.close()
