from pyaspeller import Word

# f = open('./diff_sizes/norm.txt', 'r')
#
# for line in f:
#     for word in line.rstrip().split():
#         sp = Word(word)
#         checked = sp.spellsafe
#         if checked:
#             print(word)
for i in range(10):
    sp = Word('кашаю')
    checked = sp.spellsafe
    print(checked)
