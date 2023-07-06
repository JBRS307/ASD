#include<iostream>
#include<math.h>
using namespace std;
struct point
{
    double x,y;
};
struct pointF
{
    double x,y,dest;
};
void convert(point *A,pointF *source, int n)
{
    int temp;
    for(int i=0;i<n;i++)
    {
        source[i].x=A[i].x;
        source[i].y=A[i].y;
        source[i].dest=sqrt(A[i].x*A[i].x+A[i].y*A[i].y);
    }
}
int left(int i){
    return 2*i+1;
}
int right(int i){
    return 2*i+2;
}
 int parent(int i){
    return (i-1)/2;
}
void heapify(pointF *A,int n, int i)
{
    int max=i;
    if(left(i)<n and A[left(i)].dest>A[max].dest)
        max=left(i);
    if(right(i)<n and A[right(i)].dest>A[max].dest)
        max=right(i);
    if(i!=max)
    {
        swap(A[i],A[max]);
        heapify(A,n,max);
    }
}
void build_heap(pointF *A, int n)
{
    for(int j=parent(n-1);j>=0;j--)
        heapify(A,n,j);
}
void heapsort(point *A,int n)
{
    pointF sor[n];
    convert(A,sor,n);
    build_heap(sor,n);
    for(int j=n-1;j>=1;j--)
    {
        swap(sor[j],sor[0]);
        heapify(sor,j,0);
    }
    for(int k=0;k<n;k++)
    {
        A[k].x=sor[k].x;
        A[k].y=sor[k].y;
    }
}
int main()
{
    int n,x,y;
    point *A;
    cin >> n;
    A=new point [n];
    for(int i=0;i<n;i++){
        cin >> x >> y;
        A[i].x=x;
        A[i].y=y;

    }
    heapsort(A,n);
    delete [] A;
}
