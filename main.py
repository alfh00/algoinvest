from sys import argv

from utils.tools import csv_to_tuples, clean_data, print_report

from core.bruteforce import brut_force
from core.optimized import knapsack, knapsack_d
from core.greedy import greedy

ALGO = {
  'brut_force': brut_force,
  'knapsack': knapsack,
  'knapsack_d': knapsack_d,
  'greedy': greedy,
}


if __name__ == '__main__':
  BUDGET = 500
  
  # import csv file
  stocks_list = csv_to_tuples(f'data/{argv[2]}.csv')
  # clean data by elimitating negative stocks values
  data = clean_data(stocks_list)
  # look for best portfolio combination
  best_portfolio = ALGO[argv[1]](data, BUDGET)
  # print report
  print_report(best_portfolio)