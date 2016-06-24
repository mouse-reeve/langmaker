''' Super general definition of inflection rules '''
import logging
import re

class InflectionRules(object):
    ''' a set of inflection rules '''
    rules = {}

    def __init__(self, signatures=None):
        for signature in signatures:
            self.add_by_signature(signature)

    def apply_rule(self, lemma, tags):
        ''' run the appropriate rule on a lemma for given tags '''
        tags = ','.join(tags)
        try:
            rule = self.rules[tags]
        except KeyError:
            logging.error('No rule found for tags %s', tags)
            return lemma

        return rule.inflect(lemma)

    def add_by_signature(self, signature):
        ''' create rule objects from signatures '''
        tags = signature[0]
        pattern = signature[1]
        repl = signature[2]
        self.rules[','.join(tags)] = Rule(tags, pattern, repl)


class Rule(object):
    ''' string parsing to modify a lemma based on grammatical context tags '''

    def __init__(self, tags, pattern, repl):
        self.tags = tags # array of tags that match this rule
        self.pattern = pattern # input regex to match the lemma
        self.repl = repl # replacement rules to modify lemma

    def inflect(self, lemma):
        ''' apply rule to an input lemma '''
        return re.sub(self.pattern, self.repl, lemma)
