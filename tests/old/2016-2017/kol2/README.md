### 2016/2017 - Kolokwium 2

### Zadanie 1

Student chce wypuścić n różnych pok´emonów (numerowanych od 0 do n − 1) z klatek
(pok´eball’i). Wypuszczony Pok´emon natychmiast atakuje swojego wybawiciela, chyba że (a) jest
spokojny, lub (b) w okolicy znajdują się co najmniej dwa uwolnione pok´emony, na które ten
pok´emon poluje. Proszę zaimplementować funkcję:
`int* releaseThemAll( HuntingList* list, int n ),`
gdzie list to lista z informacją, które pok´emony polują na które (lista nie zawiera powtórzeń):
```
struct HuntingList {
    HuntingList* next; // następny element listy
    int predator; // numer pokemona, który poluje
    int prey; } // numer pokemona, na którego poluje
```
Funkcja powinna zwrócić n elementową tablicę z numerami pok´emonów w kolejności
wypuszczania (tak, żeby wypuszczający nie został zaatakowany) lub NULL jeśli taka kolejność nie
istnieje. Każdy wypuszczony pok´emon zostaje ”w okolicy”. Jeśli pok´emon nie występuje na liście jako predator to znaczy, że jest spokojny. Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę krótko oszacować jej złożoność.

### Zadanie 2

Dana jest struktura `struct HT{ int* table; int size; }`, która opisuje tablicę haszującą
rozmiaru size, przechowującą liczby nieujemne. Tablica korzysta z funkcji haszującej 
`int hash(int x)` i liniowego rozwiązywania konfliktów (ujemne wartości w tablicy table oznaczają wolne pola). Doskonałością takiej tablicy nazywamy liczbę elementów x takich, że pozycja x w tablicy to `hash(x) mod size` (a więc x jest na ”swojej” pozycji). Proszę napisać funkcję: `void enlarge( HT* ht);`, która powiększa tablicę dwukrotnie i wpisuje elementy w takiej kolejności, by doskonałość powstałej tablicy była jak największa. Funkcja powinna być możliwie jak najszybsza.

### Zadanie 3

Dany jest ciąg klocków (k1, ..., kn). Klocek ki zaczyna się na pozycji ai
i ciągnie się do pozycji bi (wszystkie pozycje to liczby naturalne) oraz ma wysokość 1. Klocki układane są po kolei. Jeśli klocek nachodzi na któryś z poprzednich, to jest przymocowywany na szczycie poprzedzającego klocka. Na przykład dla klocków o pozycjach (1,3), (2,5), (0,3), (8,9), (4,6) powstaje konstrukcja o wysokości trzech klocków. Proszę podać możliwie jak najszybszy algorytm, który oblicza wysokość powstałej konstrukcji (bez implementacji) oraz oszacować jego złożoność obliczeniową.

