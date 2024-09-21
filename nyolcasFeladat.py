#8.	Tárolj el két számot egy-egy változóba! Egy harmadik változóba tárold el a két szám szorzatát, majd írasd ki a képer

import beolvas



szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()

szorzat = szam1 * szam2

print(str(szam1)+"*"+str(szam2)+"="+str(szorzat))
print("Szorzat : "+str(szorzat), end="")