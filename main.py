

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(book_text)


# It takes a filepath as input and returns the contents of the file as a string.
def get_book_text(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()
    
    # file_contents = filepath

    return file_contents


main()