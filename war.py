import json
from collections import OrderedDict
import pprint
import json
import sys

pron = sys.argv[1]

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

synset = war(pron)
print(json.dumps(synset, indent=2, ensure_ascii=False))
