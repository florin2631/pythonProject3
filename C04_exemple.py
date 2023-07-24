"""
Functii
"""
# ======================================================================================================================
# Definirea si apelarea unei functii
# ======================================================================================================================
#
# # Definirea functiei - o singura data
# def functie_hello():
#     print("Hello")
#
# # Apelarea functiei - de ori cate ori este nevoie
# functie_hello()
# functie_hello()
# functie_hello()
#
# # Alta varianta de a apela functia
# for i in range(4):
#     functie_hello()

# ======================================================================================================================
# Functii parametrizate
# ======================================================================================================================
# def puterea_x(x,y):
#     print(x ** y)
#
# numar = int(input("Introduceti un numar: "))
# numar2 = int(input("Introduceti un alt numar: "))
# puterea_x(numar, numar2)

# -------------------------------------------
# args* = pentru nr necunoscut de parametrii
# -------------------------------------------
# Creati o functie care va lua ori cate numere ca parametru si va calcula suma acestora
# todo

# ======================================================================================================================
# Cuvantul cheie return = opreste executia functiei si schimba valoarea de return a acesteia
# ======================================================================================================================
# def functie1():
#     print("Suntem in functia 1")
#
#
# functie1()                                       # Executa comenzile (functiile apelate) din interiorul functiei
# print(f"Obiectul: {functie1}")                   # Afiseaza obiectul de functie
# print(f"Valoarea de return: {functie1()}")       # Afiseaza rezultatul functiei (valoarea de return)
#
# def functie2():
#     return "Suntem in functia 2"
#
# functie2()
# print(f"Obiectul: {functie2}")
# print(f"Valoarea de return: {functie2()}")

# -------------------------------------------------------------------------------------------
# Cand folosim return?                                                                      |
# Creati un program care sa contina 2 functii:                                              |
#   1. Functia "putere" va lua n argumente si va returna o lista cu fiecare nr dat la putere|
#   2. Functia "suma" va lua ca argument o lista de numere si va returna suma acestora      |
# -------------------------------------------------------------------------------------------
# # TODO
# def putere(*args):
#     pass
#
# def suma(lst: list):
#     pass
#
# puteri = putere(5,12,3,8,4,2)
# print(suma(puteri))

# ======================================================================================================================
# Cuvantul cheie global - aduce o variabila de afara in interiorul functiei
# ======================================================================================================================
# Creati un program care sa numere de cate ori s-a executat o functie
# todo

""" 
Tupluri
"""
# ======================================================================================================================
# Declararea tuplurilor
# ======================================================================================================================
# tuplu1 = 1,2,3
# tuplu2 = 1,"a",2.,"b","3"
# tuplu3 = (tuplu2,tuplu1)
# tuplu4 = 1,
#
# for i in tuplu3:
#     print(type(i))

# ======================================================================================================================
# Operatii cu tupluri
# ======================================================================================================================
# tuplu_extended = tuplu3 + (100,1000)        # Adaugarea tuplurilor
# print(tuplu_extended)

# a,b,c = tuplu1                             # Separarea elementelor din tuplu
# print(a)
# print(b)
# print(c)

# print(tuplu_test[1])                       # Extragerea elementelor din tuplu

# print(tuplu_test * 3)                      # Multiplicarea tuplurilor

"""
Dictionare
"""
# ======================================================================================================================
# Declararea dictionarelor
# ======================================================================================================================
# dict1 = {
#     "produs": "masa",
#     "pret": 125,
#     "disponibil": True,
#  }

# ======================================================================================================================
# Operatii cu dictionare
# ======================================================================================================================
# print(dict1['produs'])                # Extragerea valorilor asociate unei chei

# dict1['stoc'] = 56                    # Adaugarea unei chei in dict
# print(dict1)

# del dict1['stoc']                     # Stergerea unui entry din dict
# print(dict1)

# print('stoc' in dict1)                # Verificarea existentei unei chei in dict

# print(dict1.keys())                   # Extragerea cheilor din dictionar
# print(dict1.values())                 # Extragerea valorilor din dictionar
# print(dict1.items())                  # Extragerea tuplurilor de (cheie,valoare) din dictionar

# dict1.update({"stoc": 12,"pret": 45.44})      # Update la dict
# print(dict1)

"""
Exceptii
"""
# ======================================================================================================================
# Sintaxa try - except - else
# ======================================================================================================================
# try:
#     # actiunea care se va incerca
#     pass
# except ValueError:
#     # actiunea care se va lua daca da de o eroare specifica (in cazul asta, ValueError)
#     pass
# except BaseException:
#     # actiunea care se va lua daca da de eroarea mentionata
#     # (BaseException = le cuprinde pe toate, aka. exceptia de backup)
#     pass
# else:
#     # actiunea care se va lua daca blocul de try s-a executat cu succes (daca nu a aparut nici o eroare)
#     pass

# -------------------------------------------------------------------------------------------
# Creati un program care va lua ca input de la utilizator 2 numere.                         |
# Afisati rezultatul impartirii a/b. Asigurati-va ca se trateaza toate erorile care pot     |
# aparea in timpul rularii. In caz contrar, se va afisa un mesaj de eroare corespunzator.   |
# -------------------------------------------------------------------------------------------
# todo

# ======================================================================================================================
# Trick: comprehensiunea de liste
# ======================================================================================================================
# Luati ca input de la utilizator 5 numere si calculati media acestora. Asigurati-va ca toate input-urile sunt numerice.

# todo