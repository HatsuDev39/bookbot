def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    sorted_dict = sort_char_dict(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in this document")
    print()

    for item in sorted_dict:
        print(f"The {item["character"]} character was found {item["count"]} times")

    print("--- End of report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
  
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    char = {}
    for c in text:
        lowered = c.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1
    return char

def sort_on(d):
    return d["count"]

def sort_char_dict(char_dict):
    new_list = []
    for char in char_dict:
        sorted_dict = {}
        if char.isalpha():
            sorted_dict["character"] = char
            sorted_dict["count"] = char_dict[char]
            new_list.append(sorted_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

main()