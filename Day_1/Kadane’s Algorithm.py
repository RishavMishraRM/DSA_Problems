# Kadane’s Algorithm
def maxsubarray(a, size):
    max_so_far = a[0]
    curr_max = a[0]
    for i in range(1, size):
        curr_max = max(a[i], curr_max+a[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far
a = [1, 2, 4, -1, -2, -8]
print("Maximum Sub Array : ",maxsubarray(a, len(a)))