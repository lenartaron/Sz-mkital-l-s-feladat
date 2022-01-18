#----IMPORT----
#Be importáljuk a dolgokat
import random
from re import T
from tkinter import*
#----HÁTTÉRBEN FUTÓ ÉRTÉKEK----
code1 = random.randint(1,3)
code2 = random.randint(4,6)
code3 = random.randint(7,9)


#----BEMONDÓ----
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("Rádió - Üdvözlöm önt a \"Legyen szabad\" játékunkban. A feladata nem más mint kijutni ebből a szobából. A ")
print("kijutáshoz oldja meg a fejtörőket amikért kodókat kap a tovább jutáshoz míg végül ki nem jut a szobából.")
print("A gombok segítségével megvizsgálatja a bútorokat amiken széfeket,dobozokat vagy akár papírokat is találhat.")
print("A válaszok/kodók beírását a \"TERMINAL\"-ba lehet.")
print("Nagyon fontos, hogy az \"ajtó\" gombot csak a legvégén használja. Csak egyszer lehet próbálkozni az ajtó kodjával.")
print("Minden gombot csak egyszer lehet használni.")
print("Szabályok:")
print("1.Ne nézze meg a megoldásokat!")
print("2.Nem ér netről lesni!")
print("3.Érezze jól magát!")


#----COMMAND----
#Itt a commandnak megadott csoportott fejthetjük ki
def wardrobe():
    print()
    print()
    print("Egy lakattal le van zárva az ajtaja és van egy felirat felette.")
    print("\"Pici szálfa, villog, serceg, nem ég tovább csak egy percet.\"")
    print("Vajon mi lehet ez?")
    #Ismétel (ha elrontja a felhasználó akkor is úrja próbálhatja)
    while True:
        megold = input("Megoldás: ")
        #Ha sikerült eltalálnia akkor tovább jut
        if megold == "Gyufa" or megold == "gyufa":
            print()
            print()
            print("Sikerült!")
            print("Egy szám van bele égetve az aljába.")
            print("Egy", code1, "szám.")
            break
        #Ha nem sikerül akkor újból meg kell próbálnia    
        else:
            print("Nem nyílik, biztos valami más lesz az.")
            print()
            print()
            print("\"Pici szálfa, villog, serceg, nem ég tovább csak egy percet.\"")  
            
#Itt a commandnak megadott csoportott fejthetjük ki    
def shelf():
    print()
    print()
    print("Egy kis lelakatolt doboz van itt és a falba van vésve egy szöveg.")
    print("\"Vízben úszik, de nem hal, embert cipel a hátán.\"")
    #Ismétel (ha elrontja a felhasználó akkor is úrja próbálhatja)
    while True:
        megold2 = input("Megoldás: ")
        #Ha sikerült eltalálnia akkor tovább jut
        if megold2 == "Hajo" or megold2 == "hajo" or megold2 == "Hajó" or megold2 == "hajó":
            print()
            print()
            print("Siker!")
            print("Egy hajó van benne.")
            print("Ennek a(z)", code2, " számú hajó.")
            break
        #Ha nem sikerül akkor újból meg kell próbálnia 
        else:
            print("Nem nyílik.")
            print()
            print()
            print("\"Vízben úszik, de nem hal, embert cipel a hátán.\"")
            
#Itt a commandnak megadott csoportott fejthetjük ki
def vv():
    print()
    print()
    print("Egy kis fiókot találtam fölötte egy fejtörő látható.")
    print("\"Négy keréken szaladgál, repül, mint a gyors madár.Szíve helyén motor dohog, fékezz, megáll, továbbrobog.\"")
    #Ismétel (ha elrontja a felhasználó akkor is úrja próbálhatja)
    while True:
        megold1 = input("Megoldás: ")
        #Ha sikerült eltalálnia akkor tovább jut
        if megold1 == "Auto" or megold1 == "auto" or megold1 == "Autó" or megold1 == "autó" or megold1 == "Kocsi" or megold1 == "kocsi":
            print()
            print()
            print("Kinyilt!")
            print("egy kis papír volt a fiók alján.")
            print("Kis autók vannak benne és az összes", code3, "számot viseli.")
            break
        #Ha nem sikerül akkor újból meg kell próbálnia 
        else:
            print("nem jó.")
            print()
            print()
            print("\"Négy keréken szaladgál, repül, mint a gyors madár.Szíve helyén motor dohog, fékezz, megáll, továbbrobog.\"")

#Itt a commandnak megadott csoportott fejthetjük ki
def open():
    print()
    print()
    print("3 zár van rajta, mindegyik fellett egy-egy felirat.")
    print("Nézzük meg a legfelső zárat!")
    print("Egy felirat van itt is.")
    print("\"Adja meg a Szekrényben talált számot.\"")
    cod1 = int(input("Szám: "))
    #Ha sikerült eltalálnia akkor tovább jut
    if cod1 == code1:
        print()
        print()
        print("Sikerült!")
        print("Nézzük a második zárat!")
        print("\"Adja meg a Polcnál talált számot.\"")
        cod2 = int(input("Szám: "))
        #Ha sikerült eltalálnia akkor tovább jut
        if cod2 == code2:
            print()
            print()
            print("Ez is sikerült!")
            print("Nézzük az utolsó zárat!")
            print("\"Adja meg az asztalnál talált számot.\"")
            cod3 = int(input("Szám: "))
            #Ha sikerült eltalálnia akkor tovább jut
            if cod3 == code3:
                print()
                print()
                print("Minden zárrat sikerükt feloldani!")
                print("Rádió - Gratulálunk sikerült kijutnod a szobából!")
            #Ha nem sikerül akkor leáll a program  
            else:
                print()
                print()
                print("Nem sikerült.")
                print("Rádió - A szoba bezárta önmagát.")
        #Ha nem sikerül akkor leáll a program
        else:
            print()
            print()
            print("Nem sikerült.")
            print("Rádió - A szoba bezárta önmagát.")
    #Ha nem sikerül akkor leáll a program
    else:
        print()
        print()
        print("Nem sikerült.")
        print("Rádió - A szoba bezárta önmagát.")
            
            
#----CSOPORT----
#A gomb csoportja amivel később dolgozhatunk
root = Tk()

#----GOMBOK----
#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button = Button(root, text="Szekrény", command = wardrobe)
#Itt a gomb kinézeti beállításai
button.config(font = ("Ink Free", 25, "bold"))
button.config(bg = "#787878")
button.config(fg = "#ffffff")
#A gomb elhelyezkedése
button.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
cc = Button(root, text="Polc", command = shelf)
#Itt a gomb kinézeti beállításai
cc.config(font = ("Ink Free", 35, "bold"))
cc.config(bg = "#787878")
cc.config(fg = "#ffffff")
#A gomb elhelyezkedése
cc.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
ce = Button(root, text="Asztal", command = vv)
#Itt a gomb kinézeti beállításai
ce.config(font=("Ink Free", 30, "bold"))
ce.config(bg = "#787878")
button.config(fg = "#ffffff")
#A gomb elhelyezkedése
ce.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
co = Button(root, text="Ajtó", command = open)
#Itt a gomb kinézeti beállításai
co.config(font=("Ink Free", 27, "bold"))
co.config(bg = "#787878")
button.config(fg = "#ffffff")
#A gomb elhelyezkedése
co.pack(side = TOP)


#----MEGJELENÍTÉS----
#Megjeleniti a gombokat/gombot
root.mainloop()