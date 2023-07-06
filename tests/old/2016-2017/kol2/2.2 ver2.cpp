// by Jan "Regzand" Golda

using namespace std;

struct HT {
    int* table;
    int size;
};

// dana funkcja
int hash(int x);

void enlarge(HT* ht){
    // nowa tablica
    int size = ht->size * 2;
    int *T = new int[size];

    // wypelnienie tablicy pustymi miejscami
    for(int i = 0; i<size; i++)
        T[i] = -1;

    // przepisanie elementow tylko na "swoje" miejsca
    for(int i = 0; i<ht->size; i++){

        // jezeli jest to wolne pole idziemy dalej
        if(ht->table[i] == -1)
            continue;

        // wyliczenie porzadanego indeksu w nowej tablicy
        int index = hash(ht->table[i]) % size;

        // jezeli indeks jest zajety idziemy dalej
        if(T[index] != -1)
            continue;

        // przeniesienie do nowej tablicy
        T[index] = ht->table[i];
        ht->table[i] = -1;
    }

    // przepisanie pozostalych elementow
    for(int i = 0; i<size; i++){

        // jezeli jest to wolne pole idziemy dalej
        if(ht->table[i] == -1)
            continue;

        // wyliczenie porzadanego indeksu w nowej tablicy
        int index = hash(ht->table[i]) % size;

        // poszukiwanie wolnego miejsca (liniowe rozwiazywanie konfliktow)
        // nie sprawdzam zapetlenia poniewaz jako za mamy dwa razy wiecej miejsca w tablicy to na pewno znajdziemy wolne miejsce
        while(true){
            // jezeli jest wolne miejsce
            if(T[index] != -1){
                // przeniesienie do nowej tablicy i zakonczenie poszukiwan wolnego miejsca
                T[index] = ht->table[i];
                ht->table[i] = -1;
                break;
            }

            // zwiekszenie indeksu
            index = (index+1) % size;
        }
    }

    // przepiecie tablicy
    ht->table = T;
    ht->size = size;
}
