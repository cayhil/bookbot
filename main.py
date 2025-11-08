import sys
from stats import get_num_words, get_character_count, create_character_dictionaries

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    character_count = get_character_count(text)
    character_list = create_character_dictionaries(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # print(character_count)
    # print(character_list)
    for character in character_list:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")


main()