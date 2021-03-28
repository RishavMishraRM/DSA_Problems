# Find the first repeated word in string.
from collections import Counter
def firstRepeatingWord(sentence):
    lis = list(sentence.split(" "))
    frequency = Counter(lis)
    for i in lis:
        if(frequency[i] > 1):
            return i
sentence = 'hey there I am here only hey listen'
firstRepeatingWord(sentence)