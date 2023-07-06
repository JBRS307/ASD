/* Funkcja powieksza dwukrotnie tablice haszujaca z maksymalna doskonaloscia. */

#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>
#include <string>
#include <limits.h>
using namespace std;

struct HT
{
    int* table;
    int size;
};

int hash (int x)
{
    int result=0;
    result^=(x>>2)+x;
    return result;
}

void enlarge (HT* ht)
{
    HT* result = new HT;
    result->size=2*ht->size;
    result->table = new int[result->size];
    for (int i=0; i<result->size; i++) result->table[i]=-1;

    for (int i=0; i<ht->size; i++)
    {
        int new_index=hash(ht->table[i])%result->size;
        if (new_index==ht->table[i])
        {
            result->table[new_index]=ht->table[i];
            ht->table[i]=-1;
        }
    }

    for (int i=0; i<ht->size; i++)
    {
        if (ht->table[i]!=-1)
        {
            int new_index=hash(ht->table[i])%result->size;
            while (result->table[new_index]!=-1) new_index=(new_index+1)%result->size;
            result->table[new_index]=ht->table[i];
        }
    }
    ht->size=2*(ht->size);
    ht->table=result->table;
}