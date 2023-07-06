#include <iostream>

using namespace std;

// Definicja obiektu kolejki priorytetowej
//----------------------------------------
struct Edge
{
  int v1,v2,weight;               // Wierzcho³ki krawêdzi, waga krawêdzi
};

class Queue
{
  private:
    Edge * Heap;
    int hpos;
  public:
    Queue(int n);
    ~Queue();
    Edge front();
    void push(Edge e);
    void pop();
};

// Definicja obiektu minimalnego drzewa rozpinaj¹cego
//---------------------------------------------------
struct TNode
{
  TNode * next;
  int v,weight;
};

class MSTree
{
  private:
    TNode ** A;                   // Tablica list s¹siedztwa
    int Alen;                     // Liczba komórek w tablicy
    int weight;                   // Waga ca³ego drzewa
  public:
    MSTree(int n);
    ~MSTree();
    void addEdge(Edge e);
    void creatGraph(int **G,int n);
    TNode * getAList(int n);
    void print();
};

// Definicje metod obiektu Queue
//------------------------------

// Konstruktor - tworzy n elementow¹ tablicê heap na kopiec
//---------------------------------------------------------
Queue::Queue(int n)
{
  Heap = new Edge [n];            // Tworzymy tablicê
  hpos = 0;                       // Pozycja w kopcu
}

// Destruktor - usuwa kopiec z pamiêci
//------------------------------------
Queue::~Queue()
{
  delete [] Heap;
}

// Zwraca krawêdŸ z pocz¹tku kopca
//--------------------------------
Edge Queue::front()
{
  return Heap[0];
}

// Umieszcza w kopcu now¹ krawêdŸ i odtwarza strukturê kopca
//----------------------------------------------------------
void Queue::push(Edge e)
{
  int i,j;

  i = hpos++;                     // i ustawiamy na koniec kopca
  j = (i - 1) >> 1;               // Obliczamy pozycjê rodzica (fajniejsze j/=2)

  // Szukamy miejsca w kopcu dla e

  while(i && (Heap[j].weight > e.weight))
  {
    Heap[i] = Heap[j];
    i = j;
    j = (i - 1) >> 1;
  }

  Heap[i] = e;                    // KrawêdŸ e wstawiamy do kopca
}

// Usuwa korzeñ z kopca i odtwarza jego strukturê
//-----------------------------------------------
void Queue::pop()
{
  int i,j;
  Edge e;

  if(hpos)
  {
    e = Heap[--hpos];

    i = 0;
    j = 1;

    while(j < hpos)
    {
      if((j + 1 < hpos) && (Heap[j + 1].weight < Heap[j].weight)) j++;
      if(e.weight <= Heap[j].weight) break;
      Heap[i] = Heap[j];
      i = j;
      j = (j << 1) + 1;
    }

    Heap[i] = e;
  }
}

// Definicje metod obiektu MSTree
//-------------------------------

// Konstruktor - tworzy tablicê pustych list s¹siedztwa
//-----------------------------------------------------
MSTree::MSTree(int n)
{
  int i;

  A = new TNode * [n];            // Tworzymy tablicê dynamiczn¹
  for(i = 0; i < n; i++) A[i] = NULL; // i wype³niamy j¹ pustymi listami
  Alen = n - 1;                   // Zapamiêtujemy d³ugoœæ tablicy
  weight = 0;                     // Zerujemy wagê drzewa
}

// Destruktor - usuwa listy oraz tablicê s¹siedztwa
//-------------------------------------------------
MSTree::~MSTree()
{
  int i;
  TNode *p,*r;

  for(i = 0; i <= Alen; i++)
  {
    p = A[i];
    while(p)
    {
      r = p;                      // Zapamiêtujemy wskazanie
      p = p->next;                // Przesuwamy siê do nastêpnego elementu listy
      delete r;                   // Usuwamy element
    }
  }

  delete [] A;                    // Usuwamy tablicê list s¹siedztwa
}

// Dodaje krawêdŸ do drzewa
//-------------------------
void MSTree::addEdge(Edge e)
{
  TNode *p;

  weight += e.weight;             // Do wagi drzewa dodajemy wagê krawêdzi
  p = new TNode;                  // Tworzymy nowy wêze³
  p->v = e.v2;                    // Wierzcho³ek koñcowy
  p->weight = e.weight;           // Waga krawêdzi
  p->next = A[e.v1];              // Dodajemy p do listy wierzcho³ka v1
  A[e.v1] = p;

  p = new TNode;                  // To samo dla krawêdzi odwrotnej
  p->v = e.v1;                    // Wierzcho³ek koñcowy
  p->weight = e.weight;           // Waga krawêdzi
  p->next = A[e.v2];              // Dodajemy p do listy wierzcho³ka v2
  A[e.v2] = p;
}

void MSTree::creatGraph(int **G,int n)
{
    Edge e;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
        {
            if(G[i][j]!=-1)
            {
                e.v1=i;
                e.v2=j;
                e.weight=G[i][j];
                addEdge(e);
            }
        }
}
// Zwraca wskaŸnik pocz¹tku listy s¹siadów wierzcho³ka
//----------------------------------------------------
TNode * MSTree::getAList(int n)
{
  return A[n];
}

// Wyœwietla zawartoœæ drzewa oraz jego wagê
//------------------------------------------
void MSTree::print()
{
  int i;
  TNode *p;

  cout << endl;
  for(i = 0; i <= Alen; i++)
  {
    cout << "Vertex " << i << " - ";
    for(p = A[i]; p; p = p->next) cout << p->v << ":" << p->weight << " ";
    cout << endl;
  }
  cout << endl << endl << "Minimal Spanning Tree Weight = " << weight << endl << endl;
}

int main()
{
  int n,m,x,y,w;                        // Liczba wierzcho³ków i krawêdzi
  Edge e;
  TNode * p;
  int i,v;

  cin >> n >> m;                  // Czytamy liczbê wierzcho³ków i krawêdzi

  Queue Q(m);                     // Kolejka priorytetowa oparta na kopcu
  MSTree T(n);                    // Minimalne drzewo rozpinaj¹ce
  MSTree G(n);
  int **macierz ;                   // Graf
  bool * visited = new bool [n];
  macierz= new int *[n];
  for(i = 0; i < n; i++)
  {
      visited[i] = false;
      macierz[i]= new int [n];
  }
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
        macierz[i][j]=-1;

  for(i = 0; i < m; i++)
  {
    cin >> x >> y >> w; // Odczytujemy kolejne krawêdzie grafu
    macierz[x][y]=w;               // i umieszczamy je w G
  }
  G.creatGraph(macierz,n);
  // Tworzymy minimalne drzewo rozpinaj¹ce

  v = 0;                          // Wierzcho³ek startowy
  visited[v] = true;              // Oznaczamy go jako odwiedzonego

  for(i = 1; i < n; i++)          // Do drzewa dodamy n - 1 krawêdzi grafu
  {
    for(p = G.getAList(v); p; p = p->next) // Przegl¹damy listê s¹siadów
      if(!visited[p->v])          // Jeœli s¹siad jest nieodwiedzony,
      {
        e.v1 = v;                 // to tworzymy krawêdŸ
        e.v2 = p->v;
        e.weight = p->weight;
        Q.push(e);                // Dodajemy j¹ do kolejki priorytetowej
      }

    do
    {
      e = Q.front();              // Pobieramy krawêdŸ z kolejki
      Q.pop();
    } while(visited[e.v2]);       // KrawêdŸ prowadzi poza drzewo?

    T.addEdge(e);                 // Dodajemy krawêdŸ do drzewa rozpinaj¹cego
    visited[e.v2] = true;         // Oznaczamy drugi wierzcho³ek jako odwiedzony
    v = e.v2;
  }

  // Wyœwietlamy wyniki

  T.print();

  delete [] visited;

  return 0;
}
