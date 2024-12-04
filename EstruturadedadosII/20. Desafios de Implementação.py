import math


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bucket_sort(arr):
    num_buckets = 10
    max_value = max(arr)
    buckets = [[] for _ in range(num_buckets)]
    for value in arr:
        index = int((value / max_value) * (num_buckets - 1))
        buckets[index].append(value)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    return output


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    return -1


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr[:min(i, n)], target)


def ternary_search(arr, target, left, right):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            return ternary_search(arr, target, left, mid1 - 1)
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, right)
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)
    return -1


def main():
    while True:
        print("\n*** Escolha uma opção ***")
        print("1. Ordenar uma lista")
        print("2. Procurar um elemento")
        print("3. Sair")

        choice = int(input("Digite sua escolha: "))

        if choice == 1:
            print("\n*** Algoritmos de Ordenação ***")
            print("1. Shell Sort")
            print("2. Merge Sort")
            print("3. Quick Sort")
            print("4. Selection Sort")
            print("5. Bucket Sort")
            print("6. Radix Sort")
            algo_choice = int(input("Escolha o algoritmo de ordenação: "))
            arr = list(map(int, input("Digite a lista de números separados por espaço: ").split()))

            if algo_choice == 1:
                print("Lista ordenada:", shell_sort(arr))
            elif algo_choice == 2:
                print("Lista ordenada:", merge_sort(arr))
            elif algo_choice == 3:
                print("Lista ordenada:", quick_sort(arr))
            elif algo_choice == 4:
                print("Lista ordenada:", selection_sort(arr))
            elif algo_choice == 5:
                print("Lista ordenada:", bucket_sort(arr))
            elif algo_choice == 6:
                print("Lista ordenada:", radix_sort(arr))

        elif choice == 2:
            print("\n*** Algoritmos de Busca ***")
            print("1. Binary Search")
            print("2. Interpolation Search")
            print("3. Jump Search")
            print("4. Exponential Search")
            print("5. Ternary Search")
            algo_choice = int(input("Escolha o algoritmo de busca: "))
            arr = sorted(list(map(int, input("Digite a lista de números ordenada separados por espaço: ").split())))
            target = int(input("Digite o número a ser procurado: "))

            if algo_choice == 1:
                index = binary_search(arr, target)
            elif algo_choice == 2:
                index = interpolation_search(arr, target)
            elif algo_choice == 3:
                index = jump_search(arr, target)
            elif algo_choice == 4:
                index = exponential_search(arr, target)
            elif algo_choice == 5:
                index = ternary_search(arr, target, 0, len(arr) - 1)

            if index != -1:
                print(f"Elemento encontrado no índice {index}.")
            else:
                print("Elemento não encontrado.")

        elif choice == 3:
            print("Saindo do programa...")
            break


if __name__ == "__main__":
    main()
