#Jakub Rękas

#Prosty algorytm wyszukiwania palindromów działający w O(n^2).
#1. Iterujemy po każdym znaku w wyrazie traktując go jako środek palindromu.
#2. Sprawdzamy, czy w tej samej odległości od środka (radius), po obu stronach, jest ten sam znak.
#3. Jeśli znaki są różne, pętla przerywa się.
#4. Jeśli radius przekroczył aktualny max_radius to go nadpisujemy.
#5. Na koniec zwracamy 2*max_radius+1, czyli 2 razy najdluższy promień (na każdą ze stron) i dodatkowo 1 znak, który jest środkiem
#   nieparzystego palindromu.

from zad1testy import runtests

def ceasar( s ): #algorytm sam w sobie zadziała tylko dla palindromów nieparzystych ze względu na konieczność wystąpienia pojedynczdego środka
    s = "^" + s + "$" #dodanie wartowników sprawia, że nie trzeba za każdym razem sprawdzać czy nie wyszliśmy za tablicę
    n = len(s)
    max_radius = 0 #radius najdłuższego palindromu
    for i in range(1, n-1):
        radius = 1
        while s[i+radius] == s[i-radius]: #każde i traktujemy jako środek palindromu i sprawdzamy czy obszar po lewej jest "lustrzanym odbiciem"
            radius += 1                   #obszaru po prawej
        radius -= 1 #po pętli radius wychodzi o 1 za duży ze względu na sprawdzanie w nagłówku, trzeba go zmniejszyć o 1

        if radius > max_radius: #Jeśli radius jest większy niż aktualny max_radius, nadpisujemy go
            max_radius = radius
    
    return 2*max_radius+1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )

# print(ceasar("akontnoknonabcddcba"))
# print(ceasar("1234321234321"))
# print(ceasar("12221221221111"))
# print(ceasar("uzozuestbofefobtseqkaitwqkuyxyukqwtiakq"))
# print(ceasar("abababa"))
