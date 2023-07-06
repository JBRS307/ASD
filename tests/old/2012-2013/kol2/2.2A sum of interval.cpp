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
    int left_sum;
    int right_sum;
};

void insert (node *&root, int value)
{
    node *el = new node;
    el->val=value;
    el->left=NULL;
    el->right=NULL;
    el->parent=NULL;
    el->left_sum=0;
    el->right_sum=0;

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

void add_sums (node* &root)
{
    if (root==NULL) return;

    if (root->left==NULL) root->left_sum=0;
    if (root->right==NULL) root->right_sum=0;

    if (root->left!=NULL)
    {
        add_sums(root->left);
        root->left_sum=root->left->left_sum + root->left->val + root->left->right_sum;
    }

    if (root->right!=NULL)
    {
        add_sums(root->right);
        root->right_sum=root->right->left_sum + root->right->val + root->right->right_sum;
    }
}

int sum_x (node* root, int x)
{
    int sum=0;
    node* ptr=root;

    while (ptr->val!=x)
    {
        if (x < ptr->val)
        {
            if (ptr->right!=NULL) sum+=ptr->right->left_sum+ptr->right->val+ptr->right->right_sum;
            sum+=ptr->val;
            ptr=ptr->left;
        }
        else ptr=ptr->right;
    }

    if (ptr->right!=NULL) sum+=ptr->right->left_sum+ptr->right->val+ptr->right->right_sum;
    sum+=x;
    return sum;
}

int sum_y (node* root, int y)
{
    int sum=0;
    node* ptr=root;

    while (ptr->val!=y)
    {
        if (y > ptr->val)
        {
            if (ptr->left!=NULL) sum+=ptr->left->left_sum+ptr->left->val+ptr->left->right_sum;
            sum+=ptr->val;
            ptr=ptr->right;
        }
        else ptr=ptr->left;
    }

    if (ptr->left!=NULL) sum+=ptr->left->left_sum+ptr->left->val+ptr->left->right_sum;
    sum+=y;
    return sum;
}

int sum_between (node* root, int x, int y)
{
    if (x==y) return x;

    node* ptr=root;
    while ((ptr->val > x && ptr->val > y) || (ptr->val < x && ptr->val < y ))
    {
        if (ptr->val > x) ptr=ptr->left;
        else ptr=ptr->right;
    }

    int result=0;

    if (ptr->val!=x) result+=sum_x(ptr->left,x);
    else result+=x;

    if (ptr->val!=y) result+=sum_y(ptr->right,y);
    else result+=y;

    if (ptr->val!=x && ptr->val!=y) result+=ptr->val;

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

    add_sums(root);

    cout << sum_between(root,1,4);

    return 0;
}