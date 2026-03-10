# Campus Event Scheduling System
**DTSC5501 — Data Structures and Algorithms | Group Project 1**
Beitner · Echeverry · Taylor

---

## Overview

A lightweight scheduling system for managing campus events — talks, hackathons, concerts, exams, and more. The system supports adding, searching, sorting, and conflict-checking events efficiently as the event list scales from a handful to tens of thousands. Two independent data structure backends (dynamic array and singly linked list) are implemented and benchmarked against each other across all operations.

---

## Repository Structure

```
campus-event-scheduling-system/
│
├── src/
│   ├── event_creator.py          # EVENT CLASS AND UNIQUE ID GENERATOR
│   ├── sample_array.py           # HARDCODED TEST EVENTS FOR DEVELOPMENT/TESTING
│   ├── randEvent.py              # RANDOM EVENT GENERATOR FOR BENCHMARK TESTING
│   ├── dynamic_array.py          # ARRAY-BASED EVENT STORAGE (DYNAMIC)
│   ├── linked_list.py            # LINKED LIST EVENT STORAGE
│   ├── converter.py              # CONVERTS LINKED LIST TO PLAIN PYTHON LIST
│   ├── sorting.py                # INSERTION SORT, MERGE SORT, QUICK SORT
│   ├── searching.py              # LINEAR SEARCH, BINARY SEARCH
│   ├── conflict.py               # NAIVE O(n²) AND OPTIMIZED O(n log n) CONFLICT DETECTION
│   ├── benchmark.py              # TIMING EXPERIMENTS ACROSS ALL ALGORITHMS AND DATA STRUCTURES
│   ├── plot.py                   # CSV EXPORT AND MATPLOTLIB PLOTTING OF BENCHMARK RESULTS
│   └── scalability-challenge.py  # MEMORY ESTIMATION AND SCALABILITY ANALYSIS AT n=1000000
│
├── tests/
│   ├── dynamic_array_test.py     # PYTEST SUITE FOR DynamicArrayEvent
│   ├── linked_list_test.py       # PYTEST SUITE FOR EventLinkedList
│   ├── sorting_test.py           # PYTEST SUITE FOR 3 SORTING ALGORITHMS
│   ├── searching_test.py         # PYTEST SUITE FOR LINEAR/BINARY SEARCH
│   └── conflict_test.py          # PYTEST SUITE FOR CONFLICT DETECTION
│
├── GP1_Beitner_Echeverry_Taylor.ipynb    # FINAL REPORT NOTEBOOK
├── requirements.txt                      # REQUIREMENTS USED TO RUN PROJECT
├── .gitignore
└── README.md
```

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/anulocaulis/campus-event-scheduling-system.git
cd campus-event-scheduling-system
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

Dependencies are minimal: `pytest`, `matplotlib`, and `numpy`. No external data structure libraries are used — all core implementations are original.

**3. Verify your Python version**

Python 3.9 or higher is recommended.
```bash
python --version
```

---

## Running the Tests

From the root of the repository:
```bash
pytest tests/
```

To run a specific test file:
```bash
pytest tests/sorting_test.py
pytest tests/searching_test.py
pytest tests/conflict_test.py
pytest tests/dynamic_array_test.py
pytest tests/linked_list_test.py
```

To see individual test names as they run:
```bash
pytest tests/ -v
```

---

## Running the Benchmarks

From the `src/` directory:
```bash
python benchmark.py
```

This runs all three benchmark suites — sorting, searching, and conflict detection — across both data structures at n = 50, 500, 5,000, and 50,000 events. Results are printed to the console. To generate CSV files and plots:
```bash
python plot.py
```

---

## Team Roles

| Member | Primary Contributions |
|---|---|
| **Mike Beitner** | Conflict detection algorithms (`conflict.py`), benchmark result analysis, plotting (`plot.py`), scalability analysis (`scalability-challenge.py`) |
| **Luis Echeverry** | Data structure backends (`dynamic_array.py`, `linked_list.py`), ('dynamic_array_test.py', 'linked_list_test.py') |
| **Christopher Taylor** | Sorting algorithms (`sorting.py`), searching algorithms (`searching.py`), benchmark infrastructure (`benchmark.py`), full pytest suite (`tests/`), `event_creator.py`, `randEvent.py`, `converter.py`, `sample_array.py` |

---

## Key Design Decisions

**Event representation** — Events are stored as objects with five attributes: `id` (auto-generated 6-digit integer), `title`, `date` (`YYYY-MM-DD`), `time` (`HH:MM`), and `location`. Dates and times are stored as zero-padded strings so that chronological order is equivalent to lexicographic order, enabling direct string comparison in sorting.

**Sort key** — All sorting uses a `(date, time, location)` tuple as the sort key, prioritizing date first, then time, then location alphabetically as a tiebreaker.

**Linked list sorting** — Since linked lists do not support O(1) random access, sorting is performed by converting to a plain Python list via `converter.py`, sorting, then writing the sorted events back into the existing nodes in place.

**Conflict detection** — Two approaches are provided. The naive O(n²) approach compares every pair of events directly. The optimized O(n log n) approach sorts events by the sort key first, then makes a single pass comparing only adjacent pairs — conflicts will always be adjacent after sorting by date/time/location.

---

## Results Summary

### Conflicts

#### **Dynamic Array**

**Naive Results**
  
| N        | Time(seconds) | 
| ------------- |:----------:|
| 100      | 0.000273 seconds| 
| 500      | 0.009020 seconds| 
| 5000     | 0.875134 seconds| 

**insertSort Results**
    
| N        | Time(seconds) | 
| ------------- |:----------:|
| 100      | 0.001259 seconds| 
| 500      | 0.024550 seconds| 
| 5000     | 2.981901 seconds| 
| 50000    | 15.428314 seconds| 


**mergesort Results**
    
| N        | Time(seconds) | 
| ------------- |:----------:|
| 100      | 0.000501 seconds| 
| 500      | 0.002552 seconds| 
| 5000     | 0.035535 seconds| 
| 50000    | 0.088872 seconds| 

**quicksort Results**

| N        | Time(seconds) | 
| ------------- |:----------:|
| 100      | 0.000603 seconds| 
| 500      | 0.003960 seconds| 
| 5000     | 0.050319 seconds| 
| 50000    | 0.135598 seconds| 


#### **LinkedList**

 **Naive Results**

| N        | Time(seconds) | 
| ------------- |:----------:|
| 100      | 0.000299 seconds| 
| 500      | 0.009040 seconds| 
| 5000     | 0.923255 seconds| 


**insertSort Results**
    
| N        | Time(seconds) | 
| ------------- |:----------:|
| 100      | 0.001201 seconds| 
| 500      | 0.025884 seconds| 
| 5000     | 3.000228 seconds| 
| 50000    | 14.444262 seconds|




**mergesort Results**

| N        | Time(seconds) | 
| ------------- |:----------:|
| 100      | 0.000436 seconds| 
| 500      | 0.002924 seconds| 
| 5000     | 0.035358 seconds| 
| 50000    | 0.090099 seconds|

**quicksort Results**
| N        | Time(seconds) | 
| ------------- |:----------:|
| 100      | 0.000626 seconds| 
| 500      | 0.003825 seconds| 
| 5000     | 0.052843 seconds| 
| 50000    | 0.139516 seconds|

  
### Sorted

- **Insertion**:

  - **Dynamic Array**

    - **Results**
      - N = 50: Time $\approx$ 0.000159 seconds
      - N = 500: Time $\approx$ 0.016448 seconds
      - N = 5000: Time $\approx$ 0.016448 seconds
      - N = 50000: Time $\approx$ 245.254482 seconds

  - **Linked List**

    - **Results**
      - N = 50: Time $\approx$ 0.000434 seconds
      - N = 500: Time $\approx$ 0.015448 seconds
      - N = 5000: Time $\approx$ 1.596537 seconds
      - N = 50000: Time $\approx$ 458.777888 seconds
            
    
- **Merge**:
  
  - **Dynamic Array**

    - **Results**
      - N = 50: Time $\approx$ 9.846667e-05 seconds
      - N = 500: Time $\approx$ 0.001654 seconds
      - N = 5000: Time $\approx$ 0.019559 seconds
      - N = 50000: Time $\approx$ 0.458003 seconds

  - **Linked List**
  
    - **Results**
      - N = 50: Time $\approx$ 9.720000e-05 seconds
      - N = 500: Time  $\approx$ 0.001579 seconds
      - N = 5000: Time $\approx$ 0.019411 seconds
      - N = 50000: Time $\approx$ 0.4227471seconds

- **Quick**:
  
    - **Dynamic Array**

        - **Results**
            - N = 50 : Time $\approx$ 0.000133 seconds
            - N = 500: Time  $\approx$ 0.002192 seconds 
            - N = 5000: Time $\approx$ 0.027317 seconds
            - N = 50000: Time $\approx$ 0.697710 seconds
     

  - **Linked List**
    
    - **Results**
      - N = 50 : Time $\approx$ 0.000133 seconds
      - N = 500: Time  $\approx$ 0.002020 seconds
      - N = 5000: Time $\approx$ 0.027627 seconds
      - N = 50000: Time $\approx$ 0.787503 seconds
 


       

### Search
- **Linear Unsorted**

  - **Results** 
    - N = 50 : Time $\approx$ 0.000179 seconds
    - N = 500: Time  $\approx$ 0.000200 seconds 
    - N = 5000: Time $\approx$ 0.000686 seconds
    - N = 50000: Time $\approx$ 0.004487 seconds


- **Linear Sorted**
 
  - **Results** 
    - N = 50 : Time $\approx$ 0.000339 seconds
    - N = 500: Time  $\approx$ 0.000257 seconds
    - N = 5000: Time $\approx$ 0.000972 seconds
    - N = 50000: Time $\approx$ 0.010381 seconds


- **Binary Sorted**:

  - **Results** 
    - N = 50 : Time $\approx$ 0.000262 seconds
    - N = 500: Time  $\approx$ 0.000222 seconds
    - N = 5000: Time $\approx$ 0.000241 seconds
    - N = 50000: Time $\approx$ 0.000250 seconds

---

## Notes

- Built-in Python sort functions (`list.sort`, `bisect`, etc.) are not used anywhere in the core implementation per assignment constraints.
- NumPy and Matplotlib are used only for analysis and plotting, not for any core data structure or algorithm logic.


