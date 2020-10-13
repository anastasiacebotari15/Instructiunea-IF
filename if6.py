"""Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, 
să le spună părinţilor toate notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai 
mare notă dintre primele două. Introduceţi noteleluate şi afişaţi notele pe care le va comunica părinţilor. """
n1=int(input("n1:"))
n2=int(input("n2:"))
n3=int(input("n3:"))
if(n3>=8):
    print(n1,n2,n3,sep=" ")
if(n3<8):
    if(n1>n2):
        print(n1)
    if(n2>n1):
        print(n2)