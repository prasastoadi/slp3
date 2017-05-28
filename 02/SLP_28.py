# 2.8 Implement the MaxMatch algorithm.

def maxMatch(sentence, dictionary):
    """
    Parameters:
        sentence: string; Raw sentence.
        dictionary: set; Set of vocabulary.
    Returns:
        List of segmented strings.
    """
    if not sentence:
        return []
    for i in range(len(sentence),1,-1):
        firstword = sentence[:i]
        remainder = sentence[i:]
        if firstword in dictionary:
            l = [firstword]
            l.extend(maxMatch(remainder, dictionary))
            return l
    # no word was found, so make a one-character word
    firstword = sentence[0]
    remainder = sentence[1:]
    l = [firstword]
    l.extend(maxMatch(remainder, dictionary))
    return l
