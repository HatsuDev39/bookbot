def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

    word_count = 0
    words = file_contents.split()
    for word in words:
        word_count += 1
    print(word_count)
main()