/* Student chce wypuscic n roznych pokemonow (numerowanych od 0 do n-1) z pokeballi. Wypuszczony pokemon od razu atakuje, chyba, ze:
a) jest spokojny (jego ofiara nie ma poprawnego numeru)
b) w okolicy sa min. 2 uwolnione pokemony, na ktore on poluje
Program implementuje funkcje int* releaseThemAll (HuntingList* list, int n), gdzie list to lista z pokemonami z elementami typu:

struct HuntingList
{
HuntingList* next;
int predator;     // numer danego pokemona
int prey;         // numer pokemona, na którego poluje dany
};

Funkcja zwraca n-elementowa tablice z numerami pokemonow w kolejnosci wypuszczania lub NULL, jesli nie mozna ich wypuscic bez atakowania wypuszczajcego.
Kazdy wypuszczony pokemon zostaje w okolicy.
 */

#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>
#include <string>
using namespace std;

struct HuntingList
{
    HuntingList* next;
    int predator;        //numer danego pokemona
    int prey;            //na kogo poluje dany pokemon
};

struct node
{
    int id;
    node* next;
};

struct pokemon
{
    int released;
    node* my_prey;
    node* hunting_me;
};

void release_hunter (pokemon pokemons[], int release_order[], int n, int &iter, int id)
{
    node* ptr; node* tmp;
    int counter=0;

    ptr=pokemons[id].my_prey;
    while (ptr!=NULL && counter<2)
    {
        counter+=pokemons[ptr->id].released;
        ptr=ptr->next;
    }
    if (counter<2) return;

    release_order[iter]=id;
    iter++;
    pokemons[id].released=1;

    ptr=pokemons[id].hunting_me;

    while (ptr!=NULL)
    {
        if (pokemons[ptr->id].released==0) release_hunter(pokemons,release_order,n,iter,ptr->id);
        tmp=ptr;
        ptr=ptr->next;
        delete tmp;
    }
}

int* releaseThemAll (HuntingList* list, int n)
{
    pokemon pokemons[n];
    int release_order[n];
    for (int i=0; i<n; i++)
    {
        release_order[i]=-1;
        pokemons[i].released=0;
        pokemons[i].my_prey=NULL;
        pokemons[i].hunting_me=NULL;
    }

    HuntingList* ptr=list;

    while (ptr!=NULL)
    {
        node* hunter = new node;
        hunter->id=ptr->predator;
        hunter->next=pokemons[ptr->prey].hunting_me;
        pokemons[ptr->prey].hunting_me=hunter;

        node* prey = new node;
        prey->id=ptr->prey;
        prey->next=pokemons[ptr->predator].my_prey;
        pokemons[ptr->predator].my_prey=prey;
    }

    int iter=0;

    for (int i=0; i<n; i++)
        if (pokemons[i].my_prey==NULL)
        {
            release_order[iter]=i;
            iter++;
            pokemons[i].released=1;
        }

    for (int i=0; i<n; i++)
        if (pokemons[i].my_prey!=NULL)
            release_hunter(pokemons,release_order,n,iter,i);

    if (release_order[n-1]!=-1)
    {
        int* result=release_order;
        return result;
    }
    else return NULL;
}