def knapsack(stocks, budget):
    n = len(stocks)
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            stock_cost = stocks[i - 1][1]
            stock_roi_percentage = stocks[i - 1][2]

            if stock_cost <= j:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - stock_cost] + stock_roi_percentage)
            else:
                dp_table[i][j] = dp_table[i - 1][j]

    best_portfolio = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp_table[i][j] != dp_table[i - 1][j]:
            best_portfolio.append(stocks[i - 1])
            j -= stocks[i - 1][1]
        i -= 1

    best_roi = dp_table[n][budget]

    return best_portfolio