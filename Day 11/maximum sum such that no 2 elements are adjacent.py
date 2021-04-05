#maximum sum such that no 2 elements are adjacent
def find_max_sum(arr):
    incl, excl = 0, 0
    for i in arr:
        new_excl = excl if excl>incl else incl
        incl = excl + i
        excl = new_excl
    return (excl if excl>incl else incl)
arr = [5, 5, 10, 100, 10, 5]
find_max_sum(arr)