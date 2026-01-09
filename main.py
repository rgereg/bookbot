from stats import count_words
from stats import count_chars
book = "./books/frankenstein.txt"


def main():


    book_text = get_book_text(book)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    stats = count_chars(book_text)
    
def get_book_text(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

main()