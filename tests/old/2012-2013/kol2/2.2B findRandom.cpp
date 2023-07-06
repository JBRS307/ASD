/* Program zwraca losowy element drzewa (w sensie kolejnoœci) dziêki trzymaniu w wêz³ach informacji o rozmiarze ich poddrzewa. */

#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>
#include <string>
#include <limits.h>
using namespace std;

struct node
{
    int val;
    node* parent;
    node *left;
    node *right;
    int size;
};

void insert (node *&root, int value)
{
    node *el = new node;
    el->val=value;
    el->left=NULL;
    el->right=NULL;
    el->parent=NULL;
    el->size=1;

    if (root==NULL)
    {
        root=el;
        return;
    }

    node *slow=NULL;
    node *fast=root;

    while (fast!=NULL)
    {
        slow=fast;
        if (el->val < fast->val) fast=fast->left;
        else fast=fast->right;
    }

    el->parent=slow;
    if (el->val < slow->val) slow->left=el;
    else slow->right=el;
}

int add_sizes (node* root)
{
    if (root==NULL) return 0;

    int tree_size=1;

    if (root->left!=NULL) root->size+=add_sizes(root->left);
    if (root->right!=NULL) root->size+=add_sizes(root->right);

    tree_size+=root->size-1;
    return tree_size;
}

int random (int k) { return rand()%k; }

int findRandom (node* T)
{
    if (T==NULL) return -1;
    int tree_size=add_sizes(T);
    int element_position=random(tree_size)+1;

cout <<"Element na pozycji " <<element_position <<" to ";

    bool found=false;
    int curr_position;
    node* ptr=T;

    while (found==false)
    {
        if (ptr->left==NULL) curr_position=1;
        else if (ptr->right==NULL) curr_position=ptr->size;
        else curr_position=ptr->size - ptr->right->size;

        if (curr_position > element_position) ptr=ptr->left;
        else if (curr_position < element_position)
        {
            element_position=element_position-curr_position;
            ptr=ptr->right;
        }
        else found=true;
    }

    return ptr->val;
}

int main()
{
    srand(time(NULL));
    node *root=NULL;

    insert(root,2);
    insert(root,1);
    insert(root,3);
    insert(root,5);
    insert(root,4);
    insert(root,6);

    cout << findRandom(root);

    return 0;
}