#Jakub Rękas

from zad1testy import runtests

def ceasar( s ): #algorytm sam w sobie zadziała tylko dla palindromów nieparzystych ze względu na konieczność wystąpienia środka
    s = "^" + s + "$"
    n = len(s)
    max_radius = 0
    for i in range(1, n-1):
        radius = 1
        while s[i+radius] == s[i-radius]:
            radius += 1
        radius -= 1

        if radius > max_radius:
            max_radius = radius
    
    return 2*max_radius+1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )

# print(ceasar("akontnoknonabcddcba"))
# print(ceasar("1234321234321"))
# print(ceasar("12221221221111"))
# print(ceasar("uzozuestbofefobtseqkaitwqkuyxyukqwtiakq"))
# print(ceasar("abababa"))
