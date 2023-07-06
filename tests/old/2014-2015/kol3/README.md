### 2014/2015 - Kolokwium 3 

### Zadanie 1

W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mają
mieszkańcy.
```cpp
struct Vertex {
    bool shop;      // true-sklep, false-dom
    int *distances; // tablica odległości do innych wierzchołków
    int *edges;     // numery wierzchołków opisanych w distances
    int edge;       // rozmiar tablicy distances (i edges)
    int d_store     // odległość do najbliższego sklepu
};
```
Zaimplementować funkcję uzupełniającą `d_store` dla tablicy Vertexów `void distanceToClosestStore (int n, Vertex *village)` i oszacować złożoność algorytmu.

### Zadanie 2

Problem plecakowy - dwuwymiarowa wersja problemu - oprócz ciężaru jest wysokość (objętość?)
towarów.przedmioty {`p1`...`pn`}
`v(pi)` - wartość przedmiotu pi
`r(pi)` - ciężar przedmiotu pi
`h(pi)` - wysokość przedmiotu pi

Jaka jest największa możliwa sumaryczna wartość przedmiotów, których ciężar nie przekracza `M` a wysokość `S`? Oszacować złożoność i udowodnić poprawność algorytmu. (Nie trzeba implementować).

### Zadanie 3

Forma to koniunkcja klauzul. Klauzula to alternatywa zmiennych lub ich negacji. Przykład:
(¬a or b) and (¬b or c or d) and (a or d) and (¬a or ¬c or d). Forma składa się z m klauzul
(C1, ..., Cm). Jest n zmiennych (x1, ..., xn). Jak ustawić zmienne, aby co najmniej połowa klauzul była spełniona? Oszacować złożoność i udowodnić poprawność algorytmu.
(Nie trzeba implementować).
