def sort_on(characters):
    return characters["num"]

def get_num_words(text):
    count = len(text.split())
    return count

def get_character_count(text):
    characters = {}

    for character in text:
        lower_case_character = character.lower()
        if lower_case_character in characters:
            characters[lower_case_character] += 1
        else:
            characters[lower_case_character] = 1
        
    return characters

def create_character_dictionaries(main_characters_dictionary):
    dictionary_list = []
    for key in main_characters_dictionary:
        new_dictionary = {"char": key, "num": main_characters_dictionary[key]}
        print(new_dictionary)
        dictionary_list.append(new_dictionary)
    
    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list