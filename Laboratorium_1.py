## Zapoznaj się z prostymi typami zmiennych
# print('Hello world') # fun print wyświetla wynik
# name_of_car = 'mercedes'  # zmienna name_of_car jest typu string
# print(name_of_car)
# print('Lubię samochód marki mercedes a moja rodzina też lubi samochód marki: mercedes')
############Przyklad 1
# a = 2  # zmienna a ma typ integer (liczba całkowita)
# b = 7.345134   # zmienna b typ float (liczba zmiennoprzecinkowa)
# c = a + b
# # d = b ** a  # ** to operator potęgowania  b^a
# # print(a)
# # print(b)
# print(c)
# # print(d)
# print(type(b)) # fun type sprawdza typ zmiennej
# print("#####################")
# z = 'Ala'
# x = "ma"
# y = "koty"
# zdanie = y + x + z
# print(zdanie)
#print(y,x,z)
# X = 2
# Y = '2'
# print("Zmienna X ma typ: ",type(X))
# print("Zmienna Y ma typ: ",type(Y))
# print(z,"ma kotów: ",str(X))
# print(z,"ma kotów: ",Y)
# print(X+Y)
# print("#####################")
# zm1 = input("Podaj zmienną x =") # fun input służy do wprowadzania wartości przez uzytkownika w konsoli
# zm2 = input("Podaj zmienną y =") # wynik funkcji (argument wyjściowy funkcji) input ma typ string
# c = zm1 + zm2  # konwersję zmiennej string na  float
# print(c)

# zm1 = input("Podaj zmienną x =") # fun imput służy do wprowadzania wartości przez uzytkownika w konsoli
# zm2 = input("Podaj zmienną y =") # wynik funkcji (argument wyjściowy funkcji) input ma typ string
# c = float(zm1) + float(zm2)  # konwersję zmiennej string na  float
# print(c)
#print("#####################")

# usun = input("Podaj zmienną ktorą chcesz usunąć z pamięci: ")
# del(usun)

#print("#####################")
############Zmienne logiczne ###############
# a = True
# b = False # zmienna b typ logiczny bool
# print(type(a))
# x = '1'
# y = 1
# print(x == y)   # operator ==  oznacza czy x równe y?
# print(x != y)   # operator !=  oznacza czy x różny od y?
# a = 3
# b = 5
# print(a < b)
# print(a >= b)


# roznica = a - b
# iloczyn = a * b##############Zadania do wykonania, Twoje pierwsze algorytmy
# 1. Wykonaj odejmowanie, mnożenie i dzielenie 2 dowolnych liczb

# x = float(input('Podaj x = '))
# y = float(input('Podaj y = '))
# suma = x + y
# print('Suma to:', suma)

# x = float(input('Podaj x = '))
# y = float(input('Podaj y = '))
# różnica = x - y
# print('Różnica to:' , różnica)

# x = float(input('Podaj x = '))
# y = float(input('Podaj y = '))
# iloczyn = x * y
# print('Iloczyn to:' , iloczyn)

# x = float(input('Podaj x = '))
# y = float(input('Podaj y = '))
# iloraz = x / y
# print('Iloraz to:' , iloraz)

# 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)

# x = float(input('Podaj x = '))
# y = float(input('Podaj y = '))
# c = 2 * x + 5 * y
# print('Wynik wyrażenia 2x+5y to: ' , c)

# 3. Popraw zmienną zdanie tak aby wyświetlany był napis: "Ala ma kota"

# z = 'Ala'
# x = "ma"
# y = "kota"
# zdanie = z + x + y
# print(z,x,y)

# 4. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
#  gdzie : a-imie, b-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)

# a = input('Podaj imię: ')
# b = input('Podaj nazwisko: ')
# c = input('Podaj wiek: ')
# d = input('Podaj kierunek: ')
# zdanie = 'Jestem' + ' ' + a + ' ' + b + ' ' + 'mam' + ' ' + c + ' ' + 'lat studiuję' + ' ' + d
# print(zdanie)

# 5. Sprawdź czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646

# x = 1 + 2 + 10 + 20000001 + 4 + 347586970885
# y = 321784560456434534646
# print(x==y)

# 6. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat

# a = int(input('Podaj pierwszą liczbę: '))
# b = int(input('Podaj drugą liczbę: '))
# suma = a + b

# if suma % 2 == 0:
#     print('Suma jest liczbą parzystą.')
# else:
#     print('Suma jest liczbą nieparzystą.')

# 7. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
# iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.

# a = float(input("Podaj pierwszą liczbę: "))
# b = float(input("Podaj drugą liczbę: "))

# suma = a + b
# iloraz = a / b
# potega = a ** b

# print("Suma: ", suma)
# print("Różnica: ", roznica)
# print("Iloczyn: ", iloczyn)
# print("Iloraz: ", iloraz)
# print("Potęga: ", potega)

# 8. Oblicz wyrażenie: a = 3z-|2cos(x)sin(y)|, gdzie: x,y,z - dowolne liczby     (|x| to moduł z liczby z, użyj funkcji abs())

# import math
# a = math.sin(30)
# print(a)

# from math import sin,cos
# a = sin(30)
# print(a)
# print(abs(a))

# 9. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",
# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.

# imie = input("Podaj swoje imię: ")
# nazwisko = input("Podaj swoje nazwisko: ")
# wiek = int(input("Podaj swój wiek: "))

# print("Czy zdrowo się odżywiasz?")
# odzywianie = input()

# print("Czy lubisz sport?")
# sport = input()

# print("Czy masz rodzeństwo?:")
# rodzeństwo = input()

# print("Czy masz pupila:")
# pupil = input()

# print("Czy lubisz pizzę?:")
# pizza = input()

# print("Podsumowanie:")
# print("Imię: ", imie)
# print("Nazwisko: ", nazwisko)
# print("Wiek: ", wiek)
# print("Zdrowe odżywianie: ", odzywianie)
# print("Lubienie sportu: ", sport)
# print("Posiadanie rodzeństwa: ", rodzeństwo)
# print("Posiadanie pupila: ", pupil)
# print("Lubienie pizzy: ", pizza)

# 10. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 10-ciu zdań, które wyświetlisz na ekranie
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.

# imie = input("Podaj swoje imię: ")
# nazwisko = input("Podaj swoje nazwisko: ")
# wiek = input("Podaj swój wiek: ")
# zawod = input("Podaj swój zawód: ")
# miejsce_urodzenia = input("Podaj swoje miejsce urodzenia: ")
# zainteresowania = input("Podaj swoje zainteresowania: ")
# zyciorys = "Nazywam się " + imie + " " + nazwisko + " i mam " + wiek + " lat. Jestem " + zawod + " i pochodzę z " + miejsce_urodzenia + ". Moje zainteresowania to " + zainteresowania + ". W przeszłości pracowałem/am również jako..."
# print(zyciorys)

# 11. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie

# spolgloski = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
# samogloski = ["a", "e", "i", "o", "u", "y"]
# while True:
#     sp = input("Podaj spółgłoskę (lub wpisz 'koniec' aby zakończyć): ")
#     if sp == "koniec":
#         break
#     if sp not in spolgloski:
#         print("Niepoprawna spółgłoska.")
#     else:
#         for sam in samogloski:
#             print(sp + sam)


#12. Sprawdz wynik działań
# 0 > 1
# 0 <= 1
# 0 >= 1
# 1 == 0
# 1 == 1
# 1 != 0
# 1 != 1
#(x > 1 and x < 13) and x != 5  , dla x = 2

# x = 2
# print(0 > 1) 
# print(0 <= 1) 
# print(0 >= 1) 
# print(1 == 0)  
# print(1 == 1)  
# print(1 != 0)  
# print(1 != 1)  
# print((x > 1 and x < 13) and x != 5) 

# 13. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna
#
#print("#####################")

# imie = input("Podaj swoje imię: ")

# if imie == "Janusz" or imie == "Grażyna":
#     print("Witaj,", imie)
# else:
#     print("Przykro mi,", imie, "nie jesteś Januszem ani Grażyną :(")
