#include<iostream>
#include<string>
using namespace std;
int a;
struct setA
{
    int val;
    setA *left,*right;
    bool contain;
};
void inorder(setA *root)
{
    if(root==NULL) return;
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);


}
setA *creatSet(string tab[],int n)
{
    setA *newSet=new setA;
    newSet->val=-1;
    newSet->contain=false;
    newSet->right=NULL;
    newSet->left=NULL;
    setA *tmp=newSet;

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<tab[i].length();j++)
        {
            if(tab[i][j]=='1')
            {
                if(tmp->right==NULL)
                {
                    setA *creat=new setA;
                    creat->val=1;
                    creat->left=NULL;
                    creat->right=NULL;
                    if(j==tab[i].length()-1) creat->contain=true;
                    else creat->contain=false;
                    tmp->right=creat;
                    tmp=creat;
                }
                else
                {
                    if(j==tab[i].length()-1) tmp->contain=true;
                    tmp=tmp->right;
                }
            }
            else
            {
                if(tmp->left==NULL)
                {
                    setA *creat=new setA;
                    creat->val=0;
                    creat->left=NULL;
                    creat->right=NULL;
                    if(j==tab[i].length()-1) creat->contain=true;
                    else creat->contain=false;
                    tmp->left=creat;
                    tmp=creat;
                }
                else
                {   if(j==tab[i].length()-1) tmp->contain=true;
                    tmp=tmp->left;
                }
            }
        }
       // inorder(newSet);
        //cout << endl << endl;
        tmp=newSet;
    }
    return newSet;
}
bool contains(setA *a, string s)
{

    for(int i=0;i<s.length()-1;i++)
    {
        if(s[i]=='1')
        {
            if(a->right!=NULL) a=a->right;
            else return false;
        }
        else
        {
            if(a->left!=NULL) a=a->left;
            else return false;
        }
    }
    if(s[s.length()-1]=='1')
    {
        if(a->right==NULL) return false;
        else
        {
            if(a->right->contain!=true) return false;
        }
    }
    else
    {
        if(a->left==NULL) return false;
        else
        {
            if(a->left->contain!=true) return false;
        }
    }
    return true;
}

int main()
{
    string tab[6]={"10","10111","10101","0","1000","11111"};
    string nie[2]={"110","1001"};
    //cout << tab[0][0];
    setA *head=NULL;
    head=creatSet(tab,6);
    //inorder(head);
    if(contains(head,nie[1])) cout << "tak";
    else cout << "nie";
}
