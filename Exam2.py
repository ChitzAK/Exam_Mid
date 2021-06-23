'''
Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana
cand lista devine goala.
'''


def remove3_by3():
    Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    while len(Lista) > 0:
        for x, y in enumerate(Lista):
            if x % 3 == 0:
                Lista.pop(x)
                print(y)
                print(Lista)
    return None


remove3_by3()
