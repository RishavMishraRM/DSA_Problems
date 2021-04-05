# Product Array Puzzle
def productArray(arr, n):
	if n == 1:
		print(0)
		return
	i, temp = 1, 1
	prod = [1 for i in range(n)]
	for i in range(n):
		prod[i] = temp
		temp *= arr[i]
	temp = 1
	for i in range(n - 1, -1, -1):
		prod[i] *= temp
		temp *= arr[i]
	for i in range(n):
		print(prod[i], end = " ")
	return
arr = [10, 3, 5, 6, 2]
n = len(arr)
print("The product array is: ")
productArray(arr, n)