import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [random.randint(1, 2) for _ in range(100000)]

start_time = time.time()
insertion_sort(arr)
end_time = time.time()

print(arr)
print(end_time - start_time, "seconds")
