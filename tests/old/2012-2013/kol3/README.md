### 2012/2013 - Kolokwium 3

### Zadanie 1

Niech G = (V, E) będzie pewnym grafem nieskierowanym a U ⊆ V pewnym podzbiorem jego
wierzchołków. Grafem indukowanym G|U nazywamy graf powstały z G przez usunięcie
wszystkich wierzchołków spoza U. Proszę podać i zaimplementować wielomianowy algorytm,
który mając na wejściu graf G = (V, E) (reprezentacja przez listy sąsiedztwa) oraz liczbę
naturalną k, znajduje maksymalny co do rozmiaru zbiór U ⊆ V taki, że wszystkie wierzchołki
w G|U mają stopień większy lub równy k. Proszę oszacować czas działania algorytmu.

### Zadanie 2

Na wejściu dana jest formuła logiczna F postaci CNF (conjunctive normal form), czyli
F = C1 ∧ C2 ∧ ... ∧ Cm, gdzie każde Ci to tak zwana klauzula, czyli alternatywa zmiennych
logicznych lub ich negacji. Formuła w postaci CNF jest Hornowska jeśli każda klauzula zawiera
najwyżej jedną niezanegowaną zmienną. Przykłady Hornowskich formuł CNF to:
(x) ∧ (x ∨ y) ∧ (x ∨ y ∨ z), (x ∨ y) ∧ (x ∨ y), czy (x) ∧ (x). Proszę opisać wielomianowy algorytm,
który sprawdza czy Hornowska formuła w postaci CNF jest spełnialna (to znaczy, czy da się
przypisać wartości logiczne zmiennym tak, żeby formuła miała wartość prawda).

### Zadanie 3

Mamy dany ciąg napisów S = (s1, ..., sn) oraz pewien napis t. Wiadomo, że t można zapisać jako
złączenie pewnej ilości napisów z S (z powtórzeniami). Na przykład dla S = (s1, s2, s3, s4, s5)
gdzie s1 = ab, s2 = abab, s3 = ba oraz s4 = bab, s5 = b, napis t = ababbab można zapisać, między innymi, jako s2s4 lub jako s1s1s3s5. Pierwsza reprezentacja ma ”szerokość” 3 (przez szerokość rozumiemy długość najkrótszego si użytego w reprezentacji) a druga 1. Proszę opisać algorytm, który mając na wejściu S oraz t znajdzie maksymalną szerokość reprezentacji t.
Proszę oszacować czas działania algorytmu
