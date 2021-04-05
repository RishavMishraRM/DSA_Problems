#Searching in an array where adjacent differ by at most k
def search(arr, n, x, k):
    i = 0
    while(i<n):
        if (arr[i] == x):
            return i
        i = i + max(1, int(abs(arr[i] - x) / k))
    print('number is not present!')
    return -1
arr = [2, 4, 5, 7, 7, 6]
x = 6
k = 2
n = len(arr)
search(arr, n, x, k)