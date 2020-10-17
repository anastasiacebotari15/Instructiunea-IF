"""Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt 
bile de două dimensiuni: mari şi mici. Să se afişeze câte bile sunt în total pe 
masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici
sau cele mari, afişând numărul lor. De ce culoare sunt bilele cele mai numeroase? 
Precizaţi numărul lor."""
a1a=int(input("a1a="))
a1r=int(input("a1r="))
a1v=int(input("a1v="))
b1a=int(input("b1a="))
b1r=int(input("b1r="))
b1v=int(input("b1v="))
#a= bile mici
#b= bile mari
Mari=b1a+b1r+b1v
Mici=a1a+a1r+a1v
if(Mari>Mici):
    print("Mari=", Mari)
else:
    print("Mici=", Mici)
a=a1a+b1a
r=a1r+b1r
v=a1v+b1v
if((a>r) and (a>v)):
    print("albe=", a1)
if((r>a) and (r>v)):
    print("rosii=", r)
if((v>a) and (v>r)):
    print("verzi=", v)