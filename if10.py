"""La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr 
de boabe de porumb. Cele care nu pot fi împărţite vor fi primite de curcanul Clapon. Să se 
spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va afişa numărul de 
boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de 
găini, iar dupa aceea numărul de boabe de porumb."""
ng=int(input("numarul de gaini la ferma=")) 
nbp=int(input("numarul de boabe de porumb="))
if nbp % ng==0:
    print("egalitate")
if nbp % ng !=0:
    print("Curcanul Clapon primeste", nbp%ng)