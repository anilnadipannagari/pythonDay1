num=int(input())
temp=False
i=1
while i<=num:
    if num%i==0 and i!=1 and i!=num:
        temp=True
    i+=1
if not temp:
    print('it is  prime')