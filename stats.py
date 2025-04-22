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


def convert_to_sorted_list(dict):
    lst = []
    for c in dict:
        lst.append({"char": c, "count": dict[c]})
    lst.sort(key=lambda item: item["count"], reverse=True)
    return lst
