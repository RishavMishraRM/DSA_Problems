#Count triplet with sum smaller than a given value 
def countTriplet(arr, n, sum):
    ans = 0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] < sum):
                    ans += 1
    return ans
arr = [5, 1, 3, 4, 7]
n = len(arr)
sum = 12
countTriplet(arr, n, sum)