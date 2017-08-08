import re
from collections import Counter

def word_count(sentence):
    words = re.findall('\w+', sentence.lower().replace('_', " "))
    return Counter(words)
