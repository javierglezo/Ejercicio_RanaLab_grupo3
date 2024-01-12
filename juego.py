
def prob_escape(n, m, k, laberinto, tuneles):
    def mov_valido(x, y):
        return 0 <= x < n and 0 <= y < m and laberinto[x][y] not in ['#','*']
    def prob_exito(x, y, visitado):
        if laberinto[x][y] == '%':
            return 1.0  # Si en casilla salida, prob 100%
        if (x, y) in visitado:
            return 0.0  # Si ya has estado, 0%
        visitado.add((x,y))

        prob_acumulada = 0.0

        movimientos_posibles = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for proximox, proximoy in movimientos_posibles:
            if mov_valido(proximox, proximoy):
                prob_acumulada += prob_exito(proximox, proximoy, visitado)

        visitado.remove((x, y))
        return prob_acumulada / len(movimientos_posibles)
    def mover_tunel(x, y, tunel):
        return 0 <= x < n and 0 <= y < m and laberinto[x][y] not in ['#', '_', '*'] and (x, y) != (tunel[0], tunel[1])
    
    for i in range(n):
        for j in range(m):
            if laberinto[i][j] == 'A':
                posicioninicial = (i, j)

    prob_acumulada = 0,0
    for tunel in tuneles:
        x, y = posicioninicial
        if mover_tunel(x, y, tunel):
            prob_acumulada += prob_exito(tunel[2], tunel[3], set)

    return prob_acumulada
