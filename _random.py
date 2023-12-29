#plese do not take file name for random as Random number
#well take random value in a variable 
import random
num=random.randint(10,20)
print(num)
while True:
    a=int(input('Enter the number you are searching for:- '))
    if a==num:
        print('congratulation young man you found the number')
        break
    elif a<num:
        print('your close to the number. elter some higer value')
    elif a>num:
        print("your out of bounds: enter some less value's bro")