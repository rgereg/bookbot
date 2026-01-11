
# Take an input string and return the number of words contained
def count_words(input_text):
    words = input_text.split()
    return (len(words))

# takes the text from the book as a string, and returns the number of times each character, 
# (including symbols and spaces), appears in the string.
# Return a dictionary of letters and counts
def count_chars(input_text):
    #convert full text to lower case
    lower_text = input_text.lower()

    #create an empty dict for counting
    counter_text = {}

    # loop through the text and add characters/counts to the dictionary
    for letter in lower_text:
        if letter in counter_text:
            counter_text[letter] +=1
            #print(counter_text[letter])
        else:
            counter_text[letter] = 1
            #print(counter_text[letter])
    return counter_text


def counter(input_dict):
    list_of_dicts = []
    for entry in input_dict:
        #print(f"{entry}: {input_dict[entry]}")
        list_of_dicts.append({entry: input_dict[entry]})
    return list_of_dicts