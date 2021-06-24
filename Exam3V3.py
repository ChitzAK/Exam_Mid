'''
Scrie un program care sa afiseze toate combinatiile de 2 litere dintre valorile dictionarului de mai jos.
dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}
'''


def combineunique_stringsof2() -> object:
    letters = ""
    listToStr = []
    dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}
    dictionar_nou = []

    for key, value in dictionar.items():
        # Adding all values to a single string:
        letters += value

        # Making all letters as an unique item from a list:
        x = list(set(letters))

        # Removed all duplicates from the letters:
        listToStr = ''.join(map(str, x))

        # Adding all combinations in a new dictionary and removing duplicates:
        for i in listToStr:
            for j in listToStr:
                dictionar_nou.append("{}{}".format(i, j))
        # Removing all duplicates from the list to make unique occurrences (if we remove this line code it will show
        # duplicates in the list also so they won't be unique and it will change the total nr. of occurrences to 844):
            dictionar_nou = list(dict.fromkeys(dictionar_nou))

    print(f"Added all values to a single string: ", letters)
    print(f"Made all letters as an unique item from a list: ", x)
    print(f"Made again the list into a string to have unique elements into the string: ", listToStr)
    print(f"Unique list of occurrences from dictionary with 2 letters: ", dictionar_nou)
    print(f"Total number of unique occurrences: ", len(dictionar_nou))

    return None

combineunique_stringsof2()
