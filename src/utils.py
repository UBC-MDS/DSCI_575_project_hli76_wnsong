import re
from nltk.corpus import stopwords


STOP_WORDS = set(stopwords.words("english"))


def simple_tokenize(text):
    """tokenize document"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    tokens = text.split()
    tokens = [
        t for t in tokens
        if t and t not in STOP_WORDS # remove stop words and empty token
    ]
    return tokens
