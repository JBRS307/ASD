# Jakub Rękas

# Na początek tworzymy tablicę dp, która finalnie będzie zawierać maksymalną ilość komnat do przejśca aby dostać
# się do danego pokoju, bądź informację, że nie da się tam dojść. Wypełniamy kolumnę 0 startując w dół z komnaty (0, 0).
# Każdą następną kolumnę sprawdzamy 2 razy, szukając maksymalnej wartości dla każdej komnaty
# z wykorzystaniem kolumny po lewej. Raz idąc z samej góry na sam dół, za drugim razem z samego dołu na samą górę.
# Metoda ta działa, ponieważ z powodu narzuconych ograniczeń jeśli raz ruszymy się w danej kolumnie w danym kierunku, to każdy
# następny ruch musi być w tym samym kierunku. Po sprawdzeniu każdej kolumny dwa razy wybieramy większą wartość maksymalną dla
# każdej komnaty w kolumnie. Gdy algorytm zakończy działanie, w komórce dp[n-1][n-1] jest informacja o maksymalnej liczbie
# komnat jakie można odwiedzić w drodze do prawego dolnego rogu (bądź informacja, że nie da się tam dotrzeć).

from zad7testy import runtests

def maze(L):
    n = len(L)
    if n == 1: # Na wszelki wypadek
        return 0
    
    # Jako None będą w dp oznaczone pola na które nie da się dojść, na początku ustawiamy wszystkie
    # zablokowane komnaty jako None
    dp = [[(0 if L[i][j] != '#' else None) for j in range(n)] for i in range(n)]

    access = True
    for i in range(1, n):
        if L[i][0] == '#':
            access = False
        if access:
            dp[i][0] = dp[i-1][0]+1
        else:
            dp[i][0] = None
    
    for j in range(1, n):
        alt_col = [dp[i][j] for i in range(n)]
        # sprawdzanie z góry na dół
        for i in range(n):
            if L[i][j] == '#':
                continue
            up = None if i == 0 else dp[i-1][j]
            left = dp[i][j-1]

            if up is None and left is None:
                dp[i][j] = None
            elif up is None:
                dp[i][j] = dp[i][j-1]+1
            elif left is None:
                dp[i][j] = dp[i-1][j]+1
            else:
                dp[i][j] = dp[i][j-1]+1 if dp[i][j-1] > dp[i-1][j] else dp[i-1][j]+1
        
        # sprawdzanie z dołu do góry
        for i in range(n-1, -1, -1):
            if L[i][j] == '#':
                continue
            down = None if i == n-1 else alt_col[i+1]
            left = dp[i][j-1]
            
            if down is None and left is None:
                alt_col[i] = None
            elif down is None:
                alt_col[i] = dp[i][j-1]+1
                if dp[i][j] is None:
                    dp[i][j] = alt_col[i]
                else:
                    dp[i][j] = alt_col[i] if alt_col[i] > dp[i][j] else dp[i][j]
            elif left is None:
                alt_col[i] = alt_col[i+1]+1
                if dp[i][j] is None:
                    dp[i][j] = alt_col[i]
                else:
                    dp[i][j] = alt_col[i] if alt_col[i] > dp[i][j] else dp[i][j]
            else:
                alt_col[i] = alt_col[i+1]+1 if alt_col[i+1] > dp[i][j-1] else dp[i][j-1]+1
                dp[i][j] = alt_col[i] if alt_col[i] > dp[i][j] else dp[i][j]

    return dp[n-1][n-1] if dp[n-1][n-1] is not None else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
