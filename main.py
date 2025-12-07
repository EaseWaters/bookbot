import sys

from stats import num_of_words, char_count, sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    if len(sys.argv)!= 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

    book_path = sys.argv[1]

    print("=================== BOOKBOT ===================")
    print(f"Analyzing book found at {book_path}...")

    book_text = get_book_text(book_path)
    num_words = num_of_words(book_text)

    print("------------------- Word Count ----------------")
    print(f"Found {num_words} total words")


    char_counts = char_count(book_text)
    print("---------------- Character Count ---------------")
    sorted_char = sorted_list(char_counts)

    for item in sorted_char:
        char = item["char"]
        num = item["num"]

        if not char.isalpha(): # skips the non alphabetical characters
               continue
        print(f"{char}: {num}")
    print("=========== END ===========")

main() 
