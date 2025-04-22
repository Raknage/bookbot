from stats import count_words, count_chars, convert_to_sorted_list
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = load_book_text(path)
    words = count_words(book_text)
    chars = count_chars(book_text)
    print_report(words, chars)


def load_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(word_count, char_dict):
    list_of_chars = convert_to_sorted_list(char_dict)

    print(f"╔═════════ Start report ═════════")
    print(f"║ {word_count} words found in the document\n║")

    for item in list_of_chars:
        if item["char"].isalpha():
            print(f"║  {item["char"]}: {item["count"]}")

    print(f"╚══════════ End report ══════════")


main()
