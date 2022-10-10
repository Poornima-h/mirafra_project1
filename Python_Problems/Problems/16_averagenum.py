#find the average of numbers in a list

def avgnum(n):
    total=sum(n)
    average=total/len(n)
    return f'average of the list is {round(average,2)}'

print(avgnum([23,45,56]))