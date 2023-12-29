n1=int(input('enter a number1:- '))
n2=int(input('enter a number2:- '))
n3=int(input('enter a number3:- '))
if n1>n2 and n1>n3:
    if n2>n3:
        print('n2 is grate')
    else:
         print('n3 is grate')
elif n2>n1 and n2>n3: 
    if n2>n3:
      print('n2 is grate')  
    else:        
      print('n3 is grate')
elif n3>n1 and n3>n2:
     if n1>n2:
        print('n1 is grate')
     else: 
        print('n2 is grate')
