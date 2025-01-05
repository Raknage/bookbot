def main():
    path = "./books/frankenstein.txt"
    book_text = load_book_text(path)
    count_words(book_text)
    count_chars(book_text)


def load_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(str):
    count = len(str.split())
    print(count)
    return count


def count_chars(str):
    characters = {}

    for char in str.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    print(characters)
    return characters


main()
