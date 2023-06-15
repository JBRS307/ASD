# Przejść przez wszystkie miasta tak, żeby skończyć tam gdzie zaczęliśmy i zrobić
# jak najmniejszy dystans.

# Wersja bitoniczna (i < j)
# f(i, j) = koszt ścieżek z 0 do i oraz z 0 do j, które odwiedzją wszystkie miasta 0...j i żadnego
# nie powtarzają.
#
# f(0, 1) = d(0, 1)
# f(i, j) = f(i, j-1) + d(j-1, j)
# f(j-1, j) = min(f(i, j-1)+d(i, j)) for i < j-1

from math import inf

# Rekurencja z memoizacją

F = [[inf]*n for i in range(n)]
def tspf(i, j, F, D):
    if F[i][j] != inf:
        return F[i][j]
    
    if i == j-1:
        best = inf
        for k in range(j-1):
            best = min(best, tspf(k, j-1, F, D)+D[k][j])
            F[j-1][j] = best
