from sys import argv

from utils.tools import import_csv, clean_data, print_report
from utils.performance import print_complexity

from core.bruteforce import brut_force
from core.optimized import optimized
from core.greedy import greedy

ALGO = {
    "bruteforce": brut_force,
    "optimized": optimized,
    "greedy": greedy,
}


if __name__ == "__main__":
    try:
        BUDGET = int(argv[3]) if len(argv) >= 4 else 500
        if argv[1] == "--p":
            for algo in ALGO.values():
                print_complexity(algo)
        else:
            # import csv file and calculate return
            stocks_list = import_csv(f"data/{argv[2]}.csv")
            # clean data and validate data
            data = clean_data(stocks_list)
            # look for best portfolio combination
            best_portfolio = ALGO[argv[1]](data, BUDGET)
            # print report
            print_report(best_portfolio)

    except Exception:
        print("Commande incorrecte.")
        print(
            "Utilisation : python main.py <algo> <nom_fichier_données> <budget (facultatif)>"
        )
        print(
            '<algo> : Choisissez "brutforce", "optimized" ou "greedy" comme algorithme.'
        )
        print("Analyse de performances : python main.py --p")
