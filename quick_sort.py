import timeit
import random
import sys
sys.setrecursionlimit(1500000000)
import numpy as np

def partition(arr, low, high):
    """Partition the array using the last element as the pivot."""
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        # If current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Swap the pivot element with the element at (i + 1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """Recursively apply the quicksort algorithm to sort the array."""
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def run_quick_sort(n):
    # randomize input array for sorting
    arr = np.random.randint(0, 100, size=n)
    # do quickSort
    quick_sort(arr, 0, len(arr) - 1)

if __name__ == '__main__':
    # the numbber of elements for sorting
    n_values = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9] 
    for n in n_values:
        exec_time = timeit.timeit(f"run_quick_sort({n})", globals=globals(), number=1)
        print(f"Execution time for n={n}: {exec_time:.4f} seconds")

# Execution time for n=100: 0.0001 seconds
# Execution time for n=1000: 0.0014 seconds
# Execution time for n=10000: 0.0444 seconds
# Execution time for n=100000: 3.5638 seconds
# Execution time for n=1000000: 342.0187 seconds
# Execution time for n=10000000: 4621.2341 seconds
# Execution time for n=100000000: 52805.3689 seconds
