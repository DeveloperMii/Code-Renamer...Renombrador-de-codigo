# Code Renamer / Renombrador de codigo

![Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)

## Table of content / Tabla de contenido

- [English](#english)
    - [Description](#description)
    - [Features](#features)
    - [How to run it?](#how-to-run-it)
    - [How does the program work?](#how-does-the-program-work)
    - [Requirements](#requirements)
    - [Recommendations](#recommendations)
    - [Limitations](#limitations)
    - [License](#license)
    - [Contributions](#contributions)
    - [Version](#version)

- [Español](#español)
    - [Descripcion](#descripcion)
    - [Caracteristicas](#caracteristicas)
    - [¿Como ejecutarlo?](#como-ejecutarlo)
    - [¿Como funciona el programa?](#como-funciona-el-programa)
    - [Requisitos](#requisitos)
    - [Recomendaciones](#recomendaciones)
    - [Limitaciones](#limitaciones)
    - [Licencia](#licencia)
    - [Contribuciones](#contribuciones)
    - [Versión](#versión)

## English

> Note: English is not my first language, so there may be minor translations errors

### Description

This Python script was originally created as a supplement to the “File Mover by Name,” but it is not required for its use; it is merely a recommendation.
You do not need to pass the data to it via the terminal, as it does not support that; instead, it requests the information incrementally. In total, it requires the location, range, and modification type.
Its main purpose is to work alongside that program to help manage large numbers of files, a task that would be quite tedious to do manually.
This program searches for a numeric code of a length specified by the user and modifies the number by adding or subtracting.
If another file uses that same numeric code, it sends a message stating that it was skipped and which file caused the omission.
Essentially, its function is to modify the numeric code by adding to or subtracting from it so that files can be added or removed in between without having to modify each one manually.

### Features

- Allows for quick modification of the alphabetical order of files
- Allows you to work with user-defined ranges
- Has no code length limitations (except for 32 or 64-bit limitations)
- Requires only Python to be installed

### How to run it?

#### Python File Option (.py)

1. Download the program from the release section.
2. Install Python 3.10 or later.
3. You can run the file from the terminal or by double-clicking it.
4. Enter the requested information and press Enter to continue.

#### Windows Executable (.exe) Option

1. Download the program from the release section.
2. You can run the file from the terminal or by double-clicking it.
3. Enter the requested information and press Enter to continue.

### How does the program work?

The program runs in the terminal and prompts the user for information step by step:

1. It asks the user for the path to the files to be modified
2. It asks the user for the number of digits in the code
3. It groups all the paths into a single array only if the specified number of digits consists solely of digits
> For this function to work, the digit code must come first; anything else can follow
4. Asks how much will be added to or subtracted from that code; if subtracting, simply type a minus sign before the number
5. Depending on whether you are adding or subtracting, it will choose an order in which to work, but this does not affect the final result—only the processing order and the console output
6. Start the renaming process one by one, checking if the file exists or if there is another file with that number to avoid errors

### Requirements

#### Python File Option (.py)

- Python 3.10 or higher
- pip
- Operating System
    - Windows 10 or higher / Linux (compatible with Python 3.10 or higher) / Mac (compatible with Python 3.10 or higher)

#### Windows Executable (.exe) Option

- Windows 10 or 11

### Recommendations

1. We recommend creating the numerical code manually at the beginning to ensure it is in the required order, and then using this program to maintain that order when adding or removing files.
2. We recommend leaving a space between the code and the rest of the filename, both for aesthetic reasons and to prevent errors.
3. As a safety measure, if no numbers are added to or removed from the code, the program will skip the renaming step.

### Limitations

1. The program will not recognize files without the code and cannot expand it.
2. If any of the first characters that should correspond to the numeric code are not numbers, the program will omit them.

### License

This project is licensed under the MIT License.

### Contributions

Pull Requests are not currently accepted.
If you find a bug or wish to suggest an improvement, open an issue explaining the issue.
The project may be freely modified via a fork, but such versions will not be associated with the official version

### Version

Current version: 1.0 

## Español

> Esta es la versión original del README

### Descripcion

Este script de Python que nació como un complemento para el "Movedor de archivos por nombre" pero no es necesario para su uso solo es una recomendación.
No es necesario pasarle los datos por la terminal, ya que no los soporta el los va pidiendo poco a poco en total son ubicación, rango, y tipo de modificación.
Su utilidad principal está ligada a aquel programa para ayudar al control de cantidades grandes de archivos donde de manera manual sería bastante tediosa.
Este programa busca un código numérico de longitud especificada por el usuario y modifica el número sumando o restando.
En caso de que otro archivo use ese mismo código numérico manda un mensaje diciendo que se omitió y cuál fue el archivo que ocasiono esa omisión.
En esencia su función es modificar el código numérico sumándole o restándole para poder añadir o eliminar archivos entre medias sin tener que modificar cada uno a mano.

### Caracteristicas

- Permite una modificación rápida del orden alfabético de los archivos
- Permite trabajar en rangos definidos por el usuario
- No tiene limitantes en la longitud del código (A excepción de las limitantes de los 32 o 64 bits)
- Solo requiere Python instalado

### ¿Como ejecutarlo?

#### Opcion Archivo de Python (.py)

1. Descargar el programa desde el apartado de release.
2. Instalar Python 3.10 o superior.
3. Puedes ejecutar el archivo desde la terminal o dándole doble clic.
4. Escribir los datos que pida y pulsar enter para continuar.

#### Opcion Ejecutable de Windows (.exe)

1. Descargar el programa desde el apartado de release.
2. Puedes ejecutar el archivo desde la terminal o dándole doble clic.
3. Escribir los datos que pida y pulsar enter para continuar.

### ¿Como funciona el programa?

El programa se ejecuta en terminal y pide datos poco a poco:

1. Pide al usuario la ruta donde están los archivos a modificar
2. Pide al usuario la cantidad de dígitos que tiene el código
3. Empaqueta todas las rutas en un array solo si dentro de la cantidad de dígitos especificados solo hay dígitos
> Para que haga esta función el código de dígitos debe ir al inicio después puede ir cualquier cosa
4. Pregunta cuanto se le va a adicionar o sustraer a ese código en caso de querer sustraer solo debe escribir un menos antes del número
5. Dependiendo de si se adiciona o sustrae va a escoger un orden en el cual trabajar, pero no afecta el resultado final solo el orden de proceso y la salida de la consola
6. Empieza el proceso de renombrado uno por uno verificando si existe o si hay algún otro archivo con ese número para evitar errores

### Requisitos

#### Opcion Archivo de Python (.py)

- Python 3.10 o superior
- pip
- Sistema operativo
    - Windows 10 o superior / Linux (compatible con Python 3.10 o superior) / Mac (compatible con Python 3.10 o superior)

#### Opcion Ejecutable de Windows (.exe)

- Windows 10 o 11

### Recomendaciones

1. Se recomienda hacer el trabajo inicial de la creación del código numérico a mano para que esté en el orden requerido y utilizar este programa para mantener el orden en caso de adicionar archivos o sustraer archivos
2. Se recomienda dejar un espacio de separación entre el código y el resto del nombre del archivo tanto para estética como para evitar errores
3. Como medida de seguridad en caso de no adicionar o sustraer ninguna cantidad al código el programa pasara por alto la etapa de renombrado

### Limitaciones

1. El programa no reconocerá archivos sin el código y tampoco puede expandirlo
2. En caso de que entre los primeros caracteres que deberían corresponder al código numérico hay algo que no se pueda considerar número lo omitirá

### Licencia

Este proyecto está bajo licencia MIT.

### Contribuciones

Actualmente, no se aceptan Pull Requests.
Si encuentras un error o deseas sugerir una mejora, abre un issue explicando el caso.
El proyecto puede ser modificado libremente mediante un fork, pero dichas versiones no estarán asociadas a la versión oficial

### Versión

Versión actual: 1.0