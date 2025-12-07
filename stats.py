def num_of_words(text):
    words = text.split() # splits the text into words
    return len(words)

def char_count(text):
    text = text.lower() # turns the text into lower case
    chars = {} # creates a dictionary to store the counts

    for char in text:
        if char in chars:
           chars[char] += 1
        else:
           chars[char] = 1
    return chars

def sort_on(item): # helper function which returns the num value of the dictionary
    return item["num"]

def sorted_list(char_dict):
    sorted_list = []

    for  char, count in char_dict.items():
         sorted_list.append({"char":char,"num":count})

    sorted_list.sort(reverse=True,key=sort_on) # Descending order

    return sorted_list
