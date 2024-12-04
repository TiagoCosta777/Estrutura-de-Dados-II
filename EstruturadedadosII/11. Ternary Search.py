def ternary_search(arr, left, right, key):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, key)
        elif key > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, key)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, key)

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
key = 18
result = ternary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print(f"Elemento encontrado na posição {result}.")
else:
    print("Elemento não encontrado na lista.")