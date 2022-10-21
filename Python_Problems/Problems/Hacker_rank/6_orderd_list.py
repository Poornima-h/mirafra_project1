"""
Determine whether the numbers are in ascending order. An array is said to be in
ascending order if there are no two adjacent
integers where the left integer exceeds the right integer in value.
"""

def assnd_ord(l):
    new=sorted(l)
    return new==l
print(assnd_ord([1,23,432,22,111]))