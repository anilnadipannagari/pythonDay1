a=int(input('Enter the numbers you wish to find the fact of numbers:- '))
def fact(c):
    fact=1
    for i in range(1,a+1):
            fact*=i
    print(fact)
fact(a)