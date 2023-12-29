#WAP a programe to generate CAPTCHA
import random
a=[]
while len(a)<6:
    a+=[chr(random.randint(65,90))]
    a+=[chr(random.randint(97,120))]   
    a+=[str(random.randint(0,9))]
random.shuffle(a)
d=""
for i in a:
    d+=i
print(d)