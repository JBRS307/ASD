#Jakub Rękas

#Na początek dodajemy wartowników na końcach ciągu, żeby nie martwić się o znaki brzegowe.
#Iterujemy po elementach ciągu, każdy element traktujemy jako środek palindromu, dopóki nie znajdziemy
#żadnego musimy wszystko sprawdzać po kolei. Promień każdego palindromu zapisujemy w tablicy do indeksu
#odpowiadającemu indeksowi znaku. Zapisujemy osobno środek i promień najdłuższego palindromu, traktujemy go jako punkt
#odniesienia. Dla każdego i mieszczącego się w tym palindromie 

from zad1testy import runtests

def ceasar( s ): #algorytm sam w sobie zadziała tylko dla palindromów nieparzystych ze względu na konieczność wystąpienia środka
    s = "^" + s + "$" #wartownicy na końcach, MUSZĄ być różni
    n = len(s)
    p = [0]*n #tablica przechowująca promienie najdłuższych palindromów o środkach na pozycjach

    i = 1 #aktualna pozycja
    center = 0 #palindromu najbardziej wysuniętego na prawo
    r = 0 #prawy kres palindromu najbardziej wysuniętego na prawo
    while i <= n-2:
        if i<r: #jeśli dla i na lewo od center jest palindrom, to w tej samej odległości strony po prawej również jest palindrom
            mirror = center - (i-center) #jesli palindrom po lewej nie wychodzi poza palindrom o środku center
            p[i] = min(r-i, p[mirror]) #przypisujemy temu po prawej tę samą wartość, jeśli wychodzi, to przypisujemy mu wartość do końca palindromu center

        radius = p[i]+1
        while s[i+radius] == s[i-radius]: #dzięki wartownikom nie trzeba martwić się o możliwość wyjścia poza tablicę
            radius += 1
        radius -= 1 #ze względu na sprawdzanie w nagłówku pętli radius wychodzi o 1 za duży
        p[i] = radius

        if i+radius>r: #sprawdzenie czy znaleziony palindrom nie jest nowym skrajnym prawym
            r = i + radius #jeśli tak, podmienia je
            center = i

        i += 1
    
    return 2*max(p)+1




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )

# print(ceasar("akontnoknonabcddcba"))
# print(ceasar("1234321234321"))
# print(ceasar("12221221221111"))
# print(ceasar("uzozuestbofefobtseqkaitwqkuyxyukqwtiakq"))
# print(ceasar("abababa"))
