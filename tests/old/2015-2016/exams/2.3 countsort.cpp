#include<iostream>
#include<cstring>
using namespace std;
int getMax(char *A[], int n)
{
    int m=strlen(A[0]);
    for(int i=1;i<n;i++)
        if(m<strlen(A[i]))
            m=strlen(A[i]);
    return m;
}
int getCharByPosit(char *word, int posit)
{
    if(strlen(word)<posit) return 0;
    else
    {
        if(word[posit]=='a') return 0;
        else return 1;
    }
}
void countSort(char *A[],int n, int posit)
{
    char *res[n];
    int tab[2]; // tab[0] to a, tab[1] to b
    for(int i=0;i<2;i++)
        tab[i]=0;
    for(int i=0;i<n;i++)
        tab[getCharByPosit(A[i],posit)]++;
    for(int i=1;i<n;i++)
        tab[i]=tab[i]+tab[i-1];
    for(int i=n-1;i>=0;i--)
    {
        res[tab[getCharByPosit(A[i],posit)]-1]=A[i];
        tab[getCharByPosit(A[i],posit)]--;

    }
    for(int i=0;i<n;i++)
        A[i]=res[i];
}
void radixSort(char *A[],int n)
{
    int m=getMax(A,n);
    for(int i=m-1;i>=0;i--)
        countSort(A,n,i);
}
void print(char *A[],int n)
{
    for(int i=0;i<n;i++)
        cout << A[i] << endl;
}
int main()
{
    char *A[5]={"abb","baa","aaaa","bbb","bbbbbb"};
    cout << A[2] <<endl;
    cout << getMax(A,5) << endl << endl;
    radixSort(A,5);
    print(A,5);


}
