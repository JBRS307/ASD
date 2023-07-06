/* Program scala dwie skiplisty. */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>

typedef struct Node {
    int val;
    int height;
    struct Node** next;
} Node;

typedef struct SkipList {
    int max_height;
    Node* start;
    Node* end;
} SkipList;

int getHeight(int max_h) {
    int h = 1;
    float p = 0.8;
    while (h < max_h && rand() / (RAND_MAX + 1.) < p) h++;
    return h;
}


Node* newNode(int val, int max_height) {
    Node *n = (Node*) malloc(sizeof(Node));
    n->val = val;
    n->height = getHeight(max_height);
    n->next = (Node**) malloc(sizeof(Node*)*(n->height));

    for (int i=0; i<n->height; i++) n->next[i]=NULL;

// allocate, set all pointers to NULL
    return n;
}

void deleteNode(Node* n) {
    free(n->next);
    free(n);

    // remove Node from memory
}

SkipList* newSkipList(int max_height) {
    SkipList* list = malloc(sizeof(*list));
    list->max_height = max_height;

    list->start = (Node*) malloc(sizeof(Node));
    list->end = (Node*) malloc(sizeof(Node));

    list->start->height = max_height;
    list->end->height = max_height;

    list->start->next = (Node**) malloc(max_height*sizeof(Node*));
    list->end->next = (Node**) malloc(max_height*sizeof(Node*));

    for(int i=0; i<max_height; i++) {
        list->start->next[i] = list->end;
        list->end->next[i] = NULL;
    }

    return list;
}

void deleteSkipList(SkipList* list) {
    Node *ptr;
    Node *tmp;
    ptr=list->start->next[0];
    while (ptr!=list->end)
    {
        tmp=ptr;
        ptr=ptr->next[0];
    }

    free(list);

    // call deleteNode() on every node in skiplist
    // call free() on list
}

void insert(SkipList* list, Node* node)
{
    Node* tmp = list->start;
    int i = list->max_height - 1;
    while (i >= 0)
    {
        while (tmp->next[i]->next[i]!=NULL && tmp->next[i]->val < node->val) tmp=tmp->next[i];
        if (i+1 <= node->height)
        {
            node->next[i]=tmp->next[i];
            tmp->next[i]=node;
        }
        i--;
    }
}

Node* find(SkipList* list, int val) {
    Node* tmp = list->start;
    int i = list->max_height - 1;
    while (i >= 0)
    {
        while (tmp->next[i]!=list->end && tmp->next[i]->val<val) tmp=tmp->next[i];
        i--;
        // while value of tmp->next[i] is less than value of given node, go ahead
    }

    if (tmp==list->end) return NULL;
    if (tmp->next[0]->val == val) return tmp->next[0];
    else return NULL;

    // return desired node or NULL if such value doesn't exist in the skiplist
}

void print (SkipList* list)
{
    Node *ptr=list->start->next[0];
    if (list->start==list->end)
    {
        printf("\nLista pusta!\n");
        return;
    }
    else while (ptr!=list->end)
    {
        printf("%d ", ptr->val);
        ptr=ptr->next[0];
    }
}

void removeFromList(SkipList* list, Node* node, int height)
{
    Node *tmp=list->start;
    Node *tmp2;
    int i=node->height-1;
    while (i>=0)
    {
        while (tmp->next[i]!=NULL && tmp->next[i]->val<node->val) tmp=tmp->next[i];
        if (tmp->next[i]!=NULL && tmp->next[i]->val==node->val)
        {
            tmp2=tmp->next[i];
            tmp->next[i]=tmp2->next[i];
        }

        // while value of tmp->next[i] is less than value of given node, go ahead
        // remove (unplug) given node on level 'i'
        i--;
    }
}

SkipList* mergeSkipLists (SkipList *list1, SkipList *list2)
{
    if (list1->start->next[0]==list1->end) return list2;
    if (list2->start->next[0]==list2->end) return list1;

    int max_height=fmax(list1->max_height,list2->max_height);
    SkipList *list3 = newSkipList(max_height);

    Node *ptr1, *ptr2, *ptr3;

    int i=max_height-1;

    while (i>=0)
    {
        ptr1=list1->start;
        ptr2=list2->start;
        ptr3=list3->start;

        while (ptr1->next[i]!=list1->end && ptr2->next[i]!=list2->end)
        {
            if (ptr1->next[i]->val < ptr2->next[i]->val)
            {
                ptr3->next[i]=ptr1->next[i];
                ptr1->next[i]=ptr1->next[i]->next[i];
                ptr3=ptr3->next[i];
            }
            else
            {
                ptr3->next[i]=ptr2->next[i];
                ptr2->next[i]=ptr2->next[i]->next[i];
                ptr3=ptr3->next[i];
            }
        }

        if (ptr1->next[i]!=list1->end)
        {
            ptr3->next[i]=ptr1->next[i];
            while (ptr1->next[i]!=list1->end) ptr1=ptr1->next[i];
            ptr1->next[i]=list3->end;
        }
        else
        {
            ptr3->next[i]=ptr2->next[i];
            while (ptr2->next[i]!=list2->end) ptr2=ptr2->next[i];
            ptr2->next[i]=list3->end;
        }

        i--;
    }

    return list3;
}

int main(int argc, char** argv) {
    /*
     * test data:
     * Z - number of test cases
     * h, I, R, F - max height of single node (h), number of values to insert (I), remove(R) and find (F)
     * I values to insert
     * R values to remove (should exist in the previous set)
     * F values to find
     * Output:
     * F lines, "y" or "n" in each one - depending on whether given value is present in the skiplist or not
    */
    srand(time(NULL));
    int n=10;
    int h=10;

        SkipList* list1 = newSkipList(h);
        SkipList* list2 = newSkipList(h);
        int x;
        for(int j=0; j<n; j++)
        {
            x=rand()%100+1;
            insert(list1, newNode(x, h));
            x=rand()%100+1;
            insert(list2, newNode(x, h));

        }

        printf("\nLista 1:\n"); print(list1);
        printf("\nLista 2:\n"); print(list2);

        SkipList *list3 = mergeSkipLists(list1,list2);
        printf("\n\nLista 3:\n"); print(list3);
}