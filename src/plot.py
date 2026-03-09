# RUNS BENCHMARKING FUNCTIONS, CATCHES RESULTS AS A CSV, AND PLOTS RESULTS

# IMPORTS
import benchmark
import csv
import matplotlib
import numpy

sort_results    = benchmark.benchmark_sorting()
search_results  = benchmark.benchmark_searching()
conflict_results = benchmark.benchmark_conflict()

def make_csv_from_benchmark(results):
    pass


def make_plot():
    pass

if __name__ == "__main__":
    # placeholder for now -- will implement after plotmaking functions are working
    sort_table.csv = make_csv_from_benchmark(sort_results)
    search_table.csv = make_csv_from_benchmark(search_results)
    conflict_table.csv = make_csv_from_benchmark(conflict_results)
    make_plot(sort_table.csv, search_table.csv, conflict_table.csv)