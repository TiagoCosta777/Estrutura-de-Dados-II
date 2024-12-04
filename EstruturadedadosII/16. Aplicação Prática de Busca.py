def binary_search_books(library, target_isbn):
    left, right = 0, len(library) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_record = library[mid]

        if mid_record['ISBN'] == target_isbn:
            return mid_record

        if mid_record['ISBN'] < target_isbn:
            left = mid + 1
        else:
            right = mid - 1

    return None


#
library = [
    {"ISBN": "978-0131103627", "Title": "The C Programming Language", "Author": "Kernighan and Ritchie"},
    {"ISBN": "978-0201616224", "Title": "The Pragmatic Programmer", "Author": "Hunt and Thomas"},
    {"ISBN": "978-0321751041", "Title": "Introduction to Algorithms", "Author": "Cormen et al."},
    {"ISBN": "978-0596007126", "Title": "Head First Design Patterns", "Author": "Freeman and Robson"},
    {"ISBN": "978-1491950296", "Title": "Python Data Science Handbook", "Author": "Jake VanderPlas"}
]

target_isbn = "978-0321751041"
book = binary_search_books(library, target_isbn)

if book:
    print(f"Livro encontrado: {book['Title']} por {book['Author']}.")
else:
    print("Livro não encontrado.")
