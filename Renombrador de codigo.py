#Librerias
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

#Validacion de ruta
while True:
    Route = input("En que ruta carpeta estan los archivos \n Si es la misma en la que esta este script pulse enter \n :  ")
    if Route != "" and Route != ".":
        Route = __file__
    if Path(Route).exists():
        print("La ruta escogida es: " + Route)
        while True:
            match input("Si no esta seguro presione 1 \n En caso de estar seguro presione 2 \n : "):
                case "1":
                    Option = False
                    break
                case "2":
                    Option = True
                    break
                case _:
                    print("Ingrese un valor valido")   
    else:
        print("La ruta es invalida")
    if Option:
        break

#Cantidad de digitos del codigo
while True:
    CDigitS = input("¿De cuantos digitos es el codigo?: ")
    if CDigitS.isdigit():
        CDigitI = int(CDigitS)
        break
    else:
        print("Valor invalido \nIngrese uno nuevo")

#Empaquetado de archivos
for i in Path(Route).iterdir():
    Files.append(i)
    for j in range(0,CDigitI):
        if len(i.stem) > j:
            if not i.stem[j].isdigit():
                Files.remove(i)
                break

#Desde donde, Hasta donde y en cuanto se espera cambiar
while FromI == None and UntillI == None and How_manyI == None:
    while True:
        while FromI == None:
            FromS = input("Ingrese desde que numero quiere iniciar: ")
            if FromS.isdigit:
                FromI = int(FromS)
            else:
                print("Valor invalido \nIngrese uno nuevo")
        while UntillI == None:
            UntillS = input("Ingrese hasta que numero quiere llegar: ")
            if UntillS.isdigit():
                UntillI = int(UntillS)
            else:
                print("Valor invalido \nIngrese uno nuevo")
        if FromI < UntillI:
            break
        else:
            FromI = None
            UntillI = None
            print("El valor hasta donde va a llegar no puede ser mayor que desde donde empieza")
    while How_manyI == None:
        How_manyS = input("¿En cuanto lo quiere aumentar o restar?: ")
        if How_manyS[0] == "-":
            if How_manyS[1:].isdigit():
                How_manyI = int(How_manyS[1:]) * -1
        else:
            if How_manyS.isdigit():
                How_manyI = int(How_manyS)
            else:
                print("Valor invalido \nIngrese uno nuevo")

#Funcion de renombrar
def Renombrador(i : int):
    Renameable = True
    if int(Files[i].stem[:CDigitI]) >= FromI and int(Files[i].stem[:CDigitI]) <= UntillI:
        for j in Files:
            if int(Path(j).stem[:CDigitI]) == int(Files[i].stem[:CDigitI]) + How_manyI:
                Renameable = False
                print(str(Files[i].stem) + " se omitio porque " + str(j.stem) + " Existe")
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
    print("No se hizo nada")

input("proceso Terminado pulse enter para salir")
