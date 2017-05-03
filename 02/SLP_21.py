# 2.1 Write regular expressions for the following languages.
#     1. the set of all alphabetic strings;
#     2. the set of all lower case alphabetic strings ending in a b;
#     3. the set of all strings from the alphabet a,b such that each
#        a is immediately preceded by and immediately followed by a b;


import re


class SLP_21:

    def __init__(self):

        # 2.1.1
        # Match against English alphabet
        self.ALPHABET_ENGLISH = r'[A-Za-z]+'

        # Unicode alphabet matching against
        # non-[non-word, non-digit, and underscore]
        self.ALPHABET_UNICODE = r'[^\W\d_]+'

        # 2.1.2
        self.ALPHABET_LOWER_LATIN = r'[a-z]+b'

        # 2.1.3
        self.ALPHABET_AB = r'(ab|b)+'


    def match(self, text, mode='ALPHABET_UNICODE'):
        re_pattern = getattr(self, mode)
        return re.match(re_pattern, text)

    def findall(self, text, mode='ALPHABET_UNICODE'):
        re_pattern = getattr(self, mode)
        return re.findall(re_pattern, text)
