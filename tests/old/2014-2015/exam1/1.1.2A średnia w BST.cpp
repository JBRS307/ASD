/* Funkcja oblicza srednia wartosc elementow w drzewie BST */

#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>
#include <string>
using namespace std;

struct BST
{
    BST *left;
    BST *right;
    int value;
};

void get_numbers (BST *T, int &sum, int &counter)
{
    if (T==NULL) return;

    sum+=T->value;
    counter++;
    if (T->left!=NULL) get_numbers(T->left,sum,counter);
    if (T->right!=NULL) get_numbers(T->right,sum,counter);
}

double average (BST *T)
{
    if (T==NULL) return 0;
    int sum=0;
    int counter=0;
    get_numbers(T,sum,counter);
    return ((double) sum / (double) counter);
}