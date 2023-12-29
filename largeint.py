# num=eval(input('enter the list of the numbers :- '))
a=[1,9,11,23,65,78,43]
out1=a[0]
out2=a[0]
for var in a:
    if out1 < var:
        out1=out2
        out1=var
    elif out2<var:
        out2=var
print(out2,out1)