

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    #print(book_text)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

# It takes a filepath as input and returns the contents of the file as a string.
def get_book_text(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def count_words(input_text):
    words = input_text.split()
    return (len(words))
    


main()