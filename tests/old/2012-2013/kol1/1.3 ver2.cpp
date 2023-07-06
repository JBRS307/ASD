#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
struct charS
{
    char a;
    bool visited;
};
void rewrite(char *A, int n, charS *B)
{
    for(int i=0;i<n;i++)
    {
        B[i].a=A[i];
        B[i].visited=false;
    }
}
bool possible(char *x, char *y, char *z)
{
    int k=0;
    int Lx=strlen(x), Ly=strlen(y), Lz=strlen(z);
    charS X[Lx], Y[Ly], Z[Lx];
    rewrite(x,Lx,X);rewrite(y,Ly,Y);rewrite(z,Lz,Z);

    for(int i=0;i<Lx;i++)
        for(int j=0;j<Ly;j++)
        {
            if(X[i].a==Y[j].a and X[i].visited==false and Y[j].visited==false)
            {
                k++;
                X[i].visited=true;
                Y[j].visited=true;
                if(k==Lx) return true;
                break;
            }

        }
    for(int i=0;i<Lx;i++)
        for(int j=0;j<Lz;j++)
        {
            if(X[i].a==Z[j].a and X[i].visited==false and Z[j].visited==false)
            {
                k++;
                X[i].visited=true;
                Z[j].visited=true;
                if(k==Lx) return true;
                break;
            }

        }
    return false;
}
int main()
{
    char *x="waxlaw";
    char *y="bdaow";
    char *z="lxxa";
    if(possible(x,y,z)) cout << "tak";
    else cout << "nie";
}
