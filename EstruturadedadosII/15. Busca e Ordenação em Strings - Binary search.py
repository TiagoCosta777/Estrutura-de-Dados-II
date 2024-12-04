def binary_search(words, target):
    left, right = 0, len(words) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_word = words[mid]

        if mid_word == target:
            return mid

        if mid_word < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



sorted_words = ["abacaxi", "banana", "laranja", "maçã", "uva", "morango", "caqui", "melancia"]
target_word = "laranja"

index = binary_search(sorted_words, target_word)

if index != -1:
    print(f"A palavra '{target_word}' foi encontrada no índice {index}.")
else:
    print(f"A palavra '{target_word}' não está na lista.")
