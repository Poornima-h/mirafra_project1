'''
1.Write a program to create a new string made of an input string’s first, middle, and last character.
'''
a=input("enter the string : ")
print(a[0]+a[len(a)//2]+a[-1])

'''
#2 Create a string made of the middle three characters
'''
m=len(a)//2
print(a[m-1]+a[m]+a[m+1])

'''
#3 Append new string in the middle of a given string
'''
new=input("enter the new string :")
print(a[0:m]+new+a[m:])

'''
 #4 Create a new string made of the first, middle, and last characters of each input string
'''
print(a[0]+new[0]+a[len(a)//2]+new[len(new)//2]+a[-1]+new[-1])

'''
#5 Arrange string characters such that lowercase letters should come first
'''
lower=[i for i in a if i.islower()]
upper=[i for i in a if i.isupper()]
print(''.join(lower)+''.join(upper))