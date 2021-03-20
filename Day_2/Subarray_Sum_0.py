# subarray with sum 0
def subArray(arr, n):
    n_sum = 0
    s = set()
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False
arr = [4, 2, 0, 1, 6]
n = len(arr)
if subArray(arr, n) == True:
    print("True!!!")
else:
    print("False!!!")