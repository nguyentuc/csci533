import threading
import timeit
import numpy as np

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# do heap sort on the the two subarray
def heap_sort_subarray(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# do pararrel sorting
def parallel_heap_sort(arr):
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # use two thread: one for the left list and other for right list
    left_thread = threading.Thread(target=heap_sort_subarray, args=(left_arr, len(left_arr)))
    right_thread = threading.Thread(target=heap_sort_subarray, args=(right_arr, len(right_arr)))

    left_thread.start()
    right_thread.start()

    # merge the results together
    left_thread.join()
    right_thread.join()

    left_ptr, right_ptr, merged = 0, 0, []
    while left_ptr < len(left_arr) and right_ptr < len(right_arr):
        if left_arr[left_ptr] < right_arr[right_ptr]:
            merged.append(left_arr[left_ptr])
            left_ptr += 1
        else:
            merged.append(right_arr[right_ptr])
            right_ptr += 1

    merged.extend(left_arr[left_ptr:])
    merged.extend(right_arr[right_ptr:])
    return merged


def run_quick_sort(n):
    arr = np.random.randint(0, 100, size=n)
    parallel_heap_sort(arr)

if __name__ == '__main__':
    n_values = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9] 
    for n in n_values:
        exec_time = timeit.timeit(f"run_quick_sort({n})", globals=globals(), number=1)
        print(f"Execution time for n={n}: {exec_time:.4f} seconds")
