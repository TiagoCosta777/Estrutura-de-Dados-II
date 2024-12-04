def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Iteração {i + 1}: {arr}")

arr = [64, 25, 12, 22, 11, 69, 77, 80, 25, 11]
print("Array original:", arr)
selection_sort(arr)
print("Array ordenado:", arr)