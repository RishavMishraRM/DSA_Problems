# Maximum Product Subarray
def maxProductSubarray(arr, n):
    result = arr[0]
    for i in range(n):
        mul = arr[i]
        for j in range(i+1, n):
            result= max(result, mul)
            mul *= arr[j]
        result = max(result, mul)
    return result
arr = [6, -3, -10, 0, 2]
n = len(arr)
maxProductSubarray(arr, n)