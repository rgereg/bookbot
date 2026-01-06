from stats import count_words

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    #print(book_text)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")


def get_book_text(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


    


main()