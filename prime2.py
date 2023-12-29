num=int(input())
a=False
cout=0
i=1
while i<=num:
    if num%i==0:
        cout+=1
    i+=1
if cout==2:
    a=True
if(a):
    print('prime number')
else:
    print('not a prinme number')