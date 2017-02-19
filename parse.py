from lxml import etree

tree = etree.parse('RuPS-SEBR-14-01-03.eaf')

time_slots = tree.xpath('//TIME_ORDER')[0]

time_hash = {}

for time_slot in time_slots:
    time = time_slot.get('TIME_VALUE')
    index = time_slot.get('TIME_SLOT_ID')
    if time not in time_hash:
        time_hash[time] = [index]
    else:
        time_hash[time].append(index)
    # print(time_slot.get('TIME_VALUE'))
    # break

# raw = tree.xpath('//*[@TIER_ID="ru_i_mj"]//ALIGNABLE_ANNOTATION')
# raw += tree.xpath('//*[@TIER_ID="ru_n_bz"]//ALIGNABLE_ANNOTATION')
# raw = tree.xpath('//*[@TIER_ID="ru_i_mt"]//ALIGNABLE_ANNOTATION')
# raw += tree.xpath('//*[@TIER_ID="ru_n_na"]//ALIGNABLE_ANNOTATION')
# raw = tree.xpath('//*[@TIER_ID="ru_i_mt"]//ALIGNABLE_ANNOTATION')
# raw += tree.xpath('//*[@TIER_ID="ru_n_nn"]//ALIGNABLE_ANNOTATION')
raw = tree.xpath('//*[@TIER_ID="ru_i_mj"]//ALIGNABLE_ANNOTATION')
raw += tree.xpath('//*[@TIER_ID="ru_n_št"]//ALIGNABLE_ANNOTATION')

# normalized = tree.xpath('//*[@TIER_ID="ru_i_mj_standartization"]//ALIGNABLE_ANNOTATION')
# normalized += tree.xpath('//*[@TIER_ID="ru_n_bz_standartization"]//ALIGNABLE_ANNOTATION')
# normalized = tree.xpath('//*[@TIER_ID="ru_i_mt_standartization"]//ALIGNABLE_ANNOTATION')
# normalized += tree.xpath('//*[@TIER_ID="ru_n_na_standartization"]//ALIGNABLE_ANNOTATION')
# normalized = tree.xpath('//*[@TIER_ID="ru_i_mt_standartization"]//ALIGNABLE_ANNOTATION')
# normalized += tree.xpath('//*[@TIER_ID="ru_n_nn_standartization"]//ALIGNABLE_ANNOTATION')
normalized = tree.xpath('//*[@TIER_ID="ru_i_mj_standartization"]//ALIGNABLE_ANNOTATION')
normalized += tree.xpath('//*[@TIER_ID="ru_n_št_standartization"]//ALIGNABLE_ANNOTATION')

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

# print(hash_ann_by_begin_id)

# print(time_hash)

aligned = {}

for explicit_time in time_hash:
    for time_id in time_hash[explicit_time]:
        # print(time_id)
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

raw_file = open('raw_one.txt', 'w', encoding='utf-8')
norm_file = open('norm_one.txt', 'w', encoding='utf-8')

for pair in aligned.values():
    if len(pair) > 1:
        norm = pair['norm'].replace('\r\n', '').replace('\n', '')
        norm = ' '.join([x.split(':')[1] for x in norm.split('|')])
        raw = pair['raw'].replace('\r\n', '').replace('\n', '')
        # print('{} --> {}'.format(pair['raw'], norm))
        raw_file.write(raw + '\n')
        norm_file.write(norm + '\n')

raw_file.close()
norm_file.close()
