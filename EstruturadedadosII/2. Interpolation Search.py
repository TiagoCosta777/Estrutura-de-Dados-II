def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1

        pos = left + ((target - arr[left]) * (right - left) // (arr[right] - arr[left]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return -1

arr_uniform = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
arr_non_uniform = [5, 7, 9, 23, 25, 28, 31, 43, 48, 50]

target = 90

print("Busca em lista uniforme:")
result_uniform = interpolation_search(arr_uniform, target)
if result_uniform != -1:
    print(f"Elemento encontrado no índice {result_uniform}")
else:
    print("Elemento não encontrado na lista")

print("Busca em lista não uniforme:")
result_non_uniform = interpolation_search(arr_non_uniform, target)
if result_non_uniform != -1:
    print(f"Elemento encontrado no índice {result_non_uniform}")
else:
    print("Elemento não encontrado na lista")