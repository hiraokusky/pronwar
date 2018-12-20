import json
from collections import OrderedDict
import pprint
import json
import sys

# prons = sys.argv
prons = ['pron1.json', 'pron2.json','pron3.json','pron4.json']

def war(pron):
    with open(pron, encoding='utf8') as f:
        d_update = json.load(f, object_pairs_hook=OrderedDict)
    synset = {}
    for d in d_update:
        if d['synset'] in synset:
            if len(synset[d['synset']]) < len(d['senses']):
                synset[d['synset']] = { 'lemma': d['lemma'], 'senses': d['senses'] }
        else:
            synset[d['synset']] = { 'lemma': d['lemma'], 'senses': d['senses'] }
    return synset

for pron in prons:
    synset = war(pron)
    print(json.dumps(synset, indent=2, ensure_ascii=False))
