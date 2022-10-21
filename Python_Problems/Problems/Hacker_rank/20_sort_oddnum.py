#How to Sort the Odd in Python
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 !=0 ), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

print(sort_array([2,111,4,33,22]))
#method 2
def method2(source_array):
    result = sorted([l for l in source_array if l % 2 == 1])
    for index, item in enumerate(source_array):
        if item % 2 == 0 :
            result.insert(index, item)
    return result

#method3
def method2(source_array):
    odd = sorted(list(filter(lambda x: x % 2, source_array)))
    l, c = [],
    for i in source_array:
        if i in odd:
            l.append(odd[c])
            c += 1
        else:
            l.append(i)
    return l