/* Funkcja sprawdza, czy dana tablica haszujaca ma prawidlowo wpisane dane.
Haszujemy stringi z tablicy *key, tablica haszujaca to *data, zajetosc *data sprawdza *free, a sama *data przechowuje wartosci haszy. */

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

bool checkHT (HT *ht, HT &hashtable)
{
    if (hashtable.size==0) return true;
    bool flag=true;

    for (int i=0; i<ht->size && flag==true; i++)
    {
        int hash_value=hash(ht->key[i],ht->size);
        int hash_data=hash_value;

        int n=0;
        while (ht->free[hash_value]==false && n < ht->size)
        {
            if (ht->data[hash_value]==hash_data) break;
            hash_value=(hash_value+1)%ht->size;
            n++;
        }
        if (n==ht->size) flag=false;
        if (ht->free[hash_value]==true) flag=false;
    }

    return flag;
}