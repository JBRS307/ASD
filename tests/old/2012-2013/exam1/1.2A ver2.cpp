/* Funkcja scala 2 drzewa BST tak, ze drzewo wynikowe zawiera tylko elementy znajdujace sie na wejsciu w obu drzewach. */

#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>
#include <string>
using namespace std;

struct node
{
    int val;
    node* parent;
    node* left;
    node* right;
};

struct listNode
{
    node* Node;
    listNode* prev;
    listNode* next;
};

listNode* tree_to_list (node* root)
{
    if (root->parent==NULL)
    {
        listNode* result = new listNode; result->prev=NULL; result->next=NULL;
        result->Node=root;
        listNode* previous=tree_to_list(root->left);
        previous->next=result; result->prev=previous;
        listNode* next=tree_to_list(root->right);
        next->prev=result; result->next=next;
        return result;
    }
    else
    {
        if (root->left!=NULL || root->right!=NULL)
        {
            listNode* newNode = new listNode; newNode->prev=NULL; newNode->next=NULL;
            newNode->Node=root;
            if (root->left!=NULL)
            {
                listNode* previous=tree_to_list(root->left);
                previous->next=newNode; newNode->prev=previous;
            }
            if (root->right!=NULL)
            {
                listNode* next=tree_to_list(root->right);
                next->prev=newNode; newNode->next=next;
            }
            return newNode;
        }
        else
        {
            listNode* newNode = new listNode; newNode->prev=NULL; newNode->next=NULL;
            newNode->Node=root;
            return newNode;
        }
    }
}

listNode* merge_lists (listNode* list1, listNode* list2, int &length)
{
    listNode* ptr1=list1;
    listNode* ptr2=list2;

    while (ptr1->prev!=NULL) ptr1=ptr1->prev;
    while (ptr2->prev!=NULL) ptr2=ptr2->prev;

    listNode* result=NULL;
    listNode* ptr3=result;
    listNode* tmp;

    while (ptr1!=NULL && ptr2!=NULL)
    {
        if (ptr1->Node->val==ptr2->Node->val)
        {
            ptr3->next=ptr1;
            ptr1=ptr1->next;
            tmp=ptr2; ptr2=ptr2->next; delete tmp;
            ptr3=ptr3->next;
            length++;
        }
        else
        {
            if (ptr1->Node->val < ptr2->Node->val) ptr1=ptr1->next;
            else ptr2=ptr2->next;
        }
    }

    ptr3->next=NULL;

    ptr3=result;
    int iter=0;
    while (iter<length/2)
    {
        ptr3=ptr3->next;
        iter++;
    }
    return ptr3;
}

node* list_to_tree (listNode* list, int length)
{
    node* root=list->Node;
    listNode* ptr1;
    listNode* ptr2;
    int counter=0;
    while (counter<length/2) ptr1=ptr1->prev;
    counter=0;
    while (counter<length/2) ptr2=ptr2->next;
    root->left=list_to_tree(ptr1,length/2);
    root->right=list_to_tree(ptr2,length/2);
    return root;
}

node* merge_BST (node* root1, node* root2)
{
    listNode* list1=tree_to_list(root1);
    listNode* list2=tree_to_list(root2);

    int length=0;
    listNode* list3=merge_lists(list1,list2,length);
    node* result=list_to_tree(list3,length);
    return result;
}