import os
from lxml import etree
from get_id import get_raw_and_standard_ids


def get_tree(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            open_name = os.path.join(root, filename)
            tree = etree.parse(open_name)
            yield tree


for tree in get_tree('./by/'):
    raw_ids, standard_ids = get_raw_and_standard_ids(tree)

    time_slots = tree.xpath('//TIME_ORDER')[0]

    time_hash = {}

    for time_slot in time_slots:
        time = time_slot.get('TIME_VALUE')
        index = time_slot.get('TIME_SLOT_ID')
        if time not in time_hash:
            time_hash[time] = [index]
        else:
            time_hash[time].append(index)

    raw = []
    for raw_id in raw_ids:
        raw += tree.xpath('//*[@TIER_ID="{}"]//ALIGNABLE_ANNOTATION'.format(raw_id))

    normalized = []
    for norm_id in standard_ids:
        normalized += tree.xpath('//*[@TIER_ID="{}"]//ALIGNABLE_ANNOTATION'.format(norm_id))

    hash_begin_raw = {}
    hash_begin_norm = {}

    for ann in raw:
        begin = ann.get('TIME_SLOT_REF1')
        text = ann[0].text
        hash_begin_raw[begin] = text

    for ann in normalized:
        begin = ann.get('TIME_SLOT_REF1')
        text = ann[0].text
        hash_begin_norm[begin] = text

    aligned = {}

    for explicit_time in time_hash:
        for time_id in time_hash[explicit_time]:
            if time_id in hash_begin_raw:
                if explicit_time not in aligned:
                    aligned[explicit_time] = {'raw': hash_begin_raw[time_id]}
                else:
                    aligned[explicit_time]['raw'] = hash_begin_raw[time_id]

            if time_id in hash_begin_norm:
                if explicit_time not in aligned:
                    aligned[explicit_time] = {'norm': hash_begin_norm[time_id]}
                else:
                    aligned[explicit_time]['norm'] = hash_begin_norm[time_id]

    raw_file = open('by.orig', 'a', encoding='utf-8')
    norm_file = open('by.norm', 'a', encoding='utf-8')

    for pair in aligned.values():
        if len(pair) > 1:
            norm = pair['norm'].replace('\r\n', '').replace('\n', '')
            norm = ' '.join([x.split(':')[1] for x in norm.split('|')])
            raw = pair['raw'].replace('\r\n', '').replace('\n', '')
            raw_file.write(raw + '\n')
            norm_file.write(norm + '\n')

    raw_file.close()
    norm_file.close()
