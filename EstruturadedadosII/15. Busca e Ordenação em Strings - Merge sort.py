def merge_sort(words):
    if len(words) <= 1:
        return words

    mid = len(words) // 2
    left_half = merge_sort(words[:mid])
    right_half = merge_sort(words[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list



words = ["banana", "maçã", "laranja", "uva", "abacaxi"]
sorted_words = merge_sort(words)
print(sorted_words)
