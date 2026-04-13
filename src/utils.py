import re
from nltk.corpus import stopwords


STOP_WORDS = set(stopwords.words("english"))


def simple_tokenize(text):
    """
    Tokenize input text into a list of normalized word tokens.

    This function lowercases the input text, removes non-alphanumeric
    characters (except hyphens), splits into whitespace tokens, and
    removes English stopwords.

    Parameters
    ----------
    text : str
        Input raw text string to be tokenized.

    Returns
    -------
    list of str
        A list of cleaned tokens after normalization and stopword removal.

    Notes
    -----
    - Converts text to lowercase.
    - Removes characters outside [a-z0-9\\s-].
    - Filters out NLTK English stopwords.
    - Drops empty tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    tokens = text.split()
    tokens = [
        t
        for t in tokens
        if t and t not in STOP_WORDS  # remove stop words and empty token
    ]
    return tokens
