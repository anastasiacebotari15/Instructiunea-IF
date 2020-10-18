"""La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr 
de boabe de porumb. Cele care nu pot fi împărţite vor fi primite de curcanul Clapon. Să se 
spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va afişa numărul de 
boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de 
găini, iar dupa aceea numărul de boabe de porumb."""
g=int(input("Numarul de gaini="))
p=int(input("Numarul de boabe de porumb="))
c=p//g
d=p-c*g
if c<d:
    print("Curcanul a primit mai mult cu",d-c,"boabe")
if c>d:
    print("Gainile au primit mai mult cu",c-d,"boabe")
else:
    print("Egalitate")