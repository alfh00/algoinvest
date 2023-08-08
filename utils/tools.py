import csv


def import_csv(csv_path):
    try:
        with open(csv_path) as f:
            data = csv.reader(f)
            stock_list = [list(line) for line in data]
            return stock_list[1:]
    except FileNotFoundError:
        print("File does not exist.")


def clean_data(list):
    clean_data = []

    for stock in list:
        stock[1] = float(stock[1])
        stock[2] = float(stock[2]) * float(stock[1]) / 100

        if stock[1] > 0 and stock[2] > 0:
            clean_data.append(stock)
    return clean_data


def print_report(portfolio):
    if len(portfolio) == 2:
        portfolio = portfolio[1]
    portfolio_sotcks = []
    total_portfolio_cost = 0
    total_portfolio_return = 0
    for stock in portfolio:
        portfolio_sotcks.append(stock[0])
        total_portfolio_cost += stock[1]
        total_portfolio_return += stock[2]

    print("--------------------------------")
    print("            Portfolio           ")
    print("--------------------------------")
    print("N°".center(4), "Stock".center(12), "Cost".center(8), "ROI".center(6))
    print("--------------------------------")

    for i, stock in enumerate(portfolio):
        number = f"{i+1})".center(4)
        stock_name = stock[0].center(12)
        cost = str(stock[1]).center(8)
        roi = str(round(stock[2], 2)).center(6)
        print(number, stock_name, cost, roi)
    print("--------------------------------")
    print("            Results             ")
    print("--------------------------------")
    print("Portfolio Cost:        ", round(total_portfolio_cost, 2))
    print("Portfolio Return:      ", round(total_portfolio_return, 2))
    print(
        "Portfolio Return in %: ",
        round(total_portfolio_return / total_portfolio_cost * 100, 2),
        "%",
    )
