"""3. Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę
jeśli z liter słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter)
oraz fałsz w przeciwnym wypadku. Można założyć, że w i v składają się wyłącznie z małych liter
alfabetu łacińskiego. Proszę krótko uzasadnić wybór zaimplementowanego algorytmu."""
def possible(A, B, C):
    D = [0] * 26
    low = ord('a')
    for x in A:
        D[ord(x)-low] += 1
    for x in B:
        D[ord(x)-low] += 1
    for x in C:
        D[ord(x)-low] -= 1
    for i in range(26):
        if D[i] < 0:
            return False
    return True


A = "jebacpis"
B = "pis"
C = "jebacd"
print(possible(A, B, C))
