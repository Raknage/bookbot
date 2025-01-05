def main():
    path = "./books/frankenstein.txt"
    count_words(load_book_text(path))


def load_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(str):
    count = len(str.split())
    print(count)
    return count


main()
