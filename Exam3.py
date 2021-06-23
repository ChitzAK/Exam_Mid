'''
Scrie un program care sa afiseze toate combinatiile de 2 litere dintre valorile dictionarului de mai jos.
'''

dictionar = {"1":"abc", "2":"s", "3":"o", "4":"n", "5":"lm", "6": "jk", "7":"gi", "8":"def", "9":"abc"}

for key, value in dictionar.items():
    if len(value) == 2:
        print (key, value)
