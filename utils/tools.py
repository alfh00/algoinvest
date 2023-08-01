import csv
from math import ceil
from decimal import Decimal, getcontext

def csv_to_tuples(csv_path):
    try:
        with open(csv_path) as f:
          data = csv.reader(f)
          stock_list = [list(line) for line in data]
          return stock_list[1:]
    except FileNotFoundError:
        print('File does not exist.')

def clean_data(list):
    clean_data = []
    for stock in list:
        stock[1] = round(float(stock[1]),2)
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
        # total_portfolio_return += stock[2]
        # total_portfolio_return += stock[2] - stock[1]
        total_portfolio_return += stock[2]
        
    
    print('---------------------------')
    print('         Portfolio         ')
    print('---------------------------')
    # for i, stock in enumerate(portfolio):
    #     print(f'{i+1})  {stock[0]}', stock[1].quantize(Decimal('0.00'), rounding=ROUND_HALF_UP), stock[1].quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))
    # print('---------------------------')
    for i, stock in enumerate(portfolio):
        print(f'{i+1})  {stock[0]}', round(float(stock[1]),2), round(float(stock[2]),2))
    print('---------------------------')
    print('         Results           ')
    print('---------------------------')
    print('Portfolio Cost: ',float(total_portfolio_cost))
    print('Portfolio Return: ',total_portfolio_return)
    print('Portfolio Return in %: ',total_portfolio_return / total_portfolio_cost * 100, '%')

