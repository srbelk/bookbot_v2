from stats import count_words, count_characters, sorted_dict_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
       with open(sys.argv[1]) as book:
            return book.read()

def main():
    book_string = get_book_text()

    characters = count_characters(book_string)

    sorted_characters = sorted_dict_list(characters)

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")

    print(f"Found {count_words(book_string)} total words")

    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")
main()

