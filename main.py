def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    print(char_dict)


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

main()