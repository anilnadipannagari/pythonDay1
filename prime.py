num=int(input())
cout=0
i=1
while i <= num:
    if(num%i==0):
        cout+=1
    i+=1
if(cout==2):
    print("prime numer")
else:
    print("not a prime numer")