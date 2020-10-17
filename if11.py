"""Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul 
fiecăruia unul dintre cuvintele PAR sau IMPAR."""
n1=int(input("n1="))
n2=int(input("n2="))
n3=int(input("n3="))
if (n1%2==0):
    print(n1, "PAR", sep="   ")
else:
    print(n1, "IMPAR", sep="   ")
if (n2%2==0):
    print(n2, "PAR", sep="   ")
else:
    print(n2, "IMPAR", sep="   ")
if (n3%2==0):
    print(n3, "PAR", sep="   ")
else:
    print(n3, "IMPAR", sep="   ")