// by Jan "Regzand" Golda

#include <stdio.h>
#include <algorithm>

using namespace std;

struct Field {
    int value;
    int long_j;
    int short_j;
};

int findBestPath(Field *T, int N){

    // tablica maksymalnych sum
    int sum[N];

    // wyliczenie sum
    for(int i = N-1; i>=0; i--){
        // mozliwe wartosci po wynonaniu skokow (zabezpieczenie przed wykroczeniem poza tablice)
        int a = ( i+T[i].long_j  < N ? sum[i+T[i].long_j ] : 0);
        int b = ( i+T[i].short_j < N ? sum[i+T[i].short_j] : 0);

        // wybieramy lepszy skok
        sum[i] = T[i].value + max(a, b);
    }

    // odpowiedz
    return sum[0];
}

int main(){

    // ilosc pol
    int N;
    scanf("%d", &N);

    // wczytanie pol
    Field T[N];
    for(int i = 0; i<N; i++)
        scanf("%d %d %d", &T[i].value, &T[i].long_j, &T[i].short_j);

    // wypisanie wyniku
    printf("Najlepsz mozliwa suma: %d\n", findBestPath(T, N));

    return 0;
}
