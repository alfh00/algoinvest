

def create_portfolio(stocks, budget):
    # Sort stocks in descending order of profit-to-cost ratio
    sorted_stocks = sorted(stocks, key=lambda x: x[2] / x[1], reverse=True)

    portfolio = []
    remaining_budget = budget

    for stock in sorted_stocks:
        if stock[1] <= remaining_budget:
            portfolio.append(stock)
            remaining_budget -= stock[1]

    return portfolio



