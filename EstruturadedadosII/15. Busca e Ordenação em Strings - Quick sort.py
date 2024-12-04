def quick_sort(words):
    if len(words) <= 1:
        return words

    pivot = words[0]
    less_than_pivot = [word for word in words[1:] if word <= pivot]
    greater_than_pivot = [word for word in words[1:] if word > pivot]

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



words = ["banana", "maçã", "laranja", "uva", "abacaxi"]
sorted_words = quick_sort(words)
print(sorted_words)
