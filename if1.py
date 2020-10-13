#Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj.
e1=int(input("e1:"))
p1=int(input("p1:"))
e2=int(input("e2:"))
p2=int(input("p2:"))
e3=int(input("e3:"))
p3=int(input("p3:"))
if ((p1>p2) and (p1>p3)):
  print(e1)
if ((p2>p1) and (p2>p3)):
  print(e2)
if ((p3>p1) and (p3>p2)):
  print(p3)
