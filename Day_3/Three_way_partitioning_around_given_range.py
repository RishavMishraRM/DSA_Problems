# Three way partitioning of an array around a given range
def threeWayPartition(arr, n, low, high):
    start = 0
    end = n-1
    i = 0
    while i <= end:
        if arr[i] < low:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            i += 1
            start += 1
        elif arr[i] > high:
            temp = arr[i]
            arr[i] = arr[end]
            arr[end] = temp
            end -= 1
        else:
            i += 1
arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
n = len(arr)
threeWayPartition(arr, n, 10, 20)
for i in range(n):
    print(arr[i], end=' ')