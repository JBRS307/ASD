#Zaimplementuj kruskala (kukla) mając find/union i posortowaną listę

#Znajdź w ważonym grafie skierowanym cykl o najmniejszej wadze
#Floyd warshall, potem szukasz dla każdej pary odległości w dwie strony, dodajesz i bierzesz najmniejszą



#W pewnym państwie, w którym znajduje się n miast postanowiono połączyć miasta autostradami
#Miasta to pary (x, y) - ich współrzędne w układzie kartezjańskim (ja pierdolę)
#Chcemy je zbudować tak żeby zminimalizować czas między otwarciem pierwszej i ostatniej.
#Czas zbudowania autostrady w dniach to sufit z jej długości w kilomatrach.
#Wszystkie zaczynamy budować w tym samym czasie
#
#Kruskal - sprawdzasz drzewo rozpinające i odejmujesz najkrótszą od najdłuższej. Potem wywalasz najktórszą i znowu.