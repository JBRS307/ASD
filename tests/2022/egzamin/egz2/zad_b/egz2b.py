# Na pierwszy rzut oka to wygląda jak O(n^2), po dłuższej analizie to chyba jest jednak O(n).
# Ilość drzwi zawsze wynosi 3n, a ten algorytm dokładnie 1 raz sprawdza każde drzwi

from egz2btesty import runtests

def transpone(C, n):
    D = [[C[i][0]] for i in range(n)]
    
    for i in range(n):
        for j in range(1, 4): # długość to zawsze 4, ponieważ jest troje drzwi, a na początku komórka na złoto
            gold, chamber = C[i][j]
            if chamber != -1:
                D[chamber].append((gold, i))
    
    return D


def magic( C ):
    n = len(C)
    dp = [-1]*n
    dp[0] = 0
    D = transpone(C, n)

    for i in range(1, n):
        for j in range(1, len(D[i])):
            to_open, chamber = D[i][j] # tyle w skrzyni, żeby otworzyć przejście
            hand = dp[chamber] # tyle w ręku w poprzedniej komnacie
            chest = C[chamber][0] # tyle w skrzyni w poprzedniej komnacie

            if hand == -1:
                continue

            if chest > to_open and chest-to_open <= 10:
                gold = hand + (chest-to_open)
            elif chest < to_open:
                gold = hand - (to_open-chest)
            elif chest == to_open:
                gold = hand
            else:
                gold = -1
            
            gold = -1 if gold < 0 else gold

            dp[i] = max(gold, dp[i])
    
    return dp[n-1]


            


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
