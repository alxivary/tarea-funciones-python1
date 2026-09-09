# Reserva de un Asiento en Sala de Cine

**Estudiante:** [Escribe aquí tu nombre completo]

## Objetivo del programa

Gestionar la reserva de asientos de una sala de cine pequeña de 3 filas por
4 columnas (12 asientos en total), utilizando una matriz representada como
lista de listas. El programa permite:

- Crear la matriz de asientos inicializada en 0 (libre).
- Solicitar al usuario la fila y columna del asiento a reservar.
- Marcar el asiento como reservado (valor 1).
- Mostrar el estado completo de la sala en formato de tabla, recorriendo
  la matriz con bucles anidados.

## Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado.
2. Desde la terminal, ubícate en la carpeta del proyecto.
3. Ejecuta:

   ```bash
   python3 reserva_cine.py
   ```

4. Ingresa la fila (0 a 2) y la columna (0 a 3) del asiento que deseas
   reservar cuando el programa lo solicite.
5. El programa mostrará la sala completa como una matriz de 0 (libre) y
   1 (reservado).

## Ejemplo de ejecución

```
Ingrese fila (0 a 2): 2
Ingrese columna (0 a 3): 1
Asiento reservado con éxito.

Estado de la sala:
0 0 0 0
0 0 0 0
0 1 0 0
```
