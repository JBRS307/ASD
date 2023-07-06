/* Program implementuje drzewo BST przechowujace lancuchy znakow bedace liczbami binarnymi. */

#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>
#include <string>
using namespace std;

struct node
{
    string number;
    node* left;
    node* right;
    bool is_end;
};

struct Set
{
    node* root;
};

void print_not_empty (node *ptr)
{
    if (ptr!=NULL)
    {
        print_not_empty(ptr->left);
        cout <<ptr->number <<" ";
        print_not_empty(ptr->right);
    }
}

void print (node *ptr)
{
    cout <<"\n";
    if (ptr==NULL) cout <<"The tree is empty!";
    else print_not_empty(ptr);
    cout <<"\n";
}

node* newNode (string number)
{
    node* Node = new node;
    Node->left=NULL;
    Node->right=NULL;
    Node->number=number;
    Node->is_end=false;
    return Node;
}

bool contains (Set a, string s)
{
    if (a.root==NULL) return false;
    node* ptr=a.root;
    int i=0;
    int length=s.length();

    while (i<length)
    {
        if (s[i]=='0')
        {
            if (ptr->left!=NULL) ptr=ptr->left;
            else return false;
        }
        else if (s[i]=='1')
        {
            if (ptr->right!=NULL) ptr=ptr->right;
            else return false;
        }
        i++;
    }
    if (ptr->is_end) return true;
    else return false;
}

void add_string (Set &set, string number)
{
    int length=number.length();
    int i=0;
    node* ptr=set.root;

    while (i<length)
    {
        if (number[i]=='0')
        {
            if (ptr->left!=NULL) ptr=ptr->left;
            else
            {
                node* tmp = newNode("0");
                ptr->left=tmp;
                ptr=ptr->left;
            }
        }
        else if (number[i]=='1')
        {
            if (ptr->right!=NULL) ptr=ptr->right;
            else
            {
                node* tmp = newNode("1");
                ptr->right=tmp;
                ptr=ptr->right;
            }
        }
        i++;
    }
    ptr->is_end=true;
}

Set create_Set (string A[], int n)
{
    Set numbers;
    node* root = new node; root->left=root->right=NULL;
    numbers.root=root;
    for (int i=0; i<n; i++) add_string(numbers,A[i]);
    return numbers;
}

int main()
{
    int n=3;

    string tab[n];
    tab[0]="0001";
    tab[1]="0010";
    tab[2]="0011";

    Set numbers = create_Set(tab,n);

    bool exists=contains(numbers,"001");
    if (exists) cout <<"Exists";
    else cout <<"Nonexistent";

    return 0;
}