#Librerias
from pathlib import Path

#Variables
Ruta : str
Opcion : bool = False
CDigitS : str
CDigitI : int = 1
Archivos : list = []
DesdeS : str = "000"
DesdeI : int = None
HastaS : str = "000"
HastaI : int = None
CuantoS : str = "000"
CuantoI : int = None
Renombrable : bool = True

#Validacion de ruta
while True:
    Ruta = input("En que ruta carpeta estan los archivos:  ")
    if Path(Ruta).exists() and Ruta != "" and Ruta != ".":
        print("La ruta escogida es: " + Ruta)
        while True:
            match input("Si no esta seguro presione 1 en caso de estar seguro presione 2: "):
                case "1":
                    Opcion = False
                    break
                case "2":
                    Opcion = True
                    break
                case _:
                    print("Ingrese un valor valido")   
    else:
        print("La ruta es invalida")
    if Opcion:
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
for i in Path(Ruta).iterdir():
    Archivos.append(i)
    for j in range(0,CDigitI):
        if len(i.stem) > j:
            if not i.stem[j].isdigit():
                Archivos.remove(i)
                break

#Desde donde, Hasta donde y en cuanto se espera cambiar
while DesdeI == None and HastaI == None and CuantoI == None:
    while True:
        while DesdeI == None:
            DesdeS = input("Ingrese desde que numero quiere iniciar: ")
            if DesdeS.isdigit:
                DesdeI = int(DesdeS)
            else:
                print("Valor invalido \nIngrese uno nuevo")
        while HastaI == None:
            HastaS = input("Ingrese hasta que numero quiere llegar: ")
            if HastaS.isdigit():
                HastaI = int(HastaS)
            else:
                print("Valor invalido \nIngrese uno nuevo")
        if DesdeI < HastaI:
            break
        else:
            DesdeI = None
            HastaI = None
            print("El valor hasta donde va a llegar no puede ser mayor que desde donde empieza")
    while CuantoI == None:
        CuantoS = input("¿En cuanto lo quiere aumentar o restar?: ")
        if CuantoS[0] == "-":
            if CuantoS[1:].isdigit():
                CuantoI = int(CuantoS[1:]) * -1
        else:
            if CuantoS.isdigit():
                CuantoI = int(CuantoS)
            else:
                print("Valor invalido \nIngrese uno nuevo")

#Funcion de renombrar
def Renombrador(i : int):
    Renombrable = True
    if int(Archivos[i].stem[:CDigitI]) >= DesdeI and int(Archivos[i].stem[:CDigitI]) <= HastaI:
        for j in Archivos:
            if int(Path(j).stem[:CDigitI]) == int(Archivos[i].stem[:CDigitI]) + CuantoI:
                Renombrable = False
                print(str(Archivos[i].stem) + " se omitio porque " + str(j.stem) + " Existe")
                break
        if Renombrable and Path(Archivos[i]).exists():
            print(str(Archivos[i].stem) + " -> " + str(int(Archivos[i].stem[:CDigitI]) + CuantoI).zfill(CDigitI) + str(Archivos[i].name[CDigitI:]))
            Path.rename(Archivos[i],str(Archivos[i].parent) + "/" + str(int(Archivos[i].stem[:CDigitI]) + CuantoI).zfill(CDigitI) + str(Archivos[i].name[CDigitI:]))
            Archivos[i] = Path("".zfill(CDigitI)).name

#Variacion del renombrador segun la cantidad de aumento
if CuantoI < 0:
    for i in range(0, len(Archivos)):
        Renombrador(i)
elif CuantoI > 0:
    for i in range(len(Archivos) - 1, -1, -1):
        Renombrador(i)
else:
    print("No se hizo nada")

input("proceso Terminado pulse enter para salir")
