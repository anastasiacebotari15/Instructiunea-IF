"""Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. 
Radu este pe locul x în ordinea mediilor. În ce clasa va fi repartizat (A, B, C, D sau E)?.""" 
x=int(input("x="))
if  (x >=1) and (x<=25):
    print("A")
if (x>25) and (x<=50):
    print("B")
if (x>50) and (x<=75):
    print("C")
if (x>75) and (x<=100):
    print("D")
if (x>100) and (x<=125):
    print("E")