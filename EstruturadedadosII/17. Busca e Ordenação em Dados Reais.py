def bucket_sort(grades):

    num_buckets = 10
    max_grade = 100
    buckets = [[] for _ in range(num_buckets)]


    for grade in grades:
        index = int((grade / max_grade) * (num_buckets - 1))
        buckets[index].append(grade)


    sorted_grades = []
    for bucket in buckets:
        sorted_grades.extend(sorted(bucket))

    return sorted_grades


def interpolation_search(grades, target):
    low = 0
    high = len(grades) - 1

    while low <= high and grades[low] <= target <= grades[high]:
        pos = low + int((target - grades[low]) * (high - low) / (grades[high] - grades[low]))

        if grades[pos] == target:
            return pos
        if grades[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1



grades = [95, 40, 85, 67, 76, 89, 53, 45, 100, 20]

# Ordena as notas usando Bucket Sort
print("Ordenando as notas com Bucket Sort...")
sorted_grades = bucket_sort(grades)
print("Notas ordenadas:", sorted_grades)


target_grade = 76
print(f"\nProcurando a nota {target_grade} com Interpolation Search...")
index = interpolation_search(sorted_grades, target_grade)

if index != -1:
    print(f"Nota {target_grade} encontrada no índice {index}.")
else:
    print(f"Nota {target_grade} não encontrada.")
