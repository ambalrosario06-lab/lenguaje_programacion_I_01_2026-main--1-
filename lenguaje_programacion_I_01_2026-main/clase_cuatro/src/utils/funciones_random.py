"""Este módulo tiene una serie de funciones random"""

# Defino mi función
def sumar_dos_numeros(a: int, b: int) -> int:
    """Esta función suma dos número y devuelve el resultado de la suma"""
    resultado: int = a + b

    return resultado

def unir_nombre(primer_nombre: str, segundo_nombre: str) -> str:
    """Esta función concatena dos nombres y devuelve el nombre completo"""
    resultado: str = f"{primer_nombre} {segundo_nombre}".title()

    return resultado

def imprimir_hermanos(hermanos: list[str]) -> None:
    """Esta función espera una lista de hermanos y la imprime"""
    for hermano in hermanos:
        print(hermano)
