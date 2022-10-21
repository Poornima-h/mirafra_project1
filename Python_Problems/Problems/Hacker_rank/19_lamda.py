""" lamda function"""
l=[lambda args=x:args*2 for x in range(10)]

for i in l:
    print(i(),end=" ")

print(" ")
#elif condition
new=lambda a,b: a if(a<b)else b
print(new(1,3))

#Python Lambda with Multiple statements

List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)

#filter using lambda function

l=[2,32,1,32,22,12,44,33,123]
l2=list(filter(lambda x:x%2==0,l))
print("filtered",l2)

# Filter all people having age more than 18, using lambda and filter() function

# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
age_list=list(filter(lambda x:x>18,ages))
print(age_list)



#Using lambda() Function with map()
#Multiply all elements of a list by 2 using lambda and map() function

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
square=list(map(lambda x:x*2,li))
print("mapping",square)
