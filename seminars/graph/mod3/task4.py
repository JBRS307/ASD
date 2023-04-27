#Dana jest tabela kursów walut, dla każdej pary walut x, y
#Wartość k[x][y] oznacza ile trzeba zapłacić waluty x, żeby otrzymać 1 walutę

#Iloczyn wag musi być większy niż 1
#Mozna puścić bellmana forda po zlogarytmowanych wagach, jeśli jest ujemny cykl, znaczy, że na pewno tak się da.


#Dane jest drzewo ważone. Znajdź wierzchołek drzewa, w którym odległość do najdalszego wierzchołka jest minimalna