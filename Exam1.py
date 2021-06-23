'''
Scrie un program care sa calculeze suma dintre trei numere. Daca valorile sunt egale,
returnati de trei ori suma acestora.
'''


def sum_3nr():
    listof_numbers = str(input('Enter 3 numbers separated by space: '))
    z = list(map(int, listof_numbers.split()))
    a = z[0]
    b = z[1]
    c = z[2]
    x = a + b + c
    if a == b == c:
        x = 3 * x

    return print(x)


sum_3nr()

