''' start a language '''
from os import path
import json

DATA = '%s/data/' % path.abspath(path.dirname(__file__))
pos = json.loads(open('%s/pos.json' % DATA).read())
cmu_phonemes = json.loads(open('%s/cmu_phonemes.json' % DATA).read())
ipa_phonemes = json.loads(open('%s/ipa_phonemes.json' % DATA).read())
