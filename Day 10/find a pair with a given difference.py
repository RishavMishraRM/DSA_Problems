#find a pair with a given difference
def findpair(arr, n):
    size = len(arr)
    i, j = 0, 1
    while i < size and j < size:
        if i != j and arr[j]-arr[i] == n:
            print('Pair Found(',arr[i], ' ,',arr[j], ')')
            return True
        elif arr[j] - arr[i] < n:
            j += 1
        else:
            i += 1
    print('No Pair Found')
    return False
arr = [1, 8, 30, 40, 100]
n = 60
findpair(arr, n)