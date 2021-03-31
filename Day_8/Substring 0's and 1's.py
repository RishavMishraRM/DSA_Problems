# Substring 0's and 1's
def maxSubStr(str, n):
    count0 = 0
    count1 = 0
    cnt = 0
    for i in range(n):
        if str[i] == "0":
            count0 += 1
        else:
            count1 += 1
        if count0 == count1:
            cnt+=1
    if count0 != count1:
        return -1
    return cnt
str = "0100110101"
n = len(str)
print(maxSubStr(str, n))