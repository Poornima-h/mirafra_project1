# check wheether the number is prime number or not

def primenum(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count +=1
    if count==2 or n==1:
        return f"{n} is a prime number , {count}"
    else:
        return f"{n} is not a prime number, {count}"

print(primenum(int(input("enter number: "))))


#Sequence of prime number
def seq_primenum(n):
    l=[1,]
    for k in range(1,n):
        count=0
        for i in range(1,k+1):
            if k%i==0:
                count +=1
        if count==2 or n==1:
            l.append(k)
    return l

print(seq_primenum(int(input("enter number: "))))
