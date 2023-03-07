#Jakub Rękas

#Zadanie da się zrobić liniowo. Sprawdzamy ciąg znaków począwszy od pozycji 1 aż do pozycji n-2
#Każdy ze znaków, który sprawdzamy traktujemy jako środek palindromu i iterujemy jednocześnie na lewo oraz na prawo
#od niego sprawdzając, czy znaki na odpowiadających odległościach od znaku na środku są jednakowe.
#Jeśli znajdziemy jakiś palindrom, to następnym środkiem będzie dopiero ostatni znak tego palindromu (z prawej strony)
#ponieważ jeśli zaczniemy sprawdzać wcześniej możemy znaleźć palindrom, ale na pewno nie będzie on dłuższy, ze względu na to, że
#ostatni znak z prawej w palindromie "zrywa" go.
#Zadanie na algorytm Manachera

from zad1testy import runtests

def ceasar( s ): #algorytm sam w sobie zadziała tylko dla palindromów nieparzystych ze względu na konieczność wystąpienia środka
    n = len(s)
    # best_center = 0
    center = 1 #znak, który jest środkiem badanego palindromu
    half_leng = 0 #radius najdłuższego palindromu (radius to odległość końca od środka)

    while center <= n-2:
        radius = 1 #odległość od środka palindromu
        while not(center+radius == n or center-radius == -1) and \
              s[center+radius] == s[center-radius]:
            radius += 1
        radius -= 1 #otrzymany radius w pętli jest o 1 za duży, ze względu na zwiększanie radiusa już po sprawdzeniu
                    #czy podciąg jest palindromem. Trzeba to skorygować

        if radius > half_leng: #warunek sprawdzający czy znaleziony palindrom jest najdłuższy, jeśli tak podmienia wartości
            half_leng = radius
            # best_center = center
        
        if radius == 0: #Zabezpieczenie przed wpadnięciem w nieskończoną pętlę w wypadku braku palindromu dla danego środka
            center += 1
        else:
            center += radius
    
    return 2*half_leng + 1 #Długość palindromu do radius z każdej strony + znak środka
    # return s[best_center-half_leng:best_center+half_leng+1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )

# print(ceasar("akontnoknonabcddcba"))
# print(ceasar("1234321234321"))
# print(ceasar("12221221221111"))
# print(ceasar("uzozuestbofefobtseqkaitwqkuyxyukqwtiakq"))
