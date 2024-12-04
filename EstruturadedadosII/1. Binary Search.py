def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid


        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


arr = [2, 3, 4, 10, 40, 67, 86, 107]
target = 67
result = binary_search(arr, target)

if result != -1:
    print(f"Elemento encontrado no índice {result}")
else:
    print("Elemento não encontrado na lista")