
from juego import *
def laberintodiseno():
    print("Indique las filas (n), columnas (m) y el número de túneles (k) del laberinto. *Separados por espacios* (n m k):")
    n, m, k = map(int, input().split())

    print("Dibuja el laberinto ('A' para Alef, '#' para obstáculos, '_' para espacios vacíos, '*' para minas, '%' para salida, 'T' para túneles):")
    laberinto = [list(input()) for _ in range(n)]

    print(f"Indique las coordenadas de los túneles (x1 y1 x2 y2) para cada túnel:")
    tuneles = [list(map(int, input().split())) for _ in range(k)]

# Calcular la probabilidad de escape y mostrar el resultado
    result = prob_escape(n, m, k, laberinto, tuneles)
    print(f"\nLa probabilidad de escape de Alef es: {result}")