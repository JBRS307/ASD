/* Program sumuje elementy w drzewie BST z przedzialu [x,y], korzystajac z zapisania w kazdym node'dzie informacji o sumach lewego i prawego poddrzewa. */

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
};

void insert (node *&root, int value)
{
    node *el = new node;
    el->val=value;
    el->left=NULL;
    el->right=NULL;
    el->parent=NULL;

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

int get_size (node* root)
{
    if (root==NULL) return 0;

    int size=1;

    if (root->left!=NULL) size+=get_size(root->left);
    if (root->right!=NULL) size+=get_size(root->right);

    return size;
}

int count_x (node* root, int x)
{
    int count=0;
    node* ptr=root;

    while (ptr->val!=x)
    {
        if (x < ptr->val)
        {
            if (ptr->right!=NULL) count+=get_size(root->right);
            count++;
            ptr=ptr->left;
        }
        else ptr=ptr->right;
    }

    if (ptr->right!=NULL) count+=get_size(root->right);
    count++;
    return count;
}

int count_y (node* root, int y)
{
    int count=0;
    node* ptr=root;

    while (ptr->val!=y)
    {
        if (y > ptr->val)
        {
            if (ptr->left!=NULL) count+=get_size(root->left);
            count++;
            ptr=ptr->right;
        }
        else ptr=ptr->left;
    }

    if (ptr->left!=NULL) count+=get_size(root->left);
    count++;
    return count;
}

int count_between (node* root, int x, int y)
{
    if (x==y) return 1;

    node* ptr=root;
    while ((ptr->val > x && ptr->val > y) || (ptr->val < x && ptr->val < y ))
    {
        if (ptr->val > x) ptr=ptr->left;
        else ptr=ptr->right;
    }

    int result=0;

    if (ptr->val!=x) result+=count_x(ptr->left,x);
    else result+=1;

    if (ptr->val!=y) result+=count_y(ptr->right,y);
    else result+=1;

    if (ptr->val!=x && ptr->val!=y) result+=1;

    return result;
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

    cout << count_between(root,1,4);

    return 0;
}