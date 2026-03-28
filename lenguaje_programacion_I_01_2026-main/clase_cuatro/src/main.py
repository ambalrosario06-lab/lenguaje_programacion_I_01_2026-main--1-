from pathlib import Path
import csv
from colorama import Fore, Back, Style
from utils.funciones_random import unir_nombre

# Módulos propios
nombre_completo = unir_nombre("Juan", "Santos")
print(nombre_completo)

# Lectura de un archivo .txt
path: Path = Path("frases.txt")
content: str = path.read_text(encoding="utf-8")

print(content)

# Escribir en un archivo .txt
path: Path = Path("frases.txt")

content: str = "1. No te rindas"
content += "\n2. Sigue estudiando, el tiempo te recompensará"
content += "\n3. La programación es el hoy y el mañana"
content += "\n4. La ingeniería de software es una buena carrera"
content += "\n5. La IA es excelente para aprender y para ser más productivo"

path.write_text(content)
print("Fin de escritura")

# Leer archivos CSV
with open("estudiantes.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)

# Excepciones -> Manejo de errores
a: int = 10
b: int = 3

# print(a / b)

try:
    # El código que puede darme arror
    resultado = a / b
except ZeroDivisionError:
    # Bloque se se ejecuta si hay un error de división entre cero
    print("No se puede dividir entre cero!")
except Exception as e:
    print(e)
else:
    # Se ejecuta si no hay un error
    print(resultado)

# Módulo de tercero

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
