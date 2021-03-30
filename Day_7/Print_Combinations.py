# Printing Combinations
def printAllCombinations(A, result="", n=0):
    if n == len(A):
        print(result[1:])
        return
    for word in A[n]:
        out = result + " " + word 
        printAllCombinations(A, out, n + 1)
A = [["John", "Emma"],
    ["Plays", "Hates", "Watches"],
    ["Cricket", "Soccer", "Chess"]]
printAllCombinations(A)