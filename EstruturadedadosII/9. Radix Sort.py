def counting_sort(arr, exp):
    n = len(arr)

    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


arr1 = [170, 45, 75, 90, 802, 24, 2, 66]
arr2 = [12345, 6789, 54321, 98765, 43210]
arr3 = [1234567890, 987654321, 12345678, 87654321]

print("Array original (2-3 dígitos):", arr1)
radix_sort(arr1)
print("Array ordenado:", arr1)

print("Array original (5 dígitos):", arr2)
radix_sort(arr2)
print("Array ordenado:", arr2)

print("Array original (8-10 dígitos):", arr3)
radix_sort(arr3)
print("Array ordenado:", arr3)