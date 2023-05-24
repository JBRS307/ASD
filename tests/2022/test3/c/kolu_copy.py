from kolutesty import runtests

def swaps( disk, depends ): 
    n=len(disk)
    TO_DO1=[0 for _ in range(n)]
    TO_DO2=[0 for _ in range(n)]
    G=[[] for _ in range(n)]
    ROOTS1=[[],[]]
    ROOTS2=[[],[]]
    


    def DFS_Visit(Graph,TO_DO,ROOTS,vertex,case,flag):

        for j in range (len(Graph[vertex])):
            neighbour=Graph[vertex][j]
            TO_DO[neighbour]-=1
            
            if TO_DO[neighbour]==0:
                if disk[neighbour]==case:
                    DFS_Visit(Graph,TO_DO,ROOTS,neighbour,case,flag)
                else:
                    ROOTS[flag].append(neighbour)

    


    for i in range(n):
        leng=len(depends[i])
        TO_DO1[i]=leng
        TO_DO2[i]=leng
        if leng==0:
            if disk[i]=="A":
                ROOTS1[0].append(i)
                ROOTS2[0].append(i)
            else:
                ROOTS1[1].append(i)
                ROOTS2[1].append(i)
        else:
            for j in range(leng):
                G[depends[i][j]].append(i)


  

    sum1=-1
    while len( ROOTS1[0])!=0 or len( ROOTS1[1])!=0:
      
        if len( ROOTS1[0])!=0:
            sum1+=1
            for j in range(len(ROOTS1[0])):
                root=ROOTS1[0][j]
                DFS_Visit(G,TO_DO1,ROOTS1,root,"A",1)
            ROOTS1[0]=[]
          
        elif len(ROOTS1[1])!=0:
            sum1+=1
            for j in range(len(ROOTS1[1])):
                root=ROOTS1[1][j]
                DFS_Visit(G,TO_DO1,ROOTS1,root,"B",0)
            ROOTS1[1]=[]

    sum2=-1
    while len( ROOTS2[0])!=0 or len( ROOTS2[1])!=0:
        if len( ROOTS2[1])!=0:
            sum2+=1
            for j in range(len(ROOTS2[1])):
                root=ROOTS2[1][j]
                DFS_Visit(G,TO_DO2,ROOTS2,root,"B",0)
            ROOTS2[1]=[]
        elif len(ROOTS2[0])!=0:
            sum2+=1
            for j in range(len(ROOTS2[0])):
                root=ROOTS2[0][j]
                DFS_Visit(G,TO_DO2,ROOTS2,root,"A",1)
            ROOTS2[0]=[]

    sum=min(sum1,sum2)
    return sum 



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = False )

"""Tworzymy tablicę TO_DO która wyznacza nam ilość wierzchołków do zrobienia przed danym wierzchołkiem. Tworzymy też tablicę ROOTS 
dzieloną na dwa bloczki - z dyskietki A i B, są to niezależne wierzchołki (możemy je wykonać od razu). Wykonujemy while dopóki są
wierzchołki w ROOTS. Na każym wierzchołku z ROOTS wykonujemy DFS na grafie odwróconym który dla wszystkich neighborów odejmuje jedynkę od tablicy
TO_DO (bo ten program już zainstalowaliśmy). Sprawdzamy czy TO_DO od neighbora stało się 0. Jeśli tak, wykonujemy DFS_Visit od
tego neighbora czyt.instalujemy go. Jeśli TO_DO jest na 0 ale jest on na innej dystkietce dodajemy go do tablicy ROOT dla 
drugiej dyskietki. Algorytm trzeba odpalić 2 razy, raz zaczynając od dyskietki A, raz od B i bierzemy min. Za każdym razem kiedy
w while zmieniamy dyskietkę dodajemy 1 do sumy."""