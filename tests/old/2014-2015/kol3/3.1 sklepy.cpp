#include<iostream>
#include<climits>
using namespace std;
struct vertex
{
    bool shop;
    int *distances;
    int *edges;
    int edge;
    int d_store;
};
int dijkstra(vertex s,int v,int n,vertex *village,vertex e,int dest)
{
    int hlen = n,x,u,parent,left,right,dmin,pmin,sptr=0;
    int d[n],p[n],h[n],hp[n],S[n];
    bool QS[n]; // false w Q true w S
    for(int i = 0; i < n; i++)
    {
        d[i] = INT_MAX;
        p[i] = -1;
        QS[i] = false;
        h[i] = hp[i] = i;
    }

    d[v] = 0;                       // Koszt dojœcia v jest zerowy
    x = h[0]; h[0] = h[v]; h[v] = x; // odtwarzamy w³asnoœæ kopca
    hp[v] = 0; hp[0] = v;

    // Wyznaczamy œcie¿ki

    for(int i = 0; i < n; i++)
    {
        u = h[0];                     // Korzeñ kopca jest zawsze najmniejszy

        // Usuwamy korzeñ z kopca, odtwarzaj¹c w³asnoœæ kopca

        h[0] = h[--hlen];             // W korzeniu umieszczamy ostatni element
        hp[h[0]] = parent = 0;        // Zapamiêtujemy pozycjê elementu w kopcu
        while(true)                   // W pêtli idziemy w dó³ kopca, przywracaj¹c go
        {
              left  = parent + parent + 1; // Pozycja lewego potomka
              right = left + 1;           // Pozycja prawego potomka
              if(left >= hlen) break;     // Koñczymy, jeœli lewy potomek poza kopcem
              dmin = d[h[left]];          // Wyznaczamy mniejszego potomka
              pmin = left;
              if((right < hlen) && (dmin > d[h[right]]))
              {
                    dmin = d[h[right]];
                    pmin = right;
              }
              if(d[h[parent]] <= dmin) break; // Jeœli w³asnoœæ kopca zachowana, koñczymy
              x = h[parent]; h[parent] = h[pmin]; h[pmin] = x; // Przywracamy w³asnoœæ kopca
              hp[h[parent]] = parent; hp[h[pmin]] = pmin;      // na danym poziomie
              parent = pmin;              // i przechodzimy na poziom ni¿szy kopca
        }

        // Znaleziony wierzcho³ek przenosimy do S

        QS[u] = true; // true w S zbiorze, false w Q

        // Modyfikujemy odpowiednio wszystkich s¹siadów u, którzy s¹ w Q

        for(int i=0; i<village[u].edge; i++)
          if(!QS[village[u].edges[i]] && (d[village[u].edges[i]] > d[u] + village[u].distances[i]))
          {
                d[village[u].edges[i]] = d[u] + village[u].distances[i];
                p[village[u].edges[i]] = u;

            // Po zmianie d[v] odtwarzamy w³asnoœæ kopca, id¹c w górê

                for(int child = hp[village[u].edges[i]]; child; child = parent)
                {
                      parent = child / 2;
                      if(d[h[parent]] <= d[h[child]]) break;
                      x = h[parent]; h[parent] = h[child]; h[child] = x;
                      hp[h[parent]] = parent; hp[h[child]] = child;
                }
          }
          if(u==dest) break;
      }

    return d[dest];
}
void distanceToClosestStore(vertex *village, int n)
{
    int max=INT_MAX,tmp;
    for(int i=0;i<n;i++)
    {
        if(village[i].shop==true)
        {
            village[i].d_store=0;
            break;
        }
        else
        {
            for(int j=0;j<n;j++)
            {
                if(village[j].shop==false) break;
                else if(i==j) break;
                tmp=dijkstra(village[i],i,n,village,village[j],j);
                if(tmp<max) max=tmp;

            }
            village[i].d_store=max;
        }
        max=INT_MAX;
    }
}
int main()
{

}
