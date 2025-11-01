🧩 1. Sort an Array of 0s, 1s, and 2s (Dutch National Flag)

Problem:
Given an array containing only 0s, 1s, and 2s, sort them without using any sorting algorithm.

Approach:
Use three pointers (low, mid, high).

def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

print(sortColors([2,0,2,1,1,0]))

🔢 2. Sort an Array Using Bubble Sort

Problem:
Implement bubble sort algorithm.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 25, 12, 22, 11]))

⚡ 3. Sort Using Selection Sort

Problem:
Implement the selection sort algorithm.

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([29, 10, 14, 37, 13]))

🚀 4. Sort Using Insertion Sort

Problem:
Implement insertion sort algorithm.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([12, 11, 13, 5, 6]))

🧮 5. Merge Sort

Problem:
Implement merge sort algorithm (Divide & Conquer).

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))

⚙️ 6. Quick Sort

Problem:
Implement quick sort algorithm using recursion.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([10, 7, 8, 9, 1, 5]))

📊 7. Counting Sort

Problem:
Sort an array of non-negative integers using Counting Sort.

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    return result

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))

⏱️ 8. Sort Characters by Frequency

Problem:
Given a string, sort characters by decreasing frequency.

from collections import Counter

def frequency_sort(s):
    count = Counter(s)
    sorted_chars = sorted(count.keys(), key=lambda x: (-count[x], x))
    return ''.join([ch * count[ch] for ch in sorted_chars])

print(frequency_sort("tree"))

💡 9. Sort by Number of Set Bits

Problem:
Sort integers by the number of 1s in their binary representation.

def sort_by_set_bits(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

print(sort_by_set_bits([0,1,2,3,4,5,6,7,8]))

🔍 10. Sort an Array of Strings by Length

Problem:
Sort an array of strings by their length (shortest to longest).

def sort_by_length(words):
    return sorted(words, key=len)

print(sort_by_length(["apple", "bat", "banana", "cat"]))
