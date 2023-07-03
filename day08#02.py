x = list(input())
dict = {}
for i in x:
if i in dict:
dict[i] =dict[i]+1
else:
dict[i] = 1
print(dict)
