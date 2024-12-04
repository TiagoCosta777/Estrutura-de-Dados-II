def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def exponential_search(arr, target):
    n = len(arr)

    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return binary_search(arr, i // 2, min(i, n - 1), target)


arr = [2, 3, 4, 10, 40, 50, 70, 80, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
target = 140

result = exponential_search(arr, target)

if result != -1:
    print(f"Elemento encontrado no índice {result}")
else:
    print("Elemento não encontrado na lista")