""" “Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele 
unei margarete cu x petale, el (ea) mă iubeşte …."""
p=int(input("numarul de petale:"))
if p>0:
    print("Ma iubeste")
    if p%5==0:
        print("... de loc")
    elif p%5==4:
        print("... la nebunie")
    elif p%5==3:
        print("... cu pasiune")
    elif p%5==2:
        print("... mult")
    else:
        print("... un pic")