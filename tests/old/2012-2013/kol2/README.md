### 2012/2013 - Kolokwium 2 

### Grupa A

### Zadanie 1

Proszę zaimplementować funkcję wstawiającą zadaną liczbę do SkipListy przechowującej dane
typu int. Proszę zadeklarować wszystkie potrzebne struktury danych i krótko (2-3 zdania) opisać
zaimplementowany algorytm.

### Zadanie 2

Proszę opisać jak zmodyfikować drzewa czerwono-czarne (przechowujące elementy typu int) tak, by operacja `int sum(T, x, y)` obliczająca sumę elementów z drzewa o wartościach z przedziału [x, y] działała w czasie `O(log n)` (gdzie n to rozmiar drzewa T). Pozostałe operacje na powstałym drzewie powinny mieć złożoność taką samą jak w standardowym drzewie
czerwono-czarnym. (Podpowiedź: Warto w każdym węźle drzewa przechowywać pewną dodatkową informację, która upraszcza wykonanie operacji sum i którą można łatwo aktualizować).

### Zadanie 3

Kapitan pewnego statku zastanawia się, czy może wpłynąć do portu mimo tego, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy:
`int n = ...`
`int m = ...`
`int A[m][n];`
gdzie wartość A[y][x] to głębokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio
jedynie na pozycję bezpośrednio obok (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję rozwiązującą problem kapitana.


### Grupa B

### Zadanie 1

Proszę zaimplementować funkcję usuwającą zadaną liczbę ze SkipListy przechowującej dane
typu int. Proszę zadeklarować wszystkie potrzebne struktury danych i krótko (2-3 zdania) opisać
zaimplementowany algorytm.

### Zadanie 2

Proszę opisać jak zmodyfikować drzewa AVL (przechowujące elementy typu int) tak, by
operacja `int findRandom(T)` zwracająca losowo wybrany element z drzewa T działała w czasie
`O(log n)`. Funkcja `findRandom` powinna zwracać każdy element z drzewa z takim samym
prawdopodobieństwem. Do dyspozycji mają Państwo funkcję `int random( int k )`, która
zwraca liczbę ze zbioru {0, ..., k − 1} zgodnie z rozkładem jednostajnym. Pozostałe operacje na
powstałym drzewie powinny mieć złożoność taką samą jak w standardowym drzewie AVL.
(Podpowiedź: Warto w każdym węźle drzewa przechowywać pewną dodatkową informację, która
upraszcza wykonanie operacji findRandom i którą można łatwo aktualizować).

### Zadanie 3

Dana jest tablica:
`int n = ...`
`int m = ...`
`bool A[m][n];`
Gracz początkowo znajduje się na (zadanej) pozycji (x, y), dla której zachodzi `A[y][x] == true`.Z danej pozycji wolno bezpośrednio przejść jedynie na pozycję, której dokładnie jedna
współrzędna różni się o 1, oraz której wartość w tablicy A wynosi true. Proszę napisać program
obliczający do ilu różnych pozycji może dojść gracz startując z zadanej pozycji (x, y).


