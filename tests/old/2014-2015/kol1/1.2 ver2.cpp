#include<iostream>
using namespace std;
struct node
{
    node *next;
    int val;
};
struct TwoLists
{
    node *even; // parzyste
    node *odd;  // nieparzyste
};
void add_to_list_at_beg(node* &head, int value)
{
    node *tmp=new node;
    tmp->val=value;
    tmp->next=head;
    head=tmp;
}
void print_list(node *head)
{
    while(head!=NULL)
    {
        cout << head->val << " ";
        head=head->next;
    }
}
TwoLists split(node *head)
{
    TwoLists S;
    S.even=NULL;
    S.odd=NULL;
    node *tmp;
    while(head!=NULL)
    {
        if((head->val)%2==0)
        {
            tmp=head;
            head=head->next;
            tmp->next=S.even;
            S.even=tmp;

        }
        else
        {
            tmp=head;
            head=head->next;
            tmp->next=S.odd;
            S.odd=tmp;

        }

    }
    while(S.odd!=NULL)
    {
        cout << S.odd->val << " ";
        S.odd=S.odd->next;
    }
    cout << endl;
     while(S.even!=NULL)
    {
        cout << S.even->val << " ";
        S.even=S.even->next;
    }
    return S;
}
int main()
{
    node *head=NULL;
    for(int i=10;i>0;i--)
    {
        add_to_list_at_beg(head,i);
    }
    print_list(head);
    cout << endl << endl;
    split(head);
}
