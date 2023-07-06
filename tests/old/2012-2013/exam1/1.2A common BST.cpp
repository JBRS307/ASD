#include<iostream>
#include<stack>
using namespace std;
struct node
{
    int val;
    node *right,*left,*parent;
};
void add_node(node* &root,int value)
{
    node *tmp=new node;
    tmp->val=value;
    tmp->left=tmp->right=tmp->parent=NULL;
    if(root==NULL)
    {
        root=tmp;
        return;
    }

    node *p=root; // element do przeszukiwania
    node *q=NULL; // previous dla parenrta

    while(p!=NULL)
    {
        if(p->val<tmp->val)
        {
            q=p;
            p=p->right;
        }
        else
        {
            q=p;
            p=p->left;
        }
    }
    if(q->val<value)
        q->right=tmp;
    else
        q->left=tmp;

    tmp->parent=q;

}
void commontBST(node *root1, node *root2, node *&dest)
{
    stack <node *> stack1,s1,s2;
    while(true)
    {
        if(root1)
        {
            s1.push(root1);
            root1=root1->left;
        }
        else if(root2)
        {
            s2.push(root2);
            root2=root2->left;
        }
        else if(!s1.empty() and !s2.empty())
        {
            root1=s1.top();
            root2=s2.top();
            if(root1->val==root2->val)
            {
                add_node(dest,root1->val);
                s1.pop();
                s2.pop();
                root1=root1->right;
                root2=root2->right;
            }
            else if(root1->val<root2->val)
            {
                s1.pop();
                root1=root1->right;
                root2=NULL;
            }
            else if(root1->val>root2->val)
            {
                s2.pop();
                root2=root2->right;
                root1=NULL;
            }
        }
        else
            break;


    }
}
void inOrder(node *bst)
{
    if(bst)
    {
        inOrder(bst->left);
        cout << bst->val << " ";
        inOrder(bst->right);
    }
}
int main()
{
    node *tree1=NULL;
    node *tree2=NULL;
    node *dest=NULL;
    add_node(tree1,10);
    add_node(tree1,5);
    add_node(tree1,12);
    add_node(tree1,2);
    add_node(tree1,8);
    add_node(tree1,11);
    add_node(tree1,18);
    add_node(tree2,5);
    add_node(tree2,2);
    add_node(tree2,30);
    add_node(tree2,1);
    add_node(tree2,4);
    add_node(tree2,10);
    commontBST(tree1,tree2,dest);
    inOrder(dest);

}
