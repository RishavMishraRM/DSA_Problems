#K-th Element of Two Sorted Arrays
def kth (arr1, arr2, m, n, k):
    sorted1 = [0] * (m+n)
    i, j, d = 0, 0, 0
    while(i<m and j<n):
        if (arr1[i] < arr2[j]):
            sorted1[d] = arr1[i]
            i+=1
        else:
            sorted1[d] = arr2[j]
            j += 1
        d += 1
    while(i<m):
        sorted1[d] = arr1[i]
        d+=1
        i+=1
    while(i<n):
        sorted1[d] = arr2[j]
        d+=1
        i+=1
    return sorted1[k-1]
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
kth(arr1, arr2, 5, 4, k)