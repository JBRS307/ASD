### 2015/2016 - Kolokwium 2

### Zadanie 1

Dane są struktury danych opisujące SkipListę:
struct SLNode {
`int value;`// wartość przechowywana w węźle
`int level;` // poziom węzła
`SLNode** next;` // level-elementowa tablica wskaźników na następniki
};
struct SkipList {
`SLNode* first;` // wartownik przedni (pole value ma wartość -∞)
`SLNode* last; `// wartownik tylny (pole value ma wartość +∞)
};
`const int MAX LEVEL = ... ; `// maksymalny poziom węzłów
Proszę zaimplementować funkcję `SkipList merge( SkipList A, SkipList B )`, która scala
dwie otrzymane SkipListy (w efekcie powstaje nowa SkipLista składająca się z dokładnie tych
samych węzłów co poprzednie; nie należy zmieniać poziomów węzłów). Węzły wartowników mają
poziom MAX LEVEL. Funkcja powinna działać możliwie jak najszybciej. Proszę oszacować
złożoność czasową.

### Zadanie 2

Proszę opisać (bez implementacji) algorytm, który otrzymuje na wejściu pewne drzewo BST T
i tworzy nowe drzewo BST T', które spełnia następujące warunki: 
(a) T' zawiera dokładnie te same wartości co T
(b) drzewo T' jest drzewem czerwono-czarnym (w związku z tym powinno zawierać kolory węzłów).

### Zadanie 3

W ramach obchodów międzynarodowego święta cyklistów organizatorzy przewidzieli górską
wycieczkę rowerową. Będzie się ona odbywać po bardzo wąskiej ścieżce, na której rowery mogą
jechać tylko jeden za drugim. W ramach zapewnienia bezpieczeństwa każdy rowerzysta będzie
miał numer identyfikacyjny oraz małe urządzenie, przez które będzie mógł przekazać
identyfikator rowerzysty przed nim (lub -1 jeśli nie widzi przed sobą nikogo). Należy napisać
funkcję, która na wejściu otrzymuje informacje wysłane przez rowerzystów i oblicza rozmiar
najmniejszej grupy (organizatorzy obawiają się, że na małe grupy mogłyby napadać dzikie
zwierzęta). Dane są następujące struktury danych:

```
struct Cyclist {
int id, n id; // identyfikator rowerzysty oraz tego, którego widzi
};
```

Funkcja powinna mieć prototyp `int smallestGroup( Cyclist cyclist[], int n )`, gdzie
cyclist to tablica n rowerzystów. Funkcja powinna być możliwie jak najszybsza. Można założyć,
że identyfikatory rowerzystów to liczby z zakresu 0 do 108 (osiem cyfr napisanych w dwóch rzędach na koszulce rowerzysty) i że pamięć nie jest ograniczona. Rowerzystów jest jednak dużo
mniej niż identyfikatorów (nie bez powodu boją się dzikich zwierząt). Należy zaimplementować
wszystkie potrzebne struktury danych.

