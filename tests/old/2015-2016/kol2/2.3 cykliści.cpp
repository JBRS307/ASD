/* Zadanie z grupami cyklistow z kolokwium 2015/2016 */

#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>
#include <string>
#include <limits.h>
using namespace std;

struct cyclist
{
    int id;
    int n_id;
};

struct better_cyclist
{
    int id;
    int n_id;
    int p_id;
};

int hash_function (int id)
{
    int hash=0;
    hash^=(id>>2)+id;
    return hash;
}

void add_to_hashtable (better_cyclist better_cyclists[], cyclist cyclists[], int better_n, int n, int index)
{
    int hash = hash_function(cyclists[index].id)%better_n;
    int i=0;

    while (better_cyclists[hash].id!=-1 && i<better_n)
    {
        hash=(hash+1)%better_n;
        i++;
    }
    if (i==better_n) return;

    better_cyclists[hash].id=cyclists[index].id;
    better_cyclists[hash].n_id=cyclists[index].n_id;
    better_cyclists[hash].p_id=-1;
}

int smallestGroup (cyclist cyclists[], int n)
{
    better_cyclist better_cyclists[2*n];
    for (int i=0; i<2*n; i++) better_cyclists[i].id=-1;
    for (int i=0; i<n; i++) add_to_hashtable(better_cyclists,cyclists,2*n,n,i);

    int index;
    for (int i=0; i<n; i++)
    {
        index=hash_function(cyclists[i].id);
        better_cyclists[better_cyclists[index].n_id].p_id=better_cyclists[index].id;
    }

    int smallestGroup=INT_MAX;
    int counter;
    int iter;

    for (int i=0; i<2*n; i++)
    {
        if (better_cyclists[i].id!=-1 && better_cyclists[i].p_id==-1)
        {
            counter=1;
            iter=i;
            while (better_cyclists[iter].n_id!=-1)
            {
                iter=hash_function(better_cyclists[iter].n_id);
                counter++;
            }
            if (counter<smallestGroup) smallestGroup=counter;
        }
    }

    return smallestGroup;
}