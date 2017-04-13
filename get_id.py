from lxml import etree
import re


def get_raw_and_standard_ids(tree):
    tiers = tree.xpath('//TIER')

    ids = []

    for tier in tiers:
        tier_id = tier.get('TIER_ID')
        if tier_id not in ids:
            ids.append(tier_id)

    RE = re.compile(r'(.+)_standartization', flags=re.U)

    standard_ids = []
    raw_ids = []

    for tier_id in ids:
        m = RE.match(tier_id)
        if m:
            raw_ids.append(m.group(1))
            standard_ids.append(m.group())

    return raw_ids, standard_ids


def main():
    tree = etree.parse('./todo/RuPS-SEBR-14-01-03.eaf')
