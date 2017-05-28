# 2.9 To test how well your MaxMatch algorithm works, create a test set by
# removing spaces from a set of sentences. Implement the Word Error Rate metric
# (the number of word insertions + deletions + substitutions, divided by the
# length in words of the correct string) and compute the WER for your test set.

from SLP_26 import min_edit_distance
from SLP_28 import maxMatch

def wordErrorRate(raw_sentences,
                  gold_sentences,
                  dictionary,
                  min_edit_distance=min_edit_distance,
                  segmenter=maxMatch):
    """
    Parameters:
        raw_sentences: list; List of raw sentences.
        gold_sentences: list; List of gold sentences.
        dictionary: set; Set of vocabulary.
        distance: function; Function of minimum edit distance.
        segmenter: function; Function of word segmenter.

    Returns:
        Word error rate
    """
    distance = 0
    length = 0

    for r_sentence, g_sentence in zip(raw_sentences, gold_sentences):
        r_segmented = maxMatch(r_sentence, dictionary)
        g_segmented = g_sentence.split()
        length += len(g_segmented)
        distance += min_edit_distance(r_segmented, g_segmented)
    word_error_rate = distance/length
    return word_error_rate

if __name__ == "__main__":
    raw_sentences = ["figureoutwhetherdriveisclosertobriefortodiversandwhattheeditdistanceistoeach",
                 "youmayuseanyversionofdistancethatyoulike"]

    gold_sentences = ["figure out whether drive is closer to brief or to divers and what the edit distance is to each",
                      "you may use any version of distance that you like"]

    dictionary = {'to', 'the', 'and', 'closer', 'any', 'brief',
                  'you', 'is', 'each', 'whether', 'use', 'what', 'edit', 'like',
                  'may', 'drive', 'distance', 'divers', 'version', 'of', 'or',
                  'that', 'out'}

    score = wordErrorRate(raw_sentences,
                          gold_sentences,
                          dictionary,
                          min_edit_distance,
                          maxMatch)

    print(score)
