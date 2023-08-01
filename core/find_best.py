from decimal import Decimal, getcontext

def find_best_portfolio(stocks, budget):
    n = len(stocks)
    if n == 0 or budget == 0:
        return 0, []

    getcontext().prec = 2  # Set the precision for decimal arithmetic
    dp = [Decimal(0)] * (budget + 1)
    selected_stocks = [[] for _ in range(budget + 1)]

    for stock_name, cost, return_value in stocks:
        for j in range(budget, int(cost) - 1, -1):
            if dp[j - int(cost)] + Decimal(return_value) > dp[j]:
                dp[j] = dp[j - int(cost)] + Decimal(return_value)
                selected_stocks[j] = selected_stocks[j - int(cost)] + [(stock_name, Decimal(cost), Decimal(return_value))]

    return dp[budget], selected_stocks[budget]

