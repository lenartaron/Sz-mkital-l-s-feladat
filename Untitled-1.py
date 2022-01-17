#----IMPORT----
#Be importáljuk a dolgokat
import random
from re import T
from tkinter import*
tt
#----HÁTTÉRBEN FUTÓ ÉRTÉKEK----
n = 0
num = 0



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
print("Üdvözlöm önt a \"Legyen szabad\" játékunkban. A feladata nem más mint kijutni ebből a szobából. A ")
print("kijutáshoz oldja meg a fejtörőket amikért kodókat kap a tovább jutáshoz míg végül ki nem jut a szobából.")
print("A gombok segítségével megvizsgálatja a bútorokat amiken széfeket,dobozokat vagy akár papírokat is találhat.")
print("A válaszok/kodók beírását a \"TERMINAL\"-ba lehet.")
print("Szabályok:")
print("1.Ne nézze meg a megoldásokat")
print("2.Nem ér netről lesni")
print("3.Érezze jól magát")

#----COMMAND----
#Itt a commandnak megadott csoportott fejthetjük ki
def open():
    #Ismétel (ha elrontja a felhasználó akkor is úrja próbálhatja)
    while True:
        megold1 = input("Megoldás: ")
        #Ha sikerült eltalálnia akkor tovább jut
        if megold1 == "auto" or megold1 == "Auto" or megold1 == "autó" or megold1 == "Autó" or megold1 == "kocsi" or megold1 == "Kocsi":
            print("kinyílt!")
            print("Megint egy papír van benne")
            code1 = random.randint(1,3)
            print("Egy", code1, "van ráírva. Elteszem hátha még jó lesz valamire")    
            break
        
        else:
            print("Nem jó")
            print()
            print()
            print("\"Négy keréken szaladgál, repül, mint a gyors madár. Szíve helyén motor dohog, fékezz, megáll, továbbrobog\"")

def wardrobe():
    print()
    print()
    print("Egy lakattal le van zárva az ajtaja és van egy felirat felette")
    print("\"Pici szálfa, villog, serceg, nem ég tovább csak egy percet\"")
    print("Vajon mi lehet ez?")
    #Ismétel (ha elrontja a felhasználó akkor is úrja próbálhatja)
    while True:
        megold = input("Megoldás: ")
        #Ha sikerült eltalálnia akkor tovább jut
        if megold == "Gyufa" or megold == "gyufa":
            print()
            print()
            print("Sikerült!")
            print("Egy kodós aktatáska van itt és egy papír")
            print("\"Négy keréken szaladgál, repül, mint a gyors madár. Szíve helyén motor dohog, fékezz, megáll, továbbrobog\"")
            num = n + 1
            break
        #Ha nem sikerül akkor újból meg kell próbálnia    
        else:
            print("Nem nyílik, biztos valami más lesz az.")
            print()
            print()
            print("\"Pici szálfa, villog, serceg, nem ég tovább csak egy percet.\"")  
    
def shelf():
    print()
    print()
    print("Egy kis lelakatolt doboz van itt és a falba van vésve egy szöveg.")
    print("\"Vízben úszik, de nem hal, embert cipel a hátán\"")
    while True:
        megold2 = input("Megoldás: ")
        if megold2 == "Hajo" or megold2 == "hajo" or megold2 == "Hajó" or megold2 == "hajó":
            print("")
        else:
            print("")
            print()
            print()
            print("\"Vízben úszik, de nem hal, embert cipel a hátán\"")

def vv():
    print()
    print()
    print("")

#----CSOPORT----
#A gomb csoportjai amivel később dolgozhatunk
root = Tk("Megnézhető dolgok")
taska = Tk("Táska")

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
cc.config(font = ("Ink Free", 30, "bold"))
cc.config(bg = "#787878")
cc.config(fg = "#ffffff")
#A gomb elhelyezkedése
cc.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
ce = Button(root, text="vv", command = vv)
#Itt a gomb kinézeti beállításai
ce.config(font=("Ink Free", 27, "bold"))
ce.config(bg = "#787878")
button.config(fg = "#ffffff")
#A gomb elhelyezkedése
ce.pack(side = TOP)

#----MEGJELENÍTÉS----
#Megjeleniti a gombokat/gombot
root.mainloop()


#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
taska = Button(taska, text = "Táska nyitása", command = open)
#Itt a gomb kinézeti beállításai
taska.config(font = ("Ink Free", 27, "bold"))
taska.config(bg="#787878")
taska.config(fg = "#ffffff")
#A gomb elhelyezkedése
taska.pack(side = TOP)

#----MEGJELENÍTÉS----
#Megjeleniti a gombokat/gombot
taska.mainloop()