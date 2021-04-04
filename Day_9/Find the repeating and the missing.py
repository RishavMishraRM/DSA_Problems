#Find the repeating and the missing
import math
def findNumbers(arr, n):
		sumN = (n * (n + 1)) / 2;
		sumSqN = (n * (n + 1) * (2 * n + 1)) / 6;
		sum = 0;
		sumSq = 0;
		for i in range(0,n):
			sum = sum + arr[i];
			sumSq = sumSq + (math.pow(arr[i], 2));
		B = (((sumSq - sumSqN) / (sum - sumN)) + sumN - sum) / 2;
		A = sum - sumN + B
		print("A = ",int(A))
		print("B = ",int(B))
arr = [ 1, 2, 2, 3, 4, 5, 6 ]
n = len(arr)
findNumbers(arr, n)