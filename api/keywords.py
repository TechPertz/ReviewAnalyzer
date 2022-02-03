import spacy

from collections import Counter
from string import punctuation

nlp = spacy.load("en_core_web_lg")

def get_hotwords(text):
    # print(text)
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN'] # 1
    doc = nlp(text.lower()) # 2
    for token in doc:
        # 3
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        # 4
        if(token.pos_ in pos_tag):
            result.append(token.text)
        # 5
    print("keywords done")
    print(Counter(result).most_common(10))
    return Counter(result).most_common(10)

# data = get_hotwords("Poor quality is what you get for looking bargain, it is total waste, as don't feel like to use it.")
# for i in data:
#     print(type(i))


