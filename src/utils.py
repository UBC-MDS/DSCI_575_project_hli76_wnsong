import re


def simple_tokenize(text):
    """tokenize document"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return text.split()