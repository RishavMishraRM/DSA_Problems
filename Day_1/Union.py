# Merge two sorted Arrays without extra space
#Union Of an Array
def UnionArray(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            print(arr2[j])
            j += 1
        else:
            print(arr2[j])
            j+=1
            i+=1
    while i<m:
        print(arr1[i])
        i+=1
    while j<n:
        print(arr2[j])
        j+=1
arr1= [1, 2, 4, 5]
arr2= [2, 3, 4, 5]
m = len(arr1)
n = len(arr2)

UnionArray(arr1, arr2, m, n)