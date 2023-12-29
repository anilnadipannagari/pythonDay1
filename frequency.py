a=input('Enter the string:-   ')
feq=input('enter the number you wish to search for:- ')
cout=0
for var in a:
    if var==feq:
        cout+=1        
    if cout==0:
        print('your char is not found') 
        break
print(cout)