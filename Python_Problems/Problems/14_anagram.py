#anagram number

def anagram(n,m):
    new=''
    for i in n:
        for j in m:
            if i==j:
                new +=i
    if len(new)==len(n) and len(new)==len(m):
        return f'{m}and {n} are anagrams'
    else:
        return f'{m} and {n} are not an anagrams'

print(anagram("silendd","lisend"))