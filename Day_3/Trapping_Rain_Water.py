# Trapping Rain Water
def maxWater(arr, n):
    res=0
    for i in range(1, n-1):
        left=arr[i]
        for j in range(i):
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])
        res = res + (min(left, right)- arr[j])
    return res
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print(maxWater(arr, n))