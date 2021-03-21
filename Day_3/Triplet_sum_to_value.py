# Triplet that sum to a given value
def findthreenum(arr, arr_size, sum):
    for i in range(0, arr_size-2):
        for j in range(i+1, arr_size-1):
            for k in range(j+1, arr_size):
                if arr[i]+arr[j]+arr[k]==sum:
                    print(arr[i], arr[j], arr[k])
                    return True
                else:
                    return False
arr = [1, 4, 45, 6, 10, 8]
sum = 50
arr_size = len(arr)
findthreenum(arr, arr_size, sum)