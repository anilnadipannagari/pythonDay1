#finding the mutilples of 7 which are devisible by 7
cour=0
i=1
while True:
    if i>100:
        print('reached 100')
        break
    else:
        if(i%7==0):
            cour+=1
            print('7->',i)
       
    i=i+1
print('number of multiples 7 till 100 is: ',cour)
    