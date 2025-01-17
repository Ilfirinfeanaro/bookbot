def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text) no need for the full text
    number_words = words_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_words} words found in the document \n")
    number_characters = character_count(text)
    # print(number_characters) no need for the full characters count dictionnary
    character_sorted = sort_character(number_characters)
    for item in character_sorted:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")

def words_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_number = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character in character_number:
            character_number[character] += 1
        else:
            character_number[character] = 1
    return character_number

def sort_on(dict):
    return dict["num"]

def sort_character(dict):
    char_list = []
    for char in dict:
        if char.isalpha():
            char_list.append({"char": char, "num": dict[char]})
    char_list.sort(reverse = True, key = sort_on)
    return char_list


def get_book_text(path):
    with open(path) as f:
        return f.read()




main()