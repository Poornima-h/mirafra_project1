a='aaabbbccccbbccccaaaajjkkk'
output=''
value=''
for i in a:
    if value=='':
        value=i
        output +=value
    elif value==i:
        continue;
    else:
        value=i
        output +=value
print(output)