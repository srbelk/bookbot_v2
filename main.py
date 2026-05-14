from stats import count_words, count_characters

def main():
    def get_book_text():
       with open("books/frankenstein.txt", encoding="utf-8", newline="") as book:
            return book.read()

    book_string = get_book_text()

    print(f"Found {count_words(book_string)} total words")

    characters = count_characters(book_string)

    print(characters)
main()

