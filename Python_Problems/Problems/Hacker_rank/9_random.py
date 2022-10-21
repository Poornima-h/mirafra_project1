import random

integers=[]
float_num=[]
random_num=[]
for i in range(10):
    a = random.random()
    integers.append(a)
    b = random.randint(0, 20)
    float_num.append(b)
    c = random.uniform(0, 8)
    random_num.append(c)

print(integers,float_num,random_num)

#genrate a sample list
m = random.sample(range(1,10),6)
print(m)