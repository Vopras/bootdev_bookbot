
def get_book_text(path):
    text = ''
    with open(path) as f:
        text = f.read()
    return text

def get_nr_of_words(text):
    number = 0
    number = len(text.split())
    return number

def get_nr_of_letters(text):
    lower_case_text = text.lower()
    result = {}
    for letter in lower_case_text:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

def sort_on(dictionary):
    return dictionary[1]

def sort_dictionary(dictionary):
    items_list = list(dictionary.items())
    items_list.sort(key=sort_on, reverse=True)
    return items_list

def print_report(path):
    text = get_book_text(path)
    number_of_words = get_nr_of_words(text)
    dictionary = get_nr_of_letters(text)
    sorted_dictionary = sort_dictionary(dictionary)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {number_of_words} total words')
    print('--------- Character Count -------')
    for character in sorted_dictionary:
        if character[0].isalpha():
            print(f'{character[0]}: {character[1]}')
    print('============= END ===============')
