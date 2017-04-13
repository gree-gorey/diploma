# from lxml import etree
import re

RE = re.compile(' +')
RE_DASH = re.compile('-+')

# tree = etree.parse('./corp2.xml')

# sentences = tree.xpath('//source')

cyr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

allowed = ' -' + cyr + cyr.upper()

w = open('rus2.lm', 'w')

f = open('corp2.xml', 'r')

for line in f:
    if 'source' in line:
        sent_text = line.replace('<source>', '').replace('</source>', '')
        sent_words = ''.join([char for char in sent_text if char in allowed])
        if any([char.isalpha() for char in sent_words]):
            sent_words = RE.sub(' ', sent_words)
            sent_words = RE_DASH.sub('-', sent_words)
            # print(sent_words)
            w.write(sent_words + '\n')

w.close()
