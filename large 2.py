num=(input('enter the input numbers: '))
if type(num)==int:
    num1=num[0]
    num2=num[0]
    for i in num:
        if i<num:
            num1=num2
            num1=i
        elif num2<i:
            num2=i
print(num2,num1)