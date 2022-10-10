mylist = [5, 10, 15, 20, 3, 15, 25, 20, 30, 10, 100]
#print(set(mylist))

#without using set
result=[]
for x in mylist:
    if x not in result:
        result.append(x)

print("without built in ",result)