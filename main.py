from utils.tools import csv_to_tuples, clean_data, print_report
from core.greedy import create_portfolio
from core.knapsack import knapsack
from core.brut_force import brut_force
from core.find_best import find_best_portfolio

stocks_list = csv_to_tuples('data/stocks.csv')

stocks_list = clean_data(stocks_list)

budget = 500

best_portfolio = find_best_portfolio(stocks_list, budget)


print_report(best_portfolio)