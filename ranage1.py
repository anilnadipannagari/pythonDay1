num=int(input('enter the  number'))
sum=0
for i in range(1,num):
    if(num % i==0):
        sum+=i
    i+=1
if sum==num:
    print('perfect number')
else:
    print('not a perfect num') 