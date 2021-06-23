'''
Scrie un program care sa afiseze toate combinatiile de 2 litere dintre valorile dictionarului de mai jos.
'''

dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}


def combineunique_stringsof2():
    letters = ""

    # Adding all values to a single string:
    for key, value in dictionar.items():
        letters += value
        print(letters)

    # Making all letters as an unique item from a list:
    x = list(set(letters))
    print(x)

    # Still have to add items one by one to make unique elements:
    for a, b in enumerate(x):
        x[a:a + 1] = [''.join(x[a:a + 1])]
    print(x)


combineunique_stringsof2()
