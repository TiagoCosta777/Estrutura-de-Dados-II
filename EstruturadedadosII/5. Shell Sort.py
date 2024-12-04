def shell_sort(arr, sequencia_gap):
    n = len(arr)

    gaps = sequencia_gap(n)

    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

    return arr


def sequencia_shell(n):
    gaps = []
    gap = n // 2
    while gap > 0:
        gaps.append(gap)
        gap //= 2
    return gaps


def sequencia_hibbard(n):
    gaps = []
    k = 1
    while (2 ** k - 1) < n:
        gaps.insert(0, 2 ** k - 1)
        k += 1
    return gaps


def sequencia_knuth(n):
    gaps = []
    k = 1
    while (3 ** k - 1) // 2 < n:
        gaps.insert(0, (3 ** k - 1) // 2)
        k += 1
    return gaps


arr = [19, 2, 31, 45, 6, 11, 121, 27, 30, 55, 22, 2, 20]

print("Array original:", arr)
array_ordenado_shell = shell_sort(arr.copy(), sequencia_shell)
print("Array ordenado com sequência de Shell:", array_ordenado_shell)

# Sequência de Hibbard
array_ordenado_hibbard = shell_sort(arr.copy(), sequencia_hibbard)
print("Array ordenado com sequência de Hibbard:", array_ordenado_hibbard)

# Sequência de Knuth
array_ordenado_knuth = shell_sort(arr.copy(), sequencia_knuth)
print("Array ordenado com sequência de Knuth:", array_ordenado_knuth)
