#Kth smallest number again
def kthSmallest(arr, n, k):
    arr.sort()
    return arr[k-1]
arr = [12, 3, 5, 7, 19]
n = len(arr)
k = 2
kthSmallest(arr, n, k)