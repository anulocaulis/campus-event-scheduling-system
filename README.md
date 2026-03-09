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
│   ├── event_creator.py          # Event class and unique ID generator
│   ├── sample_array.py           # Hardcoded test events for development/testing
│   ├── randEvent.py              # Random event generator for benchmark testing
│   ├── dynamic_array.py          # Array-based event storage (DynamicArrayEvent)
│   ├── linked_list.py            # Linked list event storage (EventLinkedList)
│   ├── converter.py              # Converts linked list to plain Python list
│   ├── sorting.py                # Insertion Sort, Merge Sort, Quick Sort
│   ├── searching.py              # Linear Search, Binary Search
│   ├── conflict.py               # Naive O(n²) and optimized O(n log n) conflict detection
│   ├── benchmark.py              # Timing experiments across all algorithms and structures
│   ├── plot.py                   # CSV export and matplotlib plotting of benchmark results
│   └── scalability-challenge.py  # Memory estimation and scalability analysis at n=1,000,000
│
├── tests/
│   ├── dynamic_array_test.py     # pytest suite for DynamicArrayEvent
│   ├── linked_list_test.py       # pytest suite for EventLinkedList
│   ├── sorting_test.py           # pytest suite for all three sorting algorithms
│   ├── searching_test.py         # pytest suite for linear and binary search
│   └── conflict_test.py          # pytest suite for conflict detection
│
├── GP1_Beitner_Echeverry_Taylor.ipynb   # Final report notebook
├── requirements.txt
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
| **Luis Echeverry** | Data structure backends (`dynamic_array.py`, `linked_list.py`) |
| **Christopher Taylor** | Sorting algorithms (`sorting.py`), searching algorithms (`searching.py`), benchmark infrastructure (`benchmark.py`), full pytest suite (`tests/`), `event_creator.py`, `randEvent.py`, `converter.py`, `sample_array.py` |

---

## Key Design Decisions

**Event representation** — Events are stored as objects with five attributes: `id` (auto-generated 6-digit integer), `title`, `date` (`YYYY-MM-DD`), `time` (`HH:MM`), and `location`. Dates and times are stored as zero-padded strings so that chronological order is equivalent to lexicographic order, enabling direct string comparison in sorting.

**Sort key** — All sorting uses a `(date, time, location)` tuple as the sort key, prioritizing date first, then time, then location alphabetically as a tiebreaker.

**Linked list sorting** — Since linked lists do not support O(1) random access, sorting is performed by converting to a plain Python list via `converter.py`, sorting, then writing the sorted events back into the existing nodes in place.

**Conflict detection** — Two approaches are provided. The naive O(n²) approach compares every pair of events directly. The optimized O(n log n) approach sorts events by the sort key first, then makes a single pass comparing only adjacent pairs — conflicts will always be adjacent after sorting by date/time/location.

---

## Results Summary

*(To be completed after benchmark runs and plots are generated.)*

---

## Notes

- Built-in Python sort functions (`list.sort`, `bisect`, etc.) are not used anywhere in the core implementation per assignment constraints.
- NumPy and Matplotlib are used only for analysis and plotting, not for any core data structure or algorithm logic.


