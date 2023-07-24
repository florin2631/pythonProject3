"""
Module
"""
# ==================================================================
# ==================== IMPORTAREA MODULELOR ========================
#
# # Varianta 1 de import (*) - da import la tot din fisierul mentionat
# from pachet_functii.functii_liste import *
#
# # Varianta 2 de import - alias la numele original (optional)
# import pachet_functii.functii_string as string_methods
#
# # Varianta 3 de import - importarea functiilor necesare
# from pachet_functii.functii_int import nr_pare
#
# #
# # Afiseaza metodele care fac parte din modulul specificat ca parametru
# print(dir(string_methods))
#
# #
# # # Apelarea variantei 1 de import
# print(transformare_majuscule(["Dana", 1, "Maria", "text", 4.5]))
# print(numar_ocurenta(["a","b","b","c","g","d",5,"5","5"],"b"))
# #
# # # Apelarea variantei 2 de import
# print(string_methods.majuscule("Abracadabra"))
# print(string_methods.numaratoare_litera("Ana are mere","e"))
# print(string_methods.minuscule("CuVAnT"))
# #
# # # Apelarea variantei 3 de import
# print(nr_pare(5,12,56,23,77,68))

# ==================================================================
# ===================== MODULE FOLOSITOARE =========================
#
# modulul math - Functii matematice
# import math
#
# for i in dir(math):
#     print(i)
#
# # Modulul platform - explorarea stratului de OS
# import platform
#
# for i in dir(platform):
#     print(i)
#
# print(platform.uname())
# print(platform.platform())
# print(platform.version())
# print(platform.python_version())

# # Modulul random - generarea numerelor pseudo-aleatorii
# import random
#
# for i in dir(random):
#     print(i)
#
# lista1 = ["Ana","Mihai","Maria","Bianca","Alex"]
# print(random.choice(lista1))            # alege un element random din lista
# print(random.choices(lista1,k=2))       # alege k elemente random din lista
#
# print(random.random())                  # nr random intre 0 si 1
# print(random.randint(5,10))             # nr random intre 5 si 10
# print(random.randrange(1,100,2))        # nr impare in intervalul 1-100
#
# # Exemplu dictionar 1
# dict1 = {
#     "preturi": (30,40,50),
#     "oameni": ["Ana","Mihai"]
# }
#
#
# # extrage cheile sub forma de lista intr-o variabila
# lista_chei = list(dict1.keys())
#
# # alege cheia din lista_chei in mod random
# random1 = random.choice(lista_chei)
#
# # afiseaza valoarea asicoata cu cheia aleasa in mod aleatoriu anterior
# print(dict1[random1])
#
# # alege in mod aleatoriu un element din valorile asociate cu cheia aleasa random anterior
# print(random.choice(dict1[random1]))
import random

"""
Siruri
"""
#
# # ASCII SI UNICODE
# print(ord(" "))     # afiseaza nr asociat cu caracterul in tabelul ASCII
# print(chr(33))      # afiseaza caracterul asociat cu numarul din tabela
# #
# print(min("Timisoara"))     # afiseaza caracterul asociat cu cel mai mic nr din tabela
# print(max("Timisoara"))     # afiseaza caracterul asociat cu cel mai mare nr din tabela
#
#
# # # Metode de siruri
# # for i in dir(str):
# #     print(i)
# #
# string1 = "TimiSoaRa"
#
# # Metode care returneaza copii ale sirului, modificand valoarea acestora
# print(string1.count('i'))           # returneaza nr de ocurenta a caracterului i in string1

# print(string1.capitalize())         # returneaza sirul cu prima litera mare
# print(string1.upper())              # returneaza sirul cu majuscule
# print(string1.lower())              # returneaza sirul cu minuscule
# print(string1.swapcase())           # returneaza un sir cu majusculele inversate cu minuscule si invers
# print(string1)

# print(string1.find('mi'))           # returneaza indexul la care s-a gasit sirul mentionat
# print(string1.find('i',2))          # returneaza indexul la care s-a gasit sirul, incepand cautarea de la indexul 2

# print(string1.lstrip("mTi"))        # returneaza sirul cu literele mentionate in sir taiate din stanga
# print(string1.rstrip("aR"))         # returneaza sirul cu literele mentionate in sir taiate din dreapta
#
# print(string1.replace("Tim","Ort")) # returneaza sirul inlocuind "Tim" cu "Ort"
#
# # Metode de verificare care returneaza True/ False
# print(string1.endswith('Ra'))   # returneaza True daca sirul se termina in sirul mentionat
# print(string1.startswith('T'))  # True daca sirul incepe cu T, False altfel
#
# print(string1.isalpha())        # True daca sirul este compus din litere, False altfel
# print(string1.isdigit())        # True daca sirul este compus din cifre, False altfel
# print(string1.isalnum())        # True daca sirul este compus din litere si cifre, False altfel
# print(string1.isupper())        # True daca sirul este compus din majuscule, False altfel
# print(string1.islower())        # true daca sirul este compus din litere mici
# print(string1.isspace())        # True daca sirul este compus din spatii, False altfel

# # Metode de separare si impreunare a sirurilor
# print(string1.split("i"))           # returneaza o lista, delimitand elementele in functie de i
# print("".join(["T","i","m","i"]))   # returneaza un sir, impreunand elementele din lista data folosind un sir gol
# print(",".join(["T","i","m","i"]))
# print(list(string1))                # returneaza sirul de caractere ca lista
#
# # Compararea sirurilor
# str1 = "Timisoara"
# str2 = "timisoara"
#
# print(str1 == str2)         # compara sirurile in functie de suma ord(caracter) din sir
# print(str1 > str2)

"""
Liste
"""
# lista1 = ['a', 'b', 5, 6.7, 'a', 'b']
# lista2 = ['b', 'c', 'a', 'b']
#
# for i in dir(list):
#     print(i)
#
# # Metode care NU AU VALORI DE RETURN => print() asupra functiilor va returna None/ eroare
# lista1.append('3')            # adauga elementul specificat in dreapta listei
# print(lista1)
# #
# lista1.remove('a')              # sterge prima ocurenta a parametrului specificat din lista
# print(lista1)
# #
# lista1.clear()                  # elimina toate elementele din lista
# print(lista1)
# #
# lista1.extend(['a','b',5,6.7,'a','b'])      # extinde lista cu elementele date ca parametru
# print(lista1)
# #
# lista1.insert(2,'x')            # adauga la indexul 2, elementul 'x'
# print(lista1)
# #
# lista1.reverse()                # inverseaza elementele listei
# print(lista1)
#
# lista1.sort()                   # sorteaza lista cu elementele de acelasi tip de data
# print(lista1)
#
# # Metode cu valori de return
# print(lista1.pop())         # returneaza ultimul element din dreapta si il elimina din lista
# print(lista1)
#
# print(lista1.count('b'))    # returneaza numarul de ocurenta a parametrului in lista
# print(lista1.index('b'))    # returneaza primul index la care se gaseste parametrul dat
# print(lista1.index('b',2))  # returneaza primul index la care se gaseste parametrul dat, incepand cautarea de indexul dat

"""
Exceptii
"""

# Exemplu 1
# try:
#     print("Incepe programul")
#     lst = []
#     print(lst[0])
#     print("Se extrage din lst elementul 0...")
# except IndexError:
#     print("Nu exista elementul 0 in lista")
#
# print("Continuam totusi executia programului")

# # Exemplu 2
# lst = [1,2,3,4]
# while True:
#     print("Lista este: ", lst)
#     x = input("introduceti un numar: ")
#     try:
#         x = int(x)
#         element = lst[x]
#         print(f"Se extrage din lst elementul {x}...")
#     except IndexError:
#         print(f"Nu exista indexul {x} in lista")
#     except ValueError:
#         print("X-ul nu este corect. Incercati din nou.")
#     else:
#         print(f"S-a reusit extragerea elementului de la pozitia {x}.")
#         print(f"Elementul este: {element}")
#         break

# # IndexError
# list1 = []
#
# try:
#     print(list1[0])
# except IndexError:
#     print("Lista nu are lungimea necesara.")

#
# # KeyError
# dict1 = {}
#
# try:
#     print(dict1['a'])
# except KeyError:
#     print("Dictionarul nu contine cheia mentionata")


# # ZeroDivision
# numar = 0
# try:
#     print(100/numar)
# except ZeroDivisionError:
#     print("Numarul nu poate fii impartit la 0.")
#
# # ValueError
# sir = '12a'
# try:
#     sir = int(sir)
# except ValueError:
#     print("Format incorect.")
# #
# # # TypeError
# sir = "1"
# numar = 1
# try:
#     print(sir + numar)
# except TypeError:
#     print("Nu se pot concatena aceste tipuri de date")


# # AssertionError = continua executia daca conditia este evaluata ca True

import sys

# # Exemplu1 = oprirea executiei
# x = 5
# y = 0
#
# try:
#     # if y > 0:
#     #     trece la else
#     assert y > 0, "Y trebuie sa fie mai mare de 0."
#     rez = x / y
# except AssertionError as ae:
#     print(ae)
# # optionala / nu se ajunge niciodata la exceptia asta
# except ZeroDivisionError:
#     print("Impartire la 0 nepermisa.")
# else:
#     print(rez)
#
# # Exemplu 2:
# x = 5
# y = 0
# assert y > 0, "Y trebuie sa fie mai mare de 0."



# ============== RAISE ================
# =====================================
# Exemplu: Se cere un script care sa calculeze cati ani va împlini utilizatorul
# în anul 2034, în funcție de input-ul acestuia cu anul nașterii
# #
# an = input("Introduceti anul nasterii: ")
#
# try:
#     an = int(an)
#     if an not in range(1900,2034):
#         raise Exception("Anul nu se afla in intervalul admis.")
# except ValueError:
#     print("Nu ati introdus un format corect.")
# except Exception as e:
#     print(e)
# else:
#     print(f"In anul 2034 veti avea: {2034 - an} ani.")


# # Varianta cu exceptii
# def varsta (a):
#     try:
#         a=int(a)# aici incercam sa il transformam in string
#         if a not in range(1900, 2034):  # vf intervalul de varsta
#             raise Exception("Nu este un an valid")
#     except ValueError:#daca nu e string ii definim exceptia
#         return "Nu ati introdus valoarea corecta, nu sunt numai cifre."
#         #return None #aci se poate pune ori none ori else
#     except Exception as e:
#         return e
#     else:
#         return f"In anul 2034 veti avea {2034 - a } ani."
#
#
# while True:
#     anul = input("In ce an v-ati nascut?")  # baga anul
#     if anul == "x":
#         break
#     print(varsta(anul))
