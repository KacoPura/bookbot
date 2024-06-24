def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars_dict(chars_dict)
    print_report(book_path, num_words, sorted_chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for i in text:
        lowered = i.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars_dict(chars_dict):
    # Convert dictionary to list of dictionaries for sorting
    chars_list = [{"char": char, "num": count} for char, count in chars_dict.items()]
    # Sort the list of dictionaries by the "num" key in descending order
    chars_list.sort(reverse=True, key=lambda d: d["num"])
    return chars_list

def print_report(book_path, num_words, sorted_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char_info in sorted_chars:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()