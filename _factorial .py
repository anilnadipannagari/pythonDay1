import random
fact=1
result=[]
for i in range(1,11):
    for j in range(1,i+1):
        fact*=i
    result+=[fact]
print(result)