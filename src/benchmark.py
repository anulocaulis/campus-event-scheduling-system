# TIMING EXPERIMENTS FOR SORTING AND SEARCHING ALGORITHMS
import time
import copy

# IMPORT NEEDED METHODS
from event_creator import Event
from dynamic_array import DynamicArrayEvent
from linked_list import EventLinkedList
from sorting import insertSort, mergeSort, quickSort
from searching import linear, binary

# FOUR TESTING SIZES
sizes = [50, 500, 5000, 50000]
# NUMBER OF REPEATS FOR AVERAGING
trials = 3
# SORT ALGORITHMS TO TEST AND THEIR DISPLAY LABELS
sortAlgs = {
    "Insertion": "insertSort",
    "Merge":     "mergeSort",
    "Quick":     "quickSort",
}

# LOADS LIST OF EVENTS INTO OUR DYNAMIC ARRAY STRUCTURE
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
    results = {}
    for alg in sortAlgs:
        results[alg] = {
            "Array":       {},
            "Linked List": {}
        }

    for n in sizes:
        print(f"\n  Generating {n:,} random events...")
        baseEvents = genEvents(n)

        for alg, key in sortAlgs.items():

            # TESTING ARRAY STRUCTURE
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
            linkedTime = 0
            for trial in range(trials):
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
def benchmark_searching():
    """
    MEASURES RUNTIME OF LINEAR SEARCH VS BINARY SEARCH
    ON SORTED AND UNSORTED DATA AT ALL 4 SIZES.
    RETURNS:
        results - DICTIONARY STRUCTURED AS:
            results["linear"]["unsorted"][n] = avg_seconds
            results["linear"]["sorted"][n]   = avg_seconds
            results["binary"]["sorted"][n]   = avg_seconds
            (CAN'T TEST BINARY SEARCH ON UNSORTED)

    """

    results = {
        "linear":        {"unsorted": {}, "sorted": {}},
        "binary":        {"sorted": {}},
    }

    for n in sizes:
        print(f"\n  n = {n:,}")
        baseEvents = genEvents(n)
        # SORT A COPY FOR BINARY SEARCH USING quickSort()
        sorted = quickSort(copy.deepcopy(baseEvents), key=lambda e: e.id)

        # TARGET: ID OF LAST ELEMENT IN SORTED LIST
        # LINEAR SEARCH ON UNSORTED DATA HAS TO SCAN WHOLE LIST: WORST CASE SCENARIO
        target_id = sorted[-1].id

        # LINEAR ON UNSORTED
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

        # LINEAR ON SORTED - SHOWS THAT SORTING DATA DOES NOT HELP LINEAR SEARCH TIMES
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

        # BINARY ON SORTED
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



# ENTRY POINT
if __name__ == "__main__":
    sort_results    = benchmark_sorting()
    search_results  = benchmark_searching()
    print("\n\nAll benchmarks complete.")
    print("Pass sort_results and search_results into plot_benchmarks() to visualize.")

