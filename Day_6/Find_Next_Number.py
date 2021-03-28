def findNext(number, n):
    for i in range(n-1, 0, -1):
        if number[i] > number[i-1]:
            break
    if i == 1 and number[i] <= number[i-1]:
        print('Not Possible')
        return
    x = number[i-1]
    smallest = i
    for j in range(i+1, n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j
    number[smallest], number[i-1] = number[i-1], number[smallest]
    x = 0
    for j in range(i):
        x = x*10+number[j]
    number = sorted(number[i:])
    for j in range(n-i):
        x = x*10+number[j]
    print('Number with set of digit is ',x)
    digits = "534976"
    number = map(int, digits)
    findNext(number, len(digits))