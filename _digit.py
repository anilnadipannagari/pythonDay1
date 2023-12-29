def strcount():
    st1=input('Enter the Inpu')
    cout=0
    for i in st1:
        if '0'<= i<='9':
            cout+=1
    print(cout)
strcount()