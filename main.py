import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

array_sizes = [100, 1000]
results = {}

for size in array_sizes:
    
    arr = [random.randint(1, 10000) for _ in range(size)]
    merge_time = timeit.timeit('merge_sort(arr.copy())', globals=globals(), number=1)
    insertion_time = timeit.timeit('insertion_sort(arr.copy())', globals=globals(), number=1)
    timsort_time = timeit.timeit('sorted(arr)', globals=globals(), number=1)

    results[size] = {'Merge Sort': merge_time, 'Insertion Sort': insertion_time, 'Timsort': timsort_time}

def show_results():
    for key in results:
        print ("%s -> %s" % (key, results[key]))
show_results()        