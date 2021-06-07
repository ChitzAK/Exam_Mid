#Ex1
taste1 = input("Tastati orice.\n")
nume = input("Numele:\n")

if taste1.isdigit():
    text1 = f"Sirul de numere a fost gasit de {nume}"
else:
    text1 = f"Sirul de caractere a fost gasit de {nume}"

print(text1)


#Ex2
taste2 = input("\nIntroduceti un numar intreg\n")

if taste2.isdigit():
    taste2 = int(taste2)
else:
    text2 = f"Nu s-a introdus un numar intreg"

if (taste2 % 2) == 0:
    text2 = f"Numarul introdus {taste2} este par"
else:
    text2 = f"Numarul introdus {taste2} este impar"

print(text2)


#Ex3
taste3 = input("\nIntroduceti un an calendaristic\n")

if taste3.isdigit():
    taste3 = int(taste3)
else:
    text3 = f"Nu s-a introdus corect anul"

if taste3 % 4 == 0:
    text3 = f"Anul introdus {taste3} este bisect"
else:
    text3 = f"Anul introdus {taste3} nu este bisect"

print(text3)


#Ex4
taste4 = input("\nIntroduceti un numar\n")

if taste4.isdigit():
    taste4 = float(taste4)
else:
    text4 = f"Nu s-a introdus corect numarul"

if (taste4 > 0) and (taste4 < 10):
    text4 = f"Numarul introdus {taste4} este pozitiv si mai mic decat 10"
elif (taste4 > 0) and (taste4 >= 10):
    text4 = f"Numarul introdus {taste4} este pozitiv si mai mare sau egal cu 10"
elif taste4 == 0:
    text4 = f"Numarul introdus {taste4} este 0"
else:
    taste4 = -taste4
    text4 = f"Numarul introdus este {taste4}"

print(text4)

#Ex5

meniu = (f"\n\t1 - Afisare lista de cumparaturi\n\t2 - Adaugare element\n\t3 - Stergere element\n\t"
         f"4 - Stergere lista de cumparaturi\n\t5 - Cautare in lista de cumparaturi\n\t")
print(meniu)

taste5 = input("Alegeti o optiune din meniu\n")

if taste5.isdigit():
    taste5 = int(taste5)
else:
    text5 = f"Nu s-au introdus cifre"

if taste5 == 1:
    text5 = f"1 - Afisare lista de cumparaturi"
elif taste5 == 2:
    text5 = f"2 - Adaugare element"
elif taste5 == 3:
    text5 = f"3 - Stergere element"
elif taste5 == 4:
    text5 = f"4 - Stergere lista de cumparaturi"
elif taste5 == 5:
    text5 = f"5 - Cautare in lista de cumparaturi"
else:
    text5 = f"Alegerea nu exista. Reincercati"

print(text5)