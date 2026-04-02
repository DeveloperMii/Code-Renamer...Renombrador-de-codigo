#Libraries
from pathlib import Path

#Variables
Route : str
Option : bool = False
CDigitS : str
CDigitI : int = 1
Files : list = []
FromS : str = "000"
FromI : int = None
UntillS : str = "000"
UntillI : int = None
How_manyS : str = "000"
How_manyI : int = None
Renameable : bool = True

#Route validation
while True:
    Route = input("In which folder are the files located? \nIf it's the same folder as this script, press Enter \n :  ")
    if Route != "" and Route != ".":
        Route = __file__
    if Path(Route).exists():
        print("The chosen route is: " + Route)
        while True:
            match input("If you're not sure, press 1 \nIf you're sure, press 2 \n : "):
                case "1":
                    Option = False
                    break
                case "2":
                    Option = True
                    break
                case _:
                    print("Enter a valid value")   
    else:
        print("The route is invalid")
    if Option:
        break

#Number of digits in the code
while True:
    CDigitS = input("How many digits are in the code?: ")
    if CDigitS.isdigit():
        CDigitI = int(CDigitS)
        break
    else:
        print("Invalid value \nPlease enter a new one")

#File packaging
for i in Path(Route).iterdir():
    Files.append(i)
    for j in range(0,CDigitI):
        if len(i.stem) > j:
            if not i.stem[j].isdigit():
                Files.remove(i)
                break

#From where, to where, and when the change is expected
while FromI == None and UntillI == None and How_manyI == None:
    while True:
        while FromI == None:
            FromS = input("Enter the number you want to start with: ")
            if FromS.isdigit:
                FromI = int(FromS)
            else:
                print("Invalid value \nPlease enter a new one")
        while UntillI == None:
            UntillS = input("Enter the number you want to dial: ")
            if UntillS.isdigit():
                UntillI = int(UntillS)
            else:
                print("Invalid value \nPlease enter a new one")
        if FromI < UntillI:
            break
        else:
            FromI ,UntillI = UntillI, FromI
            break
    while How_manyI == None:
        How_manyS = input("By how much do you want to increase or decrease it?: ")
        if How_manyS[0] == "-":
            if How_manyS[1:].isdigit():
                How_manyI = int(How_manyS[1:]) * -1
        else:
            if How_manyS.isdigit():
                How_manyI = int(How_manyS)
            else:
                print("Invalid value \nPlease enter a new one")

#Funcion de renombrar
def Renombrador(i : int):
    Renameable = True
    if int(Files[i].stem[:CDigitI]) >= FromI and int(Files[i].stem[:CDigitI]) <= UntillI:
        for j in Files:
            if int(Path(j).stem[:CDigitI]) == int(Files[i].stem[:CDigitI]) + How_manyI:
                Renameable = False
                print(str(Files[i].stem) + " It was omitted because " + str(j.stem) + " exists")
                break
        if Renameable and Path(Files[i]).exists():
            print(str(Files[i].stem) + " -> " + str(int(Files[i].stem[:CDigitI]) + How_manyI).zfill(CDigitI) + str(Files[i].name[CDigitI:]))
            Path.rename(Files[i],str(Files[i].parent) + "/" + str(int(Files[i].stem[:CDigitI]) + How_manyI).zfill(CDigitI) + str(Files[i].name[CDigitI:]))
            Files[i] = Path("".zfill(CDigitI)).name

#Variacion del renombrador segun la cantidad de aumento
if How_manyI < 0:
    for i in range(0, len(Files)):
        Renombrador(i)
elif How_manyI > 0:
    for i in range(len(Files) - 1, -1, -1):
        Renombrador(i)
else:
    print("Nothing was done")

input("Process complete \nPress Enter to exit")
