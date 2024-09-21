#7.	Tárolj el két számot egy-egy változóba! Írd ki az osztási maradékukat.
import beolvas



szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()

maradek = szam1 % szam2

print(str(szam1)+"%"+str(szam2)+"="+str(maradek))