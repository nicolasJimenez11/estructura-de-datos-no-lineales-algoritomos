def edit_distance(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    # Reconstruir las letras agregadas
    i, j = m, n
    agregadas = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and X[i-1] == Y[j-1]:
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j] == dp[i][j-1] + 1):
            agregadas.append(Y[j-1])
            j -= 1
        elif i > 0 and (j == 0 or dp[i][j] == dp[i-1][j] + 1):
            i -= 1
        else:
            i -= 1
            j -= 1

    agregadas.reverse()
    return dp[m][n], agregadas

# Ejemplo
palabra1 = "gato"
palabra2 = "gatito feliz"
dist, letras_agregadas = edit_distance(palabra1, palabra2)
print("Distancia de edición:", dist)
print("Letras agregadas para transformar la primera en la segunda:", letras_agregadas)