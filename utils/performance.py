import time
import matplotlib.pyplot as plt


def print_complexity(func):
    input_sizes = [i for i in range(0, 23, 2)]

    print(f"Function: {func.__name__}")

    input_sizes_log = []
    execution_times = []

    for n in input_sizes:
        input_data = [["i", i, i] for i in range(1, n)]

        start_time = time.time()
        func(input_data, budget=500)
        end_time = time.time()
        execution_time = end_time - start_time

        input_sizes_log.append(n)
        execution_times.append(execution_time)

        print(f"Input size: {n}, Execution time: {execution_time:.8f} seconds")

    plt.plot(input_sizes_log, execution_times, marker="o", label=func.__name__)
    plt.xlabel("Input Size ")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.title(f"{func.__name__} Complexity Analysis")
    plt.show()
