# Pseuduo Code
# 1. Start from the second element (assume the first element is sorted)
# 2. Compare the current element with the previous elements.
# 3. If the current element is smaller than the previous element, we keep comparing with the elements before until we reach an element smaller, or reach the start of the array. Then we insert the current element in the correct position.
# 4. Repeat the process for each of the elements in the array.
# Time complexity: O(n^2)
# Auxiliary space: O(1)


# Implementation
import numpy as np
import timeit
class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    def get_sorted_array(self):
        return self.arr

# Usage:
n_values = [10**2, 10**3, 10**4, 10**5] 
for n in n_values:
    arr = np.random.randint(0, 100, size=n)
    sorter = InsertionSort(arr)
    exec_time = timeit.timeit(f"sorter.sort()", globals=globals(), number=1)
    print(f"Execution time for n={n}: {exec_time:.4f} seconds")

# Running time
# Execution time for n=100: 0.0005 seconds
# Execution time for n=1000: 0.0489 seconds
# Execution time for n=10000: 4.7205 seconds
# Execution time for n=100000: 466.2660 seconds



