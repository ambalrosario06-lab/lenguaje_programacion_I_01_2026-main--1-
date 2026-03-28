# type: ignore
# Importación de módulos
from utils.mate import sumar, restar
from utils.juntar_nombres import nombre_completo

# === SET -> CONJUNTOS
# elementos = {"a", 3, True, ("Juan", "Carlos")}
elementos = {"a", "e", "i", "a", "a", "o", "i"}

# Agregar un elemento
elementos.add("u")

# Eliminar un elemnto
elementos.discard("a")

# Eliminar el conjunto
# del elementos

# Eliminar cada item del set
elementos.clear()

# === IF -> SENTENCIAS CONDICIONALES
edad = 18
es_estudiante = False

# Condicional simple
if edad > 17:
    # Aquí pongo las instrucciones a ejecutar si se cumple la condición
    print("Eres mayor de edad!")

# Condicional compuesta
if es_estudiante:
    print("Eres un estudiante")
else:
    print("Eres un profesor")

# Elif
dias_semana = "Domingo"

if dias_semana == "Lunes":
    print("Iniciamos la semana de trabajo.")
elif dias_semana == "Martes":
    print("Ten fuerza que apenas comienza la semana.")
elif dias_semana == "Miércoles":
    print("Ya estamos por la mitad, ánimo!")
elif dias_semana == "Jueves":
    print("Debes tomar clase, dale con todo!")
else:
    print("Este dia no está registrado!")

# Condicionales anidadas
edad = 17

if edad > 17:
    print("Eres mayor de edad!")
else:
    if edad > 11:
        print("Eres un adolescente")
    else:
        print("Eres un niño!")

# If dentro de una lista de diccionario
estudiantes = [
    {"nombre": "Carlos Rodríguez", "edad": 17, "nota_final": 89},
    {"nombre": "María Santana", "edad": 27, "nota_final": 62},
    {"nombre": "Julio Pérez", "edad": 19, "nota_final": 71},
    {"nombre": "Carlos Sosa", "edad": 29, "nota_final": 54},
    {"nombre": "Pablo Mariñez", "edad": 32, "nota_final": 100}
]

for estudiante in estudiantes:
    if estudiante["nota_final"] >= 70:
        print(f"El estudiante {estudiante["nombre"]} PASÓ.")
    else:
        print(f"El estudiante {estudiante["nombre"]} NO PASÓ.")

# === BUCLE WHILE
i = 1  # contador
s = 0  # sumador

continuar = "s"

while i <= 100:  # i (1) es menor o igual que 100
    s = s + i
    print(s)
    # i = i + 1  # Incremento constante
    i += 1

# print("Fin del while")
i = 0

while i < len(estudiantes):
    if estudiantes[i]["nota_final"] >= 70:
        print(f"El estudiante {estudiantes[i]["nombre"]} PASÓ.")
    i += 1

# ? === FUNCIONES
# Defino una función
def sumar_valores(a, b):
    # Aquí ejecuto mis instrucciones
    print("Gran total: ", a + b)

# # Llamada o invocación de una función
sumar_valores(10, 20)
sumar_valores(25, 18)
sumar_valores(101, 120)

# Retornar un valor
def restar(a, b):
    # Operaciones lógicas aquí
    # resultado = a - b
    # return resultado
    return a - b

res = restar(20, 10)
print(f"El resultado es {res}")

# ? === MÓDULOS
resultado_suma = sumar(10, 20)
resultado_resta = restar(20, 30)

nombre_usuario = nombre_completo("Jaime", "Vilorio")

print("Resultado de la suma: ", resultado_suma)
print("Resultado de la resta: ", resultado_resta)

print(f"Hola, {nombre_usuario}")
