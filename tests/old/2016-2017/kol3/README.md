### 2016/2017 - Kolokwium 3

### Zadanie 1

Dana jest mapa kraju w postaci grafu `G = (V, E)`, gdzie wierzchołki to miasta a krawędzie to
drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje kto
prowadzi pierwszy. Proszę zaproponować algorytm, który wskazuje taką trasę (oraz osobę, która
ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien
być jak najszybszy (ale przede wszystkim poprawny). Proszę oszacować złożoność
zaproponowanego algorytmu, zakładając, że graf jest reprezentowany macierzowo.

### Zadanie 2

Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
`int goodThief( int A[], int n );`, która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie jak najszybszy (ale przede wszystkim poprawny).

### Zadanie 3

Dany jest zbiór przedziałów otwartych A = {(a1, b1), ...,(an, bn)}. Proszę zaproponować algorytm (bez implementacji), który znajduje taki zbiór X, X ⊆ {1, ..., n} że (a) |X| = k (gdzie k ∈ N to dany parametr wejściowy), (b) dla każdych i, j ∈ X, przedziały 
(ai, bi) oraz (aj, bj ) nie nachodząna siebie, oraz (c) wartość `max_(j ∈ X) bj − min_(i∈X) ai`
jest minimalna. Jeśli podzbioru spełniającego warunki (a) i (b) nie ma, to algorytm powinien to stwierdzić. Algorytm powinien być możliwie jak najszybszy (ale przede wszystkim poprawny).


