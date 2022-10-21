# check the string is palindrome or not

def palindrome(n):
    r=n[::-1]
    if n==r:
        return f'{n} is palindrome'
    else :
        return f'{n} is not a palindrome'
print(palindrome('121'))