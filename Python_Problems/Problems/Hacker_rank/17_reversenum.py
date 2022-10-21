# reverse number

def reverse_num(n):
    n=str(n)
    m=n[::-1]
    return f'{int(n)} is reversed to {int(m)}'

print(reverse_num(int(input("enter the number:"))))
