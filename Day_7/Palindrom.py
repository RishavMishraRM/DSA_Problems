def isPalindrome(s):
    return s == s[::-1]
s = 'geeks'
a=isPalindrome(s)
if a:
    print("Yes a palindrome")
else:
    print('Not a palindrome')