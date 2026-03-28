# type: ignore
# Variables y tipos de datos
nombre = "José"  # string
usuario = "tumenor08"  # string -> alfanumérico
apellido = 'Ramírez'  # string
edad = 27  # number -> integer
altura = 6.9  # number -> float
estudiante = True  # booleano -> True / False -> 1 / 0

# Esto es un comentario
print("Hola, mi nombre es " + nombre + " " + apellido)

# Operadores matemáticas
print(10 + 20)  # Suma
print(10 - 20)  # Resta
print(10 * 20)  # Múltiplicación
print(10**2)  # Potencia
print(10 / 3)  # División con valores decimales
print(10 // 3)  # División sin valores decimales
print(10 % 2)  # El módulo es el residuo de una división
print(10 + 5 * 2)  # Prioridad de los operadores


# Operadores lógicos
print(False and True)  # Y / And
print(False or True)  # O / Or
print(not True)  # No / Not


# Operadores relacionales
# Retornan un valor de verdad -> True / False
print(10 > 20)  # Mayor que
print(10 < 20)  # Menor que
print(2 >= 9)  # Mayor o igual que
print(3 <= 3)  # Menor o igual que
print(10 == 10)  # Igualdad
print(10 != 30)  # Distinto de

# Listas o Arreglos

# Homgénea
hermanos = ["Carlos Josué", "Pablo Javier", "María Esther"]
print(hermanos)
print(hermanos[1])
print(hermanos[0])

# Heterogénea
valores = [True, "Carlos", 10, 9.7]
print(valores[3])
