# RUNS BENCHMARKING FUNCTIONS, CATCHES RESULTS AS A CSV, AND PLOTS RESULTS

# IMPORTS
import benchmark
import csv
import matplotlib.pyplot as plt
import numpy as np


def flatten_nested_results_dictionary(results):
    fieldnames = ["Structure", "Algorithm", "N", "Time"]
    flat_data = []
    for structure, algs in results.items():
        for alg, n_data in algs.items():
            for n, time in n_data.items():
                flat_data.append({"Structure": structure,
                                  "Algorithm": alg,
                                  "N": n,
                                  "Time": time
                                  })
    return flat_data

def csv_writer(flat_results, filename="results.csv"):
    fieldnames = ["Structure", "Algorithm", "N", "Time"]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(flat_results)
    return filename



def make_plot(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            row["N"] = int(row["N"])
            row["Time"] = float(row["Time"])
            data.append(row)

    algorithms = set(d['Algorithm'] for d in data)
    structures = set(d['Structure'] for d in data)
    for structure in structures:
        for alg in algorithms:
            subset = [d for d in data if d['Algorithm'] == alg and d['Structure'] == structure]
            subset.sort(key=lambda x: x['N'])

        x = [d['N'] for d in subset]
        y = [d['Time'] for d in subset]
        plt.plot(x, y, label = f"{structure} {alg}", marker = '.')

    plt.title(f"Performance Analysis: {filename}")
    plt.xlabel("Number of Events (log scale)")
    plt.ylabel("Time (sec)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log') # displaying at log scale to see difference in sorting algs
    # SAVE OUTPUT
    png_name = filename.split('.')[0] + ".png"
    plt.savefig(png_name, dpi=300)
    
    plt.show()

if __name__ == "__main__":
    # placeholder for now -- will implement after plotmaking functions are working
    try:
        make_plot("sort_results.csv")
        make_plot("search_results.csv")
        make_plot("conflict_results.csv")

    except FileNotFoundError:
        sort_results    = benchmark.benchmark_sorting()
        search_results  = benchmark.benchmark_searching()
        conflict_results = benchmark.benchmark_conflict()

        sort_flat = flatten_nested_results_dictionary(sort_results)
        search_flat = flatten_nested_results_dictionary(search_results)
        conflict_flat = flatten_nested_results_dictionary(conflict_results)

        csv_writer(sort_flat, "sort_results.csv")
        csv_writer(search_flat, "search_results.csv")
        csv_writer(conflict_flat, "conflict_results.csv")

        make_plot("sort_results.csv")
        make_plot("search_results.csv")
        make_plot("conflict_results.csv")