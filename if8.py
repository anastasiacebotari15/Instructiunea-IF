#Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. 
n1=int(input("n1="))
n2=int(input("n1="))
if ((n1%2==0) and (n2%2==0)) :
    if (n1>n2):
        print(n1)
    else:
        print(n2)
if ((n1%2==0) and (n2%2!=0)):
    if(n1>n2):
        print(n1)
if((n1%2!=0) and (n2%2==0)):
    if(n2>n1):
        print(n2)
if((n1%2!=0) and (n2%2!=0)):
    print("nu exista asa numar")