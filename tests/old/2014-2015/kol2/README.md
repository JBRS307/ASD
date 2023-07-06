### 2014/2015 - Kolokwium 2

### Zadanie 1

Pewna firma przechowuje dużo iczb pierwszych w postaci binarnej jako stringi ”10101...”.
Zaimplementuj strukturę danych Set do przechowywania tych danych. Napisz funkcje:
`Set createSet( string A[], int n )`, która tworzy Set z n-elementowej tablicy stringów
oraz `bool contains( Set a, string s )`, która sprawdza czy dana liczba jest w Secie.
Oszacuj złożoność czasową i pamięciową powyższych funkcji.

### Zadanie 2

Dana jest struktura danych:
```struct Edge {
int u, v; // u < v
Edge* next;
};
```
Napisz funkcję `bool Euleran( Edge* E, int n )`, która sprawdza czy graf zadany przez listę
krawędzi posiada cykl Eulera (n to liczba wierzchołków w grafie). Graf jest nieskierowany
i spójny. Krawędzie w liście mogą się powtarzać. Funkcja powinna alokować nie więcej pamięci,
niż liniowo proporcjonalnie do ilości krawędzi.

### Zadanie 3

Zaproponuj algorytm, który policzy ile jest najkrótszych ścieżek w grafie z danego wierzchołka
u do v. Wskazówka: Dla każdej najkrótszej ścieżki przechodzącej przez wierzchołek w,
odległość w od startu jest taka sama jak odległość w do mety.