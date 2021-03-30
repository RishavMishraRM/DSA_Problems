# Number of flips to make binary string alternate
def flip( ch):
    return '1' if (ch == '0') else '0'
def getFlipWithStartingCharcter(str, expected):
    flipCount = 0
    for i in range(len( str)):
        if (str[i] != expected):
            flipCount += 1
        expected = flip(expected)
    return flipCount
def minFlipToMakeStringAlternate(str):
    return min(getFlipWithStartingCharcter(str, '0'),
            getFlipWithStartingCharcter(str, '1'))
str = "0001010111"
minFlipToMakeStringAlternate(str)