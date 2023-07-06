#include<iostream>
using namespace std;
struct slistEl
{
    slistEl *next;
    int v;
};

void GrafIndukowany(slistEl **G, int n, int k, int *X, int R)
{
    for(int i=0;i<R;i++)
    {
        int tmp=X[i];
        slistEl *p=G[tmp];
        slistEl *r;
        while(p)
        {
            r=p;
           // cout << r->v;
            slistEl *d=G[r->v];
            slistEl *prev=NULL;
            while(d->v!=X[i])
            {
                prev=d;
                d=d->next;
            }
            if(d->next==NULL and prev!=NULL)
            {
                prev->next=NULL;
                delete d;

            }
            else if(prev==NULL and d->next!=NULL)
            {
                prev=d;
                d=d->next;
                G[r->v]=d;
                delete prev;
            }
            else if(prev==NULL and d->next==NULL)
            {
                G[r->v]=NULL;
                delete d;
            }
            else
            {
                prev->next=d->next;
                delete d;
            }

            p=p->next;
            delete r;
        }
        p=new slistEl;
        p->v=-1;
        p->next=NULL;
        G[tmp]=p;
    }



    int licznik=0,tmp;

    for(int i=0;i<n;i++)
    {
        tmp=0;
        slistEl *p=G[i];
        while(p)
        {
            if(p->v==-1) break;
            p=p->next;
            tmp++;
            if(tmp==k) licznik++;
        }
    }
    cout << endl << licznik;

}


int main()
{
    slistEl **G,*p;

    int n,m,v1,v2;
    cin >> n >> m;
    G= new slistEl *[n];
    int U[2]={4,6}; //5 i 7 wierzcholek
    for(int i=0; i<n; i++)
    {
        G[i]=NULL;

    }
    for(int i = 0; i < m; i++)
    {
        cin >> v1 >> v2;    // Wierzcho³ek startowy i koñcowy krawêdzi
        p = new slistEl;    // Tworzymy nowy element
        p->v = v2;          // Numerujemy go jako v2
        p->next = G[v1];    // Dodajemy go na pocz¹tek listy A[v1]
        G[v1] = p;
        p = new slistEl;    // nieskerowany
        p->v=v1;
        p->next=G[v2];
        G[v2]=p;
    }
    cout << endl << endl;
    for(int i=0;i<n;i++)
    {
        slistEl *p=G[i];
        while(p)
        {
            cout << p->v ;
            p=p->next;

        }
        cout << endl;
    }
    GrafIndukowany(G,n,3,U,2);
}
