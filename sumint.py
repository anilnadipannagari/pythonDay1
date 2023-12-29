a=eval(input('enter the liost of the numbers'))
sum=0
pro=1
if len(a)%2==0:
    for i in a:
        sum+=i
    # i+=1
    print(sum)
else:
    for i in a:
        pro*=i
    # i+=1
    print(pro)

