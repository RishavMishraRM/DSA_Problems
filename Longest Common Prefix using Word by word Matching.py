# Longest Common Prefix using Word by word Matching
def commonPrefixUtil(str1, str2):
    result = '';
    n1 = len(str1)
    n2 = len(str2)
    i, j = 0, 0
    while i <= n1 - 1 and j <= n2 - 1:
        if (str1[i] != str2[j]):
            break
        result += str1[i]
        i += 1
        j += 1
    return (result)
def commomPrefix(arr, n):
    prefix = arr[0]
    for i in range(1, n):
        prefix = commonPrefixUtil(prefix, arr[i])
    return (prefix)
arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
n = len(arr)
ans = commomPrefix(arr, n)
if (len(ans)):
    print ("The longest common prefix is",ans);
else:
    print("There is no common prefix")