""")La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, 
roşie, albastră şi neagră, în această secvenţă. Ionel este pe locul x. Ce culoare va avea 
tricoul pe care-l va primi? """
x=int(input("introduceti numarul locului="))
if x>=1 and x<=25: 
    print("culoarea alba")
if x>25 and x<=50:
    print("culoarea rosie")
if x>50 and x<=75:
    print("culoarea albastra")
if x>=75 and x<100:
    print("culoarea neagra")