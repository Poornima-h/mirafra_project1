#using builtin function
mylist = [5, 10, 15, 20, 3, 15, 25, 20, 30, 10, 100]
new_list=sorted(mylist)
mylist.sort()
print("sorted list",mylist)

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



#using function
def sort_fun(l):
    new_list = sorted(l)
    l.sort()
    return new_list
print("using fucntion",sort_fun([2,3,221,1,22,1232]))

class myclass:
    def __init__(self,l):
        self.l=l
    def sort_fun(self):
        new_list = sorted(self.l)
        return new_list
myobj=myclass([2,3,221,1,22,1232])
print("using class",myobj.sort_fun())
