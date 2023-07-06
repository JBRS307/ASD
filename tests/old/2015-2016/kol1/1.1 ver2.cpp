#include<iostream>
#include<math.h>
#define MAX_INT 2147483647
using namespace std;
void sumSort(int A[], int B[],int n)
{
    int m=sqrt(n),x=0,sum=0;
    int tab[m];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
            sum+=A[i+j];

        tab[x++]=sum;
        sum=0;
        i+=(m-1);
    }

    int min=tab[0],num=0,posit=0;
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(min>tab[j]){
                min=tab[j];
                num=j;
            }
        }
        tab[num]=MAX_INT;
        for(int k=num*m;k<(m*num)+m;k++)
            B[posit++]=A[k];

        min=tab[0];
        num=0;
    }



}

int main()
{
    int A[16]={12555,16,22,1,66,112,151,661,333,11,0,900,4,100,200,500};
    int B[16];

    sumSort(A,B,16);
    for(int i=0;i<16;i++) cout << B[i] << " ";
}
