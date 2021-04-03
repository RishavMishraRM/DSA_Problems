#Find a Fixed Point in a given array
def linearSearch(arr, n):
    for i in range(n):
        if arr[i] is i:
            return i
    return -1
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
linearSearch(arr, n)