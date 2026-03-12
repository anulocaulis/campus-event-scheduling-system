# TIMING EXPERIMENTS FOR SORTING AND SEARCHING ALGORITHMS
# THIS SCRIPT RUNS PERFORMANCE BENCHMARKS ON MULTIPLE DATA STRUCTURES AND ALGORITHMS
# IT MEASURES EXECUTION TIME FOR SORTING, SEARCHING, AND CONFLICT DETECTION
import time
import copy

# IMPORT NEEDED METHODS
# IMPORTS EVENT OBJECT AND DATA STRUCTURES USED IN THE EXPERIMENTS
# ALSO IMPORTS RANDOM EVENT GENERATOR AND THE SORTING/SEARCHING ALGORITHMS BEING TESTED
from event_creator import Event
from dynamic_array import DynamicArrayEvent
from linked_list import EventLinkedList
from randEvent import genEvents
from sorting import insertSort, mergeSort, quickSort
from searching import linear, binary
import conflict

# FOUR TESTING SIZES FOR SORTING
sizes = [50, 500, 5000, 50000]

# FOUR TESTING SIZES FOR CONFLICT DETECTION
# SEPARATE SIZE LIST BECAUSE NAIVE CONFLICT ALGORITHM IS MUCH SLOWER
conf_size = [100, 500, 5000, 10000]

# NUMBER OF REPEATS FOR AVERAGING
trials = 3

# SORT ALGORITHMS TO TEST AND THEIR DISPLAY LABELS
# MAPS HUMAN-READABLE NAMES TO THE ACTUAL ALGORITHM IDENTIFIERS USED
sortAlgs = {
    "Insertion": "insertSort",
    "Merge":     "mergeSort",
    "Quick":     "quickSort",
}

# LOADS LIST OF EVENTS INTO OUR DYNAMIC ARRAY STRUCTURE
# CONVERTS A STANDARD PYTHON LIST OF Event OBJECTS INTO A DynamicArrayEvent STRUCTURE
def loadArray(events):
    """
    TAKES LIST OF EVENTS AND LOADS THEM INTO OUR DynamicArrayEvent.
    genEvents() RETURNS PLAIN LIST. WE HAVE TO PUT THAT LIST INTO STRUCTURE WE ARE TESTING
    PARAMS:
        events - PLAIN LIST OF Event OBJECTS
    RETURNS:
        dyn_arr - A DynamicArrayEvent CONTAINING SAME EVENTS FROM LIST
    """
    dyn_arr = DynamicArrayEvent()
    for e in events:
        dyn_arr.append(e)
    return dyn_arr

# LOADS LIST OF EVENTS INTO OUR LINKED LIST STRUCTURE
# CONVERTS A STANDARD PYTHON LIST OF Event OBJECTS INTO A EventLinkedList STRUCTURE
def loadLinked(events):
    """
    TAKES LIST OF EVENTS AND LOADS THEM INTO OUR Linked List STRUCTURE.
    genEvents() RETURNS PLAIN LIST. WE HAVE TO PUT THAT LIST INTO STRUCTURE WE ARE TESTING
    PARAMS:
        events - PLAIN LIST OF Event OBJECTS
    RETURNS:
        dyn_arr - A DynamicArrayEvent CONTAINING SAME EVENTS FROM LIST
    """
    linked = EventLinkedList()
    for e in events:
        linked.append(e)
    return linked

# BENCHMARK TESTING OF SORTING ALGORITHMS
# THIS FUNCTION TIMES insertSort, mergeSort, AND quickSort
# EACH ALGORITHM IS TESTED ON BOTH DynamicArrayEvent AND EventLinkedList
# MULTIPLE DATASET SIZES ARE USED AND TIMES ARE AVERAGED ACROSS TRIALS
def benchmark_sorting():
    """
    MEASURES RUNTIME OF ALL 3 SORT ALGORITHMS
    ON BOTH DATA STRUCTURES AT ALL 4 SIZES.
    RETURNS:
        results - A NESTED DICTRIONARY STRUCTURED AS:
            results[algorithm_name][structure_name][n] = avg_seconds
    EXAMPLE:
        results["Merge Sort"]["Array"][5000] = 0.032

    FRESH COPY PER TRIAL: GENERATE ONE RANDOM DATASET PER SIZE, THEN COPY IT BEFORE EACH TRIAL
    THIS MEANS:
        1. ALL ALGORITHMS SEE THE SAME INPUT FOR FAIR COMPARISON
        2. NO ALGORITHM SORTS AN ALREADY-SORTED LIST ON ITS SECOND TRIAL, GIVING INCORRECT TIMES
        
    """
    # BUILD THE RESULTS DICT — NESTED: ALGORITHM > STRUCTURE > SIZE > TIME
    # THIS STRUCTURE STORES AVERAGE EXECUTION TIME FOR EACH COMBINATION TESTED
    results = {}
    for alg in sortAlgs:
        results[alg] = {
            "Array":       {},
            "Linked List": {}
        }

    # OUTER LOOP: ITERATE THROUGH EACH DATASET SIZE
    # GENERATE A BASE RANDOM EVENT LIST THAT WILL BE COPIED FOR EACH TRIAL
    for n in sizes:
        print(f"\n  Generating {n:,} random events...")
        baseEvents = genEvents(n)

        # LOOP THROUGH EACH SORTING ALGORITHM
        for alg, key in sortAlgs.items():

            # TESTING ARRAY STRUCTURE
            # RUN THE SELECTED SORT ALGORITHM ON THE DynamicArrayEvent STRUCTURE
            arrTime = 0
            for t in range(trials):
                # DEEP COPY: INDEPENDENT COPY OF LIST SO EACH TRIAL STARTS UNSORTED
                deepCop = copy.deepcopy(baseEvents)
                dyn_arr = loadArray(deepCop)

                start = time.perf_counter()
                dyn_arr.sort(algorithm=key)
                end = time.perf_counter()

                arrTime += (end - start)

            avgTime = arrTime / trials
            results[alg]["Array"][n] = avgTime
            print(f"    {alg:15s} | Array       | n={n:6,} | {avgTime:.6f}s")

            # TESTING LINKED LIST STRUCTURE
            # RUN THE SAME SORT ALGORITHM ON TEH EventLinkedList STRUCTURE
            linkedTime = 0
            for t in range(trials):
                deepCop = copy.deepcopy(baseEvents)
                ll = loadLinked(deepCop)

                start = time.perf_counter()
                ll.sort(algorithm=key)
                end = time.perf_counter()

                linkedTime += (end - start)

            avgTime = linkedTime / trials
            results[alg]["Linked List"][n] = avgTime
            print(f"    {alg:15s} | Linked List | n={n:6,} | {avgTime:.6f}s")

    return results

# BENCHMARK TESTING OF SEARCHING ALGORITHMS
# THIS FUNCTION COMPARES LINEAR SEARCH AND BINARY SEARCH PERFORMANCE
# TESTS ARE RUN ON BOTH SORTED AND UNSORTED DATA TO ILLUSTRATE PERFORMANCE DIFFERENCES
def benchmark_searching():
    """
    MEASURES RUNTIME OF LINEAR SEARCH VS BINARY SEARCH
    ON SORTED AND UNSORTED DATA AT ALL 4 SIZES.
    RETURNS:
        results - DICTIONARY STRUCTURED AS:
            results["linear"]["unsorted"][n] = avg_seconds
            results["linear"]["sorted"][n]   = avg_seconds
            results["binary"]["sorted"][n]   = avg_seconds
            (CAN'T REALLY TEST BINARY SEARCH ON UNSORTED)

    """
    # INITIALIZE RESULTS DICTIONARY FOR STORING SEARCH TIMING
    results = {
        "linear":        {"unsorted": {}, "sorted": {}},
        "binary":        {"sorted": {}},
    }

    # LOOP THROUGH EACH DATASET SIZE AND GENERATE RANDOM EVENTS
    for n in sizes:
        print(f"\n  n = {n:,}")
        baseEvents = genEvents(n)
        
        # SORT A COPY OF DATA USING quickSort() SO BINARY SEARCH CAN BE USED
        sorted = quickSort(copy.deepcopy(baseEvents), key=lambda e: e.id)

        # TARGET: ID OF LAST ELEMENT IN SORTED LIST
        # LINEAR SEARCH ON UNSORTED DATA HAS TO SCAN WHOLE LIST: WORST CASE SCENARIO
        target_id = sorted[-1].id

        # LINEAR ON UNSORTED DATA
        # DEMONSTRATES THE COST OF FULL LIST SCANNING
        totalTime = 0
        for t in range(trials):
            deepCop_unsorted = copy.deepcopy(baseEvents)
            start = time.perf_counter()
            linear(target_id, deepCop_unsorted)
            end = time.perf_counter()
            totalTime += (end - start)
        avgTime = totalTime / trials
        results["linear"]["unsorted"][n] = avgTime
        print(f"    Linear  | Unsorted | {avgTime:.6f}s")

        # LINEAR ON SORTED DATA
        # SHOWS THAT SORTING DATA DOES NOT IMPROVE LINEAR SEARCH COMPLEXITY
        totalTime = 0
        for t in range(trials):
            deepCop_sorted = copy.deepcopy(sorted)
            start = time.perf_counter()
            linear(target_id, deepCop_sorted)
            end = time.perf_counter()
            totalTime += (end - start)
        avgTime = totalTime / trials
        results["linear"]["sorted"][n] = avgTime
        print(f"    Linear  | Sorted   | {avgTime:.6f}s")

        # BINARY ON SORTED DATA
        # DEMONSTRATES THE LOGARITHMIC TIME COMPLEXITY ADVANTAGE OF BINARY SEARCH
        totalTime = 0
        for t in range(trials):
            deepCop_sorted = copy.deepcopy(sorted)
            start = time.perf_counter()
            binary(target_id, deepCop_sorted, key=lambda e: e.id)
            end = time.perf_counter()
            totalTime += (end - start)
        avgTime = totalTime / trials
        results["binary"]["sorted"][n] = avgTime
        print(f"    Binary  | Sorted   | {avgTime:.6f}s")

    return results

# BENCHMARK TESTING FOR CONFLICT DETECTION
# COMPARES A NAIVE O(n^2) CONFLICT DETECTION APPROACH AGAINST AN OPTIMIZED VERSION
# OPTIMIZED VERSION FIRST SORTS EVENTS USING DIFFERENT SORT ALGORITHMS
def benchmark_conflict():
    """
    MEASURES RUNTIME OF NAIVE VS OPTIMIZED CONFLICT DETECTION.
    TEST ALL THREE SORTS.
    RESULTS STRUCTURED AS:
        results[LinkedList][naive][n] = avg_seconds
        results[LinkedList][mergeSort][n] = avg_seconds
        results[LinkedList][insertSort][n] = avg_seconds
        results[LinkedList][quickSort][n] = avg_seconds
        results[DynamicArray][naive][n] = avg_seconds
        results[DynamicArray][mergeSort][n] = avg_seconds
        results[DynamicArray][insertSort][n] = avg_seconds
        results[DynamicArray][quickSort][n] = avg_seconds 
    """
    # SETUP NESTED LOOPS OF ALL STRUCTURES AND ALGORITHMS
    # MAP TO LOADING FUNCTIONS AND ALGORITHM FUNCTIONS
    structures = ["Array", "LinkedList"]
    sort_funcs = {"insertSort": insertSort, "mergeSort": mergeSort, "quickSort": quickSort}
    algos = ["Naive", "insertSort", "mergeSort", "quickSort"]
    loaders = {"Array": loadArray, "LinkedList": loadLinked}

    # INITIALIZE RESULTS DATA STRUCTURE FOR STORING TIMES
    results = {"Array":  {alg: {} for alg in algos},
               "LinkedList": {alg: {} for alg in algos}}
    
    # LOOP THROUGH EACH DATASET SIZE USED FOR CONFLICT TESTING
    for n in conf_size:
        print(f"\n  n = {n:,}")
        baseEvents = genEvents(n)
        
        # TEST BOTH DATA STRUCTURES: DynamicArrayEvent AND EventLinkedList
        for structure in structures:
            loader_func = loaders[structure]
            
            # TEST EACH CONFLICT DETECTION STRATEGY
            for alg in algos:
                # SKIP NAIVE ALGORITHM FOR VERY LARGE DATASETS BECAUSE IT'S TOO SLOW
                if alg == "Naive" and n > 5000:
                    print(f"skipping brute force conflict detection for n={n} for troubleshooting")
                    continue
                conflict_time = 0
                
                # RUN MULTIPLE TRIALS FOR AVERAGING
                for t in range(trials):
                    container = loader_func(copy.deepcopy(baseEvents))
                    sort_func = None
                    if alg != "Naive":
                        sort_func = sort_funcs[alg]
                    start = time.perf_counter()
                    conflict.conflict(container, sort_func=sort_func)
                    end = time.perf_counter()
                    conflict_time += (end - start)
                
                avg_time = conflict_time/trials
                results[structure][alg][n] = avg_time
                print(f"{structure:10s} | {alg:15s} | n={n:6} | Average Completion: {avg_time:.6f}s")
    return results

# ENTRY POINT
# WHEN THIS SCRIPT IS RUN DIRECTLY, EXECUTE ALL THREE BENCHMARK SUITES
# RESULTS ARE STORED IN VARIABLES SO THEY CAN BE PASSED INTO A PLOTTING FUNCTION
if __name__ == "__main__":
    sort_results    = benchmark_sorting()
    search_results  = benchmark_searching()
    conflict_results = benchmark_conflict()
    print("\n\nAll benchmarks complete.")
    print("Pass sort_results and search_results into plot_benchmarks() to visualize.")

