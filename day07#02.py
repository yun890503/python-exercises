a=input ("input your number:")

if a.isdigit():
a=int(a)
b=1
for i in range(1,a+1):
b=i*b
print(b)

