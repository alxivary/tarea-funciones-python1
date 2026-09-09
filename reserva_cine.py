"""
Programa: Reserva de un asiento en sala de cine
Objetivo: Gestionar la reserva de asientos de una sala de cine de 3 filas
          por 4 columnas, utilizando una matriz (lista de listas) y
          bucles anidados para mostrar el estado de la sala.

Estado de cada asiento:
    0 = asiento libre
    1 = asiento reservado
"""

NUM_FILAS = 3
NUM_COLUMNAS = 4


def crear_matriz_asientos(filas, columnas):
    """Crea y devuelve una matriz de 'filas' x 'columnas' inicializada en 0."""
    asientos = []
    for i in range(filas):
        fila_actual = []
        for j in range(columnas):
            fila_actual.append(0)
        asientos.append(fila_actual)
    return asientos


def pedir_fila_columna(filas, columnas):
    """Solicita al usuario la fila y la columna del asiento a reservar,
    validando que los valores estén dentro del rango permitido."""
    while True:
        try:
            fila = int(input(f"Ingrese fila (0 a {filas - 1}): "))
            columna = int(input(f"Ingrese columna (0 a {columnas - 1}): "))
        except ValueError:
            print("Por favor ingrese solo números enteros.\n")
            continue

        if 0 <= fila < filas and 0 <= columna < columnas:
            return fila, columna
        else:
            print("Fila o columna fuera de rango. Intente nuevamente.\n")


def reservar_asiento(asientos, fila, columna):
    """Marca el asiento indicado como reservado (valor 1).
    Informa al usuario si el asiento ya estaba reservado."""
    if asientos[fila][columna] == 1:
        print("Atención: ese asiento ya estaba reservado. Se mantiene reservado.\n")
    else:
        asientos[fila][columna] = 1
        print("Asiento reservado con éxito.\n")


def mostrar_sala(asientos):
    """Recorre la matriz con bucles anidados e imprime el estado
    de la sala en formato de tabla."""
    print("Estado de la sala:")
    for i in range(len(asientos)):
        for j in range(len(asientos[i])):
            print(asientos[i][j], end=" ")
        print()  # salto de línea al terminar cada fila


def main():
    # Crear la matriz de asientos inicializada en 0
    asientos = crear_matriz_asientos(NUM_FILAS, NUM_COLUMNAS)

    # Pedir al usuario la fila y columna del asiento a reservar
    fila, columna = pedir_fila_columna(NUM_FILAS, NUM_COLUMNAS)

    # Marcar el asiento como reservado
    reservar_asiento(asientos, fila, columna)

    # Mostrar el estado completo de la sala
    mostrar_sala(asientos)


if __name__ == "__main__":
    main()
