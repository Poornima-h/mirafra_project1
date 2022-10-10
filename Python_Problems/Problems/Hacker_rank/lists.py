'''
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''
l=[]
N = int(input())

for i in range(N):
    k=input().split(" ")
    if k[0]=='insert':
       l.insert(int(k[1]),int(k[2]))
    if k[0]=='remove':
       l.remove(int(k[1]))
    if k[0]=='append':
       l.append(int(k[1]))
    if k[0]=='sort':
       l.sort()
    if k[0]=='pop':
       l.pop()
    if k[0]=='reverse':
       l.reverse()
    if k[0] =='print':
        print(l)
