import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [random.randint(1, 100000) for _ in range(100000)]

start_time = time.time()
selection_sort(arr)
end_time = time.time()

print(arr)
print(end_time - start_time, "seconds")
