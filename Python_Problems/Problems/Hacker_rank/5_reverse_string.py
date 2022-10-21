"""
Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
Make sure that if it is a negative number you keep the negative in the front (-123 becomes -321)
"""
def reverse_int(n):
    n=str(n)
    strg=''
    if n[0]=='-':
        strg += '-'
        strg += n[:0:-1]
    else:
        strg=n[::-1]
    return int(strg)
print(reverse_int(-12355))

