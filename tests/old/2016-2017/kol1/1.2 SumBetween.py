"""2. Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie)."""
from quicksort import quickselect
def sumbetween(A, f, t, n):
    low = quickselect(A, 0, n - 1, f)
    high = quickselect(A, 0, n - 1, t)
    suma = 0
    for i in range(n):
        if low <= A[i] <= high:
            suma += A[i]
