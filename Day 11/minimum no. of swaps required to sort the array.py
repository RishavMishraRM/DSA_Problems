#minimum no. of swaps required to sort the array
def minSwaps(arr, N):
    ans = 0
    temp = arr.copy()
    temp.sort()
    h = {}
    temp.sort()
    for i in range(n):
        h[arr[i]] = i
    init = 0
    for i in range(n):
        if (arr[i] != temp[i]):
            ans += 1
            init = arr[i]
            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]
            h[init] = h[temp[i]]
            h[temp[i]] = i
    return ans
a = [ 101, 758, 315, 730,472, 619, 460, 479 ]
n = len(a)
minSwaps(a, n)