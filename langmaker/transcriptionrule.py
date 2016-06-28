''' General description of transcription rules '''
import re

class TranscriptionRules(object):
    ''' a set of inflection rules '''
    rules = []

    def apply_rules(self, word):
        ''' run the appropriate rule on a lemma for given tags '''
        for rule in self.rules:
            word = rule.transform(word)
        return word

    def add_rule(self, pattern, repl):
        ''' create rule objects from signatures '''
        self.rules.append(Rule(pattern, repl))


class Rule(object):
    ''' replace phoneme or pheneme groups with graphemes '''

    def __init__(self, pattern, repl):
        self.pattern = pattern # input regex to match the lemma
        self.repl = repl # replacement rules to modify lemma

    def transform(self, word):
        ''' apply rule to an input lemma '''
        return re.sub(self.pattern, self.repl, word)

