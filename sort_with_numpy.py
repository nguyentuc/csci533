import numpy as np
import time
import random

# call heap sort from numpy
def run_heap_sort(arr):
    np.sort(arr, kind='heapsort')

# call quick sort from numpy
def run_quicK_sort(arr):
    np.sort(arr, kind='quick')

if __name__ == '__main__':
    n_values = [10**2, 10**3, 10**4, 10**5, 10**6,10**7, 10**8,10**9]
    for n in n_values:
        arr = np.random.randint(0, 100, size=n)
        start_time_heap = time.time()
        run_heap_sort(arr)
        end_time_heap = time.time()
        exec_time = end_time_heap-start_time_heap
        print(f"HeapSort Execution time for n={n}: {exec_time:.4f} seconds")

        start_time_quick = time.time()
        run_quicK_sort(arr)
        end_time_quick= time.time()
        quick_exec_time = end_time_quick- start_time_quick
        print(f"QuickSort Execution time for n={n}: {quick_exec_time:.4f} seconds")

# HeapSort Execution time for n=100: 0.0000 seconds
# QuickSort Execution time for n=100: 0.0000 seconds
# HeapSort Execution time for n=1000: 0.0001 seconds
# QuickSort Execution time for n=1000: 0.0000 seconds
# HeapSort Execution time for n=10000: 0.0006 seconds
# QuickSort Execution time for n=10000: 0.0003 seconds
# HeapSort Execution time for n=100000: 0.0076 seconds
# QuickSort Execution time for n=100000: 0.0030 seconds
# HeapSort Execution time for n=1000000: 0.0531 seconds
# QuickSort Execution time for n=1000000: 0.0232 seconds
# HeapSort Execution time for n=10000000: 0.8256 seconds
# QuickSort Execution time for n=10000000: 0.2275 seconds
# HeapSort Execution time for n=100000000: 10.0117 seconds
# QuickSort Execution time for n=100000000: 2.1757 seconds
# HeapSort Execution time for n=1000000000: 102.2400 seconds
# QuickSort Execution time for n=1000000000: 22.8555 seconds