def count_words(text):
    words = text.split()

    word_count = 0

    for word in words:
        word_count += 1

    return word_count

def count_characters(text):
    lower_case = text.lower()

    char_dict = {}

    for char in lower_case:
         if char not in char_dict:
              char_dict[char] = 1

         else:
              char_dict[char] += 1

    return char_dict








