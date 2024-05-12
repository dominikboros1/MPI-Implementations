import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [random.randint(1, 1000) for _ in range(100000)]

start_time = time.time()
bubble_sort(arr)
end_time = time.time()

print(arr)
print(end_time - start_time, "seconds")
