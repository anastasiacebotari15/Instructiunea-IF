"""Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi."""
zc=int(input("ziua curenta :"))
lc=int(input("luna curenta :"))
ac=int(input("anul curent :"))
zn=int(input("ziua nasterii :"))
ln=int(input("luna nasterii :"))
an=int(input("anul nasterii :"))
if(lc>ln):
    print((ac-an)+1)
else:
    print(ac-an)
if(zc>zn):
    print((ac-an)+1)
else:
    print(ac-an)
if(ac>an):
    print(ac-an)