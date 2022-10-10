t=("hello",[2,3,4,5])

l=t[1]
for i in range(len(l)):
    value=l[i]+1
    l.remove(l[i])
    l.insert(i,value)

print(l)