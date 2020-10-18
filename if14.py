"""Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit 
al n-lea. În a câta căsuţă se va afla?"""
x=int(input("introduceti x="))
c=x//4
if c==0:
    print("1 casuta")
if c>0:
    print("A",c+1,"-a casuta")