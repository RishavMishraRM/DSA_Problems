# Minimum number of jumps to reach end *
def minjump(arr, l, h):
    if (h == l):
        return 0 
    if (arr[l] == 0):
        return float('inf')
    min = float('inf')
    for i in range(l+1, h+1):
        if (i < l+arr[l]+1):
            jumps = minjump(arr, i, h)
            if (jumps != float('inf') and jumps + 1 < min):
                min = jumps + 1
    return min
arr = [1, 2, 5, 6, 2, 6, 3, 9, 8]
n = len(arr)
print('Minimum number of jumps to reach end is ', minjump(arr, 0, n-1))