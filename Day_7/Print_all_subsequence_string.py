#Print all subsequence of string
def subsequence(s, binary, length):
    sub = ""
    for j in range(length):
        if(binary&(1<<j)):
            sub +=s[j]
    return sub
def possibleSubsequence(s):
    sorted_subsequence={}
    length = len(s)
    limit = 2**length
    for i in range(1, limit):
        sub = subsequence(s, i, length)
        if len(sub) in sorted_subsequence.keys():
            sorted_subsequence[len(sub)] = \
            tuple(list(sorted_subsequence[len(sub)])+[sub])
        else:
            sorted_subsequence[len(sub)] = [sub]
    for it in sorted_subsequence:
        print("\n",'Subsequences of length', it, 'are:')
        for ii in sorted(set(sorted_subsequence[it])):
            print(ii, end=' ')        
s='abc'
possibleSubsequence(s)