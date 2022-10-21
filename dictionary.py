#dictionary - dictionary is a python data type it's having key value pair , keys must be immutable object
# like number ,string and tuple and values can any data type

#dict compression
d={i:i*i for i in range(10)}
print(d)

#sorting a dictionary based on values
d={1:'a',9:'balu',4:'c',3:'assdw'}
l=sorted(d.items(),key=lambda i:i[1])
print(l)

#sorting a dictionary based on keys
d={1:'a',9:'balu',4:'c',3:'assdw'}
l=sorted(d.items(),key=lambda i:i[0])
print(l)


#methods
d={1:'poornima',2:'deepu',4:'fsbbsb',23:'cat',12:'veenu'}

#access element
print(d[1])

##update element
for i in range(10):
    d.update({i:i*i})
print(d)

#remove value
d.pop(1)  # it will remove mentioned element
d.popitem()  # it will remove lat element
print(d)

#delete entire elements
d.clear()
print(d)
