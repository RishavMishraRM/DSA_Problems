#Minimize the maximum difference between the heights
def getMinDiff(arr, n, k):
    if(n==1):
        return 0
    arr.sort()
    ans = arr[n-1]-arr[0]
    small = arr[0]+k
    big = arr[n-1]-k
    if (small > big):
        small, big = big, small
    for i in range(1, n-1):
        subtract = arr[i]-k
        add = arr[i]+k
        if (subtract >= small or add <= big):
            continue
        if (big-subtract <= small+add):
            small = subtract
        else:
            big = add
    return min(ans, big-small)
arr=[ 50, 6]
n=len(arr)
k=10
print(getMinDiff(arr, n, k))