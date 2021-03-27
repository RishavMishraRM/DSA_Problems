from collections import Counter
def find_duplicates(s):
    elements = Counter(s)
    return [k for k,v in elements.items() if v>1]
find_duplicates('Hello')