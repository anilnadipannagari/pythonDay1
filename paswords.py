import random
otp=''
i=0 
while i<4:
    ran=str(random.randrange(0,9))
    otp=otp+str(ran)
    i+=1
print(otp)