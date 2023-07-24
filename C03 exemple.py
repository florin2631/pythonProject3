"""
Logica if-else
"""
# # if - else
# vreme = "soare"
#
# if vreme == "soare":                            # Se verifica daca conditia de dupa cuvantul cheie if este True
#     print("Merg la plimbare")                   # Se executa doar in cazul in care conditia = True
# else:
#     print("Astazi nu e vreme de plimbare")      # Optional: Se executa daca conditia = False
#
# # if - elif - else
# vreme = "ploios"
#
# if vreme == "soare":                            # Se verifica fiecare conditie pe rand => prima care = True -> se executa codul din blocul indentat
#     print("Merg la plimbare.")
# elif vreme == "innorat":
#     print("Merg la o plimbare scurta")
# elif vreme == "ploios":
#     print("Merg la o plimbare cu masina")
# else:
#     print("Astazi stau in casa.")

# =======================================================================
# TRUTH TABLE - AND (aka toate conditiile trebuie sa fie adevarate)
# print("|______A______|_____B_____|______Rez______|")
# print("|    False    |   False   |  ",False and False)          # False
# print("|    True     |   False   |  ",True and False)           # False
# print("|    False    |   True    |  ",False and True)           # False
# print("|    True     |   True    |  ",True and True)            # True
# print("|_____________|___________|_______________|")
#
# a = int(input("Introduceti un numar pozitiv a = "))
# b = int(input("Introduceti un numar pozitiv b = "))
#
# if a > 0 and b > 0:                             # Daca a > 0 = True SI b > 0 = True => se executa blocul indentat. Altfel, intra in else
#     print(f"Rezultatul este: {a * b}")
# else:
#     print("Nu ati introdus numere corespunzatoare.")
# =======================================================================
# TRUTH TABLE - OR (aka minim una din conditii trebuie sa fie adevarata)
# print("|______A______|_____B_____|______Rez______|")
# print("|    False    |   False   |  ",False or False)          # False
# print("|    True     |   False   |  ",True or False)           # True
# print("|    False    |   True    |  ",True or True)            # True
# print("|    True     |   True    |  ",True or True)            # True
# print("|_____________|___________|_______________|")
#
# vreme = int(input("Introduceti ce vreme este astazi: "))
#
# if vreme == "soare" or vreme == "innorat":      # Daca vreme = soare SAU vreme = innorat => se executa blocul indentat
#     print("Merg la plimbare pe jos")
# else:
#     print("Nu merg la plimbare azi.")

"""
Bucle while
"""
# i = 0                     # Initializarea unui counter i
#
# while i < 10:             # Conditie verificata la fiecare iteratie de bucla
#     print(i)              # Se va afisa i-ul actual
#     i += 1                # Incrementarea lui i (aka i = i + 1) / Altfel, valoarea lui i va ramane 0 => rezulta in bucla infinita

# ======================================================================================================================
# CONTINUE - la intalnirea cuvantului cheie continue se va trece direct la urmatoarea iteratie de bucla
# fara a continua cu executia restului de bucla pentru iteratia curenta
#
# i = 0
# while i < 10:
#     if i % 2 == 0:        # daca i este numar par
#         i += 1            # vom incrementa doar valoarea lui i pentru a evita o bucla infinita
#         continue          # se va intoarce la linia 67 => face din nou verificarea fara a executa restul buclei
#     print(i)              # va afisa numarul impar
#     i += 1                # vom incrementa valoarea lui i cu 1
# ======================================================================================================================
# BREAK - la intalnirea cuvantului cheie break se va intrerupe complet bucla, neexecutand nici o iteratie care urmeaza
#
# # Se cere un program care sa caute prima ocurenta a unei litere introduse de catre utilizator in cuvantul alfabet si sa
# # returneze pozitia literei in cuvant.
# cuvant = "alfabet"
#
# i = 0                                           # initializarea indexului de plecare in cuvant
# litera = input("Introduceti o litera: ")        # Se cere input cu litera
#
# while i < len(cuvant):                          # Se parcurge cuvantul folosind indexul i
#     if cuvant[i] == litera:                     # daca litera de la pozitia actuala (i) coincide cu litera introdusa
#                                                 # de user, se afiseaza pozitia si se iese din bucla.
#         print(f"Am gasit litera {litera} la pozitia {i} in cuvantul alfabet.")
#         break
#     i += 1

# ======================================================================================================================
# WHILE -ELSE

# Se cere un program care sa caute prima ocurenta a unei litere introduse de catre utilizator in cuvantul alfabet si sa
# returneze pozitia literei in cuvant. Daca nu s-a gasit litera, sa se afiseze un mesaj corespunzator la final.

# TODO

# ======================================================================================================================
# BUCLE INFINITE = au nevoie mereu de conditii de break
# password = "8459"
#
# user = input("Introduceti numele utilizatorului: ")
# while True:
#     parola = input(f"Introduceti parola pentru utilizatorul {user}: ")
#     if parola == password:
#         print("Access granted.")
#         break
#     print("Parola gresita. ")

"""
Bucle for
"""
cuvant = "alfabet"

for i in cuvant:        # parcurge un iterabil (siruri, liste, tupluri, range-uri, etc.)
    print(i)

# ======================================================================================================================
# FOR - ELSE

# Se cere un program care sa caute prima ocurenta a unei litere introduse de catre utilizator in cuvantul alfabet,
# iar daca nu s-a gasit, sa se afiseze un mesaj corespunzator.

# todo

"""
Liste
"""
# lista1 = [1,2,3]
# lista2 = ["abc", 1, "5", 1, "5", lista1]
#
# print(lista1)
# print(lista2)
#
# # Metode folositoare pe liste
# print(dir(list))        # afiseaza toate metodele disponibile pe obiecte de tip lista
#
# lista1.append("sir")    # adauga elementul specificat la finalul listei
# print(lista1)
#
# lista1.insert(3,"s")    # adauga elementul "s" la pozitia 3 in lista
# print(lista1)
#
# lista1.remove("sir")    # elimina prima ocurenta a elementului "sir" din lista
# print(lista1)
#
# lista2.reverse()        # inverseaza elementele listei
# print(lista1)
#
# lista1.clear()          # goleste lista
# print(lista1)
#
# # Metode care returneaza o valoare (putem afisa direct operatiunea)
# print(lista2.count("5"))       # returneaza nr de ocurenta a parametrului in lista

"""
Range (Intervalul)
"""
# Se cere un program care sa verifice daca utilizatorul are peste 18 ani.
#
# # Varianta 1
# range1 = range(18,100)
#
# varsta = input("Introduceti varsta dvs: ")
#
# if int(varsta) not in range1:
#     print("Nu aveti peste 18 ani.")
# else:
#     print("Puteti merge la vot.")
#
# # Varianta 2
# range2 = range(18)
# varsta = input("Introduceti varsta dvs: ")
#
# if int(varsta) in range2:
#     print("Nu aveti peste 18 ani.")
# else:
#     print("Puteti merge la vot.")

# ======================================================================================================================
# Se cere un program care sa parcurga toate numerele pare de la 0 la un nr introdus de user
# nr = input("Introduceti un numar: ")
#
# for i in range(0,int(nr),2):
#     print(i)
