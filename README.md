# Portfolio Optimization

This project implements various algorithms for portfolio optimization. The goal is to select a combination of stocks from a given list while staying within a budget constraint, in order to maximize the total return on investment (ROI).

## Algorithms

The project includes the following portfolio optimization algorithms:

- **Brute Force**: This algorithm exhaustively explores all possible combinations of stocks to find the best portfolio within the budget constraint.

- **Optimized**: This algorithm uses dynamic programming to efficiently solve the portfolio optimization problem by considering subproblems and building a table of solutions.

- **Greedy**: This algorithm uses a greedy approach, selecting stocks with the highest profit-to-cost ratio until the budget is exhausted.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory in the terminal.

### Usage

To run the portfolio optimization with different algorithms and data:

```bash
python main.py <algo> <nom_fichier_données> <budget (facultatif)>
<algo>: Choose between 'bruteforce', 'optimized', or 'greedy' as the optimization algorithm.
<nom_fichier_données>: Specify the name of the data CSV file located in the 'data' directory.
<budget>: Optional. Set the budget constraint. Default is 500.
Performance Analysis
To analyze the performance of the algorithms:

bash
Copy code
python main.py --p
Example
To optimize a portfolio using the 'greedy' algorithm:

bash
Copy code
python main.py greedy stocks_data 1000
This command will use the 'greedy' algorithm to find the optimal portfolio for the 'stocks_data.csv' file with a budget of 1000.
```
