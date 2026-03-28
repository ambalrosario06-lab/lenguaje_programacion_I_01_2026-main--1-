# type: ignore
# ? Entradas de datos
prompt = "Ingresa tu nombre: "
nombre = input(prompt)
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))

print(nombre + " " + apellido)  # Concatenación
print(f"Hola, mi nombre es {nombre} {apellido}")  # Interpolación

# ? Listas
hermanos = ["Juan", "Pedro", "María"]

# Añadir un elemento
hermanos.append("Carlos")
print(f"Haz registrado a {hermanos[-1]}")

hermano = input("Ingresa tu hermano: ")
hermanos.append(hermano)  # Añade al final un nuevo dato a mi lista

hermano = input("Ingresa tu hermano: ")
hermanos.append(hermano)

hermano = input("Ingresa tu hermano: ")
hermanos.append(hermano)

# Eliminar un elemento
hermanos.remove("Juan")
hermanos.remove("Juan")
hermanos.remove("Carlos")

# 'del' permite eliminar un elemento o varios elementos a la vez, e incluso a la misma lista
del hermanos

# Insertar un elemento
# -1 usando insert sería la penúltima posición
# la última posición sería la longitud de la lista
hermanos.insert(2, "María")

hermano_eliminado = hermanos.pop(-1)
print(f"Haz eliminado a '{hermano_eliminado}'.")

print(hermanos)

# ? Tuplas
nombre, apellido, edad = ("Juan", "Santana", 38)  # Desempaquetado
persona = ("Juan", "Santana", 38)
print(persona[1])

# ? Diccionarios
Estructura de datos que nos permite manipular datos en pares de clave - valor

familia = {
    "padre": "Carlos Santana",
    "madre": "Josefina Pérez",
    "hija": "María Santana Pérez",
    "abuelos": {
        "abuelo_paterno": "Juan Santana",
        "abuelo_materno": "José Pérez",
    }
}

# Get devulve el valor de la llave o nulo
# None -> Nulo
print(familia.get("hija"))

# ? Bucle For
amigos = ["Carlos Javier", "Juan José", "Marino Pérez", "Hayro Pérez"]

for amigo in amigos:
    print(amigo)

# ? Lista de tuplas
amigos = [("Carlos", "Santana", 23),
          ("María", "Pérez", 28), ("Juan", "Santos", 19)]

for nombre, apellido, edad in amigos:
    print(
        f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años de edad.")

# ? Lista de diccionario
amigos = [
    {"nombre": "Carlos", "apellido": "Santana", "edad": 23},
    {"nombre": "Juan", "apellido": "Rodríguez", "edad": 33},
    {"nombre": "Santos", "apellido": "Pérez", "edad": 17},
]

for amigo in amigos:
    print(amigo["edad"])
