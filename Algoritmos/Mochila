def knapsack(pesos, valores, capacidad):
    n = len(valores)
    dp = [[0]*(capacidad+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacidad+1):
            if pesos[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], valores[i-1] + dp[i-1][w - pesos[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacidad]

# Ejemplo
pesos = [2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
valores = [3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
capacidad =70
print("Valor máximo en la mochila:", knapsack(pesos, valores, capacidad))
