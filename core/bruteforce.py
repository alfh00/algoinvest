def brut_force(stocks, budget, portfolio=[]):
    if stocks:
        best_value1, best_portfolio1 = brut_force(stocks[1:], budget, portfolio)
        stock = stocks[0]
        if stock[1] <= budget:
            best_value2, best_portfolio2 = brut_force(
                stocks[1:], budget - stock[1], portfolio + [stock]
            )
            if best_value1 < best_value2:
                return best_value2, best_portfolio2

        return best_value1, best_portfolio1
    else:
        return sum([stock[2] for stock in portfolio]), portfolio
