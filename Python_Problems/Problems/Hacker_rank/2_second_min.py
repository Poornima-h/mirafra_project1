#using builtin function
mylist = [5, 10, 15, 20, 3, 15, 25, 20, 30, 10, 100]
new_list=sorted(mylist)
mylist.sort()
print("sorted list",mylist)
print("second min",mylist[1])
print("second max",mylist[-2])

#without builtin
s_list=[]
for i in range(len(mylist)):
    min=mylist[0]
    for j in mylist:
        if min > j:
            min = j
    s_list.append(min)
    mylist.remove(min)
print("sorted list",s_list)
print("second min",s_list[1])
print("second max",s_list[-2])


