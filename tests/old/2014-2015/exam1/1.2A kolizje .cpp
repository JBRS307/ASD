/* Funkcja oblicza srednia ilosc krokow przy liniowym rozwiazywaniu kolizji w danej tablicy haszujacej */

#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>
#include <string>
using namespace std;

struct HT
{
    string *key; //tablica na klucze danych
    int *data; //tablica na dane
    bool *free; //pole wolne czy zajete
    int size; //rozmiar tablicy
};

int hash (string key, int size)
{
    int hash=0;
    for (int i=0; i<key.length(); i++) hash^=(hash<<3)+key[0];
    return hash%size;
}

int take_place (HT *ht, HT &hashtable, int index)
{
    if (hashtable.size==0) return 0;
    int hash_value=hash(ht->key[index],hashtable.size);
    int steps=0;

    while (hashtable.free[hash_value]==false && steps<hashtable.size)
    {
        hash_value=(hash_value+1)%hashtable.size;
        steps++;
    }

    hashtable.free[hash_value]=false;
    return steps;
}

double averageAccess (HT *ht)
{
    HT hashtable;
    hashtable.size=ht->size;
    hashtable.free = new bool[hashtable.size];
    for (int i=0; i<hashtable.size; i++) hashtable.free[i]=true;
    int steps=0;
    for (int i=0; i<hashtable.size; i++) steps+=take_place(ht,hashtable,i);

    double result = (double)steps / (double)hashtable.size;
    return result;
}