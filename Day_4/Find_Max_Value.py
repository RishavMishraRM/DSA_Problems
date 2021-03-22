# findMaxValue
N = 5
def findMaxValue(mat):
    maxValue = 0
    for a in range(N-1):
        for b in range(N-1):
            for d in range(a+1, N):
                for e in range(b+1, N):
                    if maxValue < int(mat[d][e] - mat[a][b]):
                        maxValue = int(mat[d][e] - mat[a][b]);
    return maxValue
mat = [[ 1, 2, -1, -4, -20 ], 
       [ -8, -3, 4, 2, 1 ], 
       [ 3, 8, 6, 1, 3 ], 
       [ -4, -1, 1, 7, -6 ], 
       [ 0, -4, 10, -5, 1 ]]; 
findMaxValue(mat)