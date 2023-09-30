import numpy as np
from scipy.optimize import curve_fit
import time
import random
from heap_sort import heapSort

def heapSort_time(n):
    arr = [random.randint(0, n) for _ in range(n)]
    start_time = time.time()
    heapSort(arr)
    return time.time() - start_time

# Define the models for time complexity
def heap_model(n, c):
    return c * n * np.log(n)


# Define the models for time complexity
def heap_model(n, c):
    return c * n * np.log(n)
heap_times = np.array([heapSort_time(n) for n in ns])
heap_params, _ = curve_fit(heap_model, ns, heap_times)
print(f'Heap Sort constant: {heap_params[0]:.6f}')
