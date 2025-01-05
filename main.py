def main():
    path = "./books/frankenstein.txt"
    book_text = load_book_text(path)
    words = count_words(book_text)
    chars = count_chars(book_text)
    print_report(words, chars)


def load_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(str):
    count = len(str.split())
    return count


def count_chars(str):
    characters = {}
    for char in str.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def convert_to_list(dict):
    lst = []
    for char in dict:
        lst.append({char: dict[char]})
    lst.sort(key=lambda item: list(item.values())[0], reverse=True)
    return lst


def print_report(word_count, char_dict):
    list_of_chars = convert_to_list(char_dict)

    print(f"╔═════════ Start report ═════════")
    print(f"║ Book contains {word_count} words\n║")
    for item in list_of_chars:
        char = list(item.keys())[0]
        count = list(item.values())[0]
        if char.isalpha():
            print(f"║  {char} is {count}")
    print(f"╚══════════ End report ══════════")


main()
