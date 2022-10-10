#using dictionary comprension
mylist = [5, 10, 15, 20, 3, 15, 25, 20, 30, 10, 100]
d={x:mylist.count(x) for x in mylist}
print(d)

#using for loop
d2={}
for i in mylist:
    if i in d2:
        d2[i]++1
    else:
        d2[i]=1
print(d2)

