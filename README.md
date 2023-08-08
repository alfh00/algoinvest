# Algo Invest

<p align="center">
  <img src="https://scontent.fcdg4-1.fna.fbcdn.net/v/t39.30808-6/301857731_754087558895984_4057687465612667658_n.png?_nc_cat=110&cb=99be929b-59f725be&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=Crsqr_wpzJMAX8BUyjd&_nc_ht=scontent.fcdg4-1.fna&oh=00_AfDnZrOth13EN_6hAhyKbSr0EFiG6m63NouVJ2R4LHdH1w&oe=64D616DF" alt="AlgoInvest&Trade Logo" width="200" height="200">
</p>

AlgoInvest&Trade, a financial company specializing in investment. The company aims to optimize its investment strategies using algorithms, in order to generate greater profits for its clients.

## Portfolio Optimization

This project implements various algorithms for portfolio optimization. The goal is to select a combination of stocks from a given list while staying within a budget constraint, in order to maximize the total return on investment (ROI).

## Algorithms

The project includes the following portfolio optimization algorithms:

- **Brute Force**: This algorithm exhaustively explores all possible combinations of stocks to find the best portfolio within the budget constraint.

- **Optimized**: This algorithm uses dynamic programming to efficiently solve the portfolio optimization problem by considering subproblems and building a table of solutions.

- **Greedy**: This algorithm uses a greedy approach, selecting stocks with the highest profit-to-cost ratio until the budget is exhausted.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory in the terminal.
3. install dependecies by running 'pip install requirements.txt'.
4. Make sure you have your csv data in the data folder ./data/<data_file>.csv.
4. Follow the usage guide bellow.

### Usage

To run the portfolio optimization with different algorithms and data:


```python
python main.py <algo> <nom_fichier_données> <budget (facultatif)>
<algo>: Choose between 'bruteforce', 'optimized', or 'greedy' as the optimization algorithm.
<nom_fichier_données>: Specify the name of the data CSV file located in the 'data' directory.
<budget>: Optional. Set the budget constraint. Default is 500.
```

Performance Analysis
To analyze the performance of the algorithms:
```python
python main.py --p
```
Example
To optimize a portfolio using the 'greedy' algorithm from the data:
```python
python main.py greedy stocks_data 1000
```
This command will use the 'greedy' algorithm to find the optimal portfolio for the 'stocks_data.csv' file with a budget of 1000.
