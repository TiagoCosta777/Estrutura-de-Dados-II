def quick_sort_first(arr, low, high):
    if low < high:
        pi = partition_first(arr, low, high)
        quick_sort_first(arr, low, pi - 1)
        quick_sort_first(arr, pi + 1, high)

def partition_first(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quick_sort_last(arr, low, high):
    if low < high:
        pi = partition_last(arr, low, high)
        quick_sort_last(arr, low, pi - 1)
        quick_sort_last(arr, pi + 1, high)

def partition_last(arr, low, high):
    pivot = arr[high]
    left = low
    right = high - 1
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[high], arr[left] = arr[left], arr[high]
    return left

def quick_sort_middle(arr, low, high):
    if low < high:
        pi = partition_middle(arr, low, high)
        quick_sort_middle(arr, low, pi - 1)
        quick_sort_middle(arr, pi + 1, high)

def partition_middle(arr, low, high):
    mid = (low + high) // 2
    pivot = arr[mid]
    arr[mid], arr[low] = arr[low], arr[mid]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def print_quick_sort(arr, sort_func):
    print("Array original:", arr)
    sort_func(arr, 0, len(arr) - 1)
    print("Array ordenado:", arr)
    print("-" * 40)

arr1 = [10, 7, 8, 9, 1, 5, 7, 15]
arr2 = [10, 7, 8, 9, 1, 5, 7, 15]
arr3 = [10, 7, 8, 9, 1, 5, 7, 15]

print("Usando o primeiro elemento como pivô:")
print_quick_sort(arr1, quick_sort_first)

print("Usando o último elemento como pivô:")
print_quick_sort(arr2, quick_sort_last)

print("Usando o elemento do meio como pivô:")
print_quick_sort(arr3, quick_sort_middle)