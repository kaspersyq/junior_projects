# palindrome number
def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False
n = int(input())
result = isPalindrome(n)
print(result)