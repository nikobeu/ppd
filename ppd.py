import os
import sys

script_path = os.path.abspath(sys.argv[0])

parent_directory = os.path.dirname(script_path)

nstart = (rf"start {str(parent_directory)}\start_ppd.cmd")

if not os.path.exists(rf"{str(parent_directory)}\start_ppd.cmd"):
    file = open("start_ppd.cmd", "a")
    file.write(f"@echo off\n\n")
    file.write(rf"python {str(parent_directory)}\ppd.py")
    file.close()
    os.system(nstart)
    exit()

else:

    idiotentest = True
    file = open("start_ppd.cmd", "r")
    idiotl1 = file.readline()
    idiotl2 = file.readline()
    idiotl3 = file.readline()
    file.close()
    if not idiotl1 == "@echo off\n":
        idiotentest = False
    elif not idiotl2 == "\n":
        idiotentest = False
    elif not idiotl3 == (rf"python {str(parent_directory)}\ppd.py"):
        idiotentest = False

    if idiotentest == False:
        file = open("start_ppd.cmd", "w")
        file.write(f"@echo off\n\n")
        file.write(rf"python {str(parent_directory)}\ppd.py")
        file.close()
        os.system(nstart)
        exit()
    else:
        liste = False
        print("wenn du stoppen willst drücke zu dem zeitpunkt x und wenn du irgendwann neustarten willst drücke n")
        sauswahl = input("willst du deín ergebnis speichern ? JA/Nein :").lower()
        if sauswahl == "x":
            print("abgebrochen")
            input("zum schließen irgendeine taste drücken")
            exit()
        elif sauswahl == "n":
            print("neustart")
            os.system(nstart)
            exit()
        elif sauswahl == "ja":
            liste = True
        else:
            liste = False
        auswahl = input(
            "drücke z zum ziel berechnen oder b zum berechnen vom endergebnis oder t für eine anzahl an tagen : ").lower()

        if sauswahl == "x":
            print("abgebrochen")
            input("zum schließen irgendeine taste drücken")
            exit()
        elif sauswahl == "n":
            print("neustart")
            os.system(nstart)
            exit()
        elif auswahl == "b":

            print("du bist im berechnen bereich")

            start = input("start angeben : ")

            tage = input("tage eingeben : ")

            ppd = input("prozent pro tag eingeben : ")

            if start == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif start == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif tage == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif tage == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif ppd == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ppd == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()

            else:
                tagerechn1 = float(tage) + 1

                listename = f"von {str(start)} mit {str(ppd)} % für {str(tage)} tage liste.txt"

                if liste == True:
                    if os.path.exists(listename):
                        print("genau diese datei gibt es bereits")
                        liste = False
                    else:
                        file = open(str(listename), "a", encoding='utf-8')
                        file.write(f"von {str(start)} mit {str(ppd)} % für {str(tage)} tage : \n")
                        file.close()
                else:
                    print("du hast dich gegen die liste entschieden")

                tagedone = 0
                startr = 0

                profitber = (float(ppd) / 100) + 1
                while float(tagedone) < float(tagerechn1):
                    startr = round(float(start), 2)
                    if liste == True:
                        file = open(str(listename), "a")
                        file.write(f"tag {str(tagedone)} : {str(startr)} \n")
                        file.close()
                    start = float(start) * float(profitber)
                    tagedone += 1

                print(str(startr), "bei", str(ppd), "%")

                neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                if neustart == "n":
                    os.system(nstart)
                    exit()
                else:
                    input("zum schließen irgendeine taste drücken")
                    exit()

        elif auswahl == "z":
            print("du bist im zeit such bereich")
            start = input("start angeben : ")
            ziel = input("Ziel eingeben : ")
            ppd = input("wass ist ein realistischer profit in % pro tag : ")
            tagen = 1
            startr = 0

            if start == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif start == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ziel == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ziel == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif ppd == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ppd == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            else:
                listename = f"von {str(start)} mit {str(ppd)} % bis {str(ziel)} liste.txt"

                if liste == True:
                    if os.path.exists(listename):
                        print("genau diese datei gibt es bereits")
                        liste = False
                    else:
                        file = open(str(listename), "a")
                        file.write(f"von {str(start)} mit {str(ppd)} % bis {str(ziel)} : \n")
                        file.write(f"tag : 0 : {str(start)} \n")
                        file.close()
                else:
                    print("du hast dich gegen die liste entschieden")

                if start == "0":
                    print("der startpunkt ist zu klein!")
                else:
                    rechn1 = (float(ppd) / 100) + 1

                    while float(start) < float(ziel):
                        startr = round(float(start), 2)
                        start = float(start) * float(rechn1)
                        if liste == True:
                            file = open(str(listename), "a")
                            file.write(f"tag : {str(tagen)} : {str(startr)} \n")
                            file.close()
                        tagen += 1
                    if float(start) > float(ziel):
                        print("")

                        if liste == True:
                            file = open(str(listename), "a")
                            file.write(f"tag : {str(tagen)} : {str(ziel)} \n")
                            file.close()

                    print("es braucht ", str(tagen), "tag(e) bis du ", str(ziel), "erreicht hast")

                    neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                    if neustart == "n":
                        os.system(nstart)
                        exit()
                    else:
                        input("zum schließen irgendeine taste drücken")
                        exit()

        elif auswahl == "t":
            print("du bist im tage bereich")
            start = input("startpunkt eingeben : ")
            ziel = input("gib dein ziel ein : ")
            tage = input("wie viele tage hast du zeit : ")

            if start == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif start == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif tage == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif tage == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif ziel == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ziel == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            else:

                listename = f"von {str(start)} zu {str(ziel)} in {str(tage)} tagen liste.txt"
                tagerechn1 = float(tage) + 1
                mindtage = 1

                if float(tage) < float(mindtage):
                    print("du hast zu wenig tage eingegeben bitte versuche es erneut")
                    tage = input("tage wiederholen : ")
                else:
                    print("")

                A = float(start)
                E = float(ziel)
                T = float(tage)
                # rechnung, do not touch !!!
                P = ((E / A) ** (1 / T)) - 1

                proz = float(P) * 100
                prozr = round(proz, 2)

                if liste == True:
                    if os.path.exists(listename):
                        print("genau diese datei gibt es bereits")
                        liste = False
                    else:
                        file = open(str(listename), "a")
                        file.write(f"von {str(start)} zu {str(ziel)} in {str(tage)} benötigt : {str(prozr)} % \n")
                        file.write(f"das Kapital würde so aussehen : \n")
                        file.close()

                    tagedone = 0
                    startr = 0

                    profitber = (float(proz) / 100) + 1
                    while float(tagedone) < float(tagerechn1):
                        startr = round(float(start), 2)
                        if liste == True:
                            file = open(str(listename), "a")
                            file.write(f"tag {str(tagedone)} : {str(startr)} \n")
                            file.close()
                        start = float(start) * float(profitber)
                        tagedone += 1

                print("es braucht ca.", str(prozr), "% pro tag")

                neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                if neustart == "n":
                    os.system(nstart)
                    exit()
                else:
                    input("zum schließen irgendeine taste drücken")
                    exit()

        else:
            print("fehler bitte drücke nur z oder t oder b")
            neustart = input("drücke n zum erneuten versuchen : ").lower()
            if neustart == "n":
                os.system(nstart)
                exit()
            else:
                input("zum schließen irgendeine taste drücken")
                exit()

input("durchgerutscht bitte debuggen")
