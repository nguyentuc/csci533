import timeit
import random

def heapify(arr, n, i):
    largest = i  # Root is the largest one
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # when left child of root exists and is bigger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # when right child of root exists and is bigger than the biggest ones
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Change root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 

        # do heapify with new root.
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def run_heap_sort(n):
    arr = [random.randint(0, 100) for _ in range(n)]
    heapSort(arr)

if __name__ == '__main__':
    n_values = [10**2, 10**3, 10**4, 10**5, 10**6,10**7, 10**8,10**9] 
    for n in n_values:
        exec_time = timeit.timeit(f"run_heap_sort({n})", globals=globals(), number=1)
        print(f"Execution time for n={n}: {exec_time:.4f} seconds")

# Execution time for n=100: 0.0002 seconds
# Execution time for n=1000: 0.0021 seconds
# Execution time for n=10000: 0.0275 seconds
# Execution time for n=100000: 0.3506 seconds
# Execution time for n=1000000: 4.3138 seconds
# Execution time for n=10000000: 50.9411 seconds
# Execution time for n=100000000: 593.0884 seconds
# Execution time for n=1000000000: 6514.0786 seconds
