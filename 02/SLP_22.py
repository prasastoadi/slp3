# 2.2   Write regular expressions for the following languages. By “word”, we mean
#       an alphabetic string separated from other words by whitespace, any relevant
#       punctuation, line breaks, and so forth.
#
#     1.  the set of all strings with two consecutive repeated words (e.g., “Humbert
#         Humbert” and “the the” but not “the bug” or “the big bug”);
#     2.  all strings that start at the beginning of the line with an integer and that
#         end at the end of the line with a word;
#     3.  all strings that have both the word grotto and the word raven in them
#         (but not, e.g., words like grottos that merely contain the word grotto);
#     4.  write a pattern that places the first word of an English sentence in a
#         register. Deal with punctuation.


import re
from string import punctuation

class SLP_22:

    def __init__(self):
        # 2.2.1
        self.REPEATED = r'\b([A-Za-z]+)[\W]+(\1)\b'

        # 2.2.2
        self.END_TO_END_ENGLISH = r'^\d.*[\W]+[A-Za-z]+$'
        self.END_TO_END_UNICODE = r'^\d.*[\W]+[^\W\d_]+$'

        # 2.2.3
        # what is the best patter?
        self.BOTH = r'([\W]?grotto[\W].*[\W]raven[\W]?)|([\W]?raven[\W].*[\W]grotto[\W]?)'

        # 2.2.4
        self.REGISTER = r'[\W_\d]?([A-Za-z]+)[\W_\d]'

    def findall(self, text, mode='REPEATED'):
        re_pattern = getattr(self, mode)
        return re.findall(re_pattern, text)
