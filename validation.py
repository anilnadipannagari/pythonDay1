num=(input('enter the input numbers: '))
password=''
upper=False
lower=False
special=False
number=False
space=True
#assigning all the vaalues to the false and cheking condition at last
if len(num)>=8:
    for i in num:
        if 'A'<=i<='Z':
         upper=True
        elif 'a'<=i<='z':
         lower=True
        elif '0'<=i<='9':
         number=True
        elif i !=' ':
         special=True
        elif i==' ':
           space=False
if((upper==True)and(lower==True)and( number==True)and( special==True)and(space==True)):
        print('pasword is Valid and your password:- ',end='')
        print(num)
else:
    print('enter the valid input')
