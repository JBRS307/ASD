// by Jan "Regzand" Golda

#include <stdio.h>
#include <algorithm>

using namespace std;

struct Tree{
    // ojciec
    Tree *parent;

    // lewy potomek
    Tree *left;
    int w_left;

    // prawy potomek
    Tree *right;
    int w_right;

    // najdluzsza sciezka wychodzaca z poddrzewie
    int longestPathOut;

    // najdluzsza sciezka w calosci zawarta w poddrzewie
    int longestPathIn;
};

void updatePathsInTree(Tree *T){
    // przypadek braku potomka
    if(T == NULL) return;

    // wywolanie rekurencyjne
    updatePathsInTree(T->left);
    updatePathsInTree(T->right);

    // T jest lisciem
    if(T->left == NULL && T->right == NULL){

        // lisc ma zawsze dlugosc najdluzszej sciezki 0
        T->longestPathOut = 0;
        // lisc ma zawsze dlugosc najdluzszej sciezki 0
        T->longestPathIn = 0;

    // T ma tylko lewego potomka
    }else if(T->right == NULL){

        // najdluzsza sciezka wychodzaca jest rowna sciezce wychodzacej z potomka plus waga krawedzi
        T->longestPathOut = T->left->longestPathOut + T->w_left;
        // najdluzsza sciezka wewnetrzna jest albo sciezka wewnetrzna w poddrzewie albo sciezka wychodzaca
        T->longestPathIn = max(T->left->longestPathIn, T->longestPathOut);

    // T ma tylko prawego potomka
    }else if(T->left == NULL){

        // najdluzsza sciezka wychodzaca jest rowna sciezce wychodzacej z potomka plus waga krawedzi
        T->longestPathOut = T->right->longestPathOut + T->w_right;
        // najdluzsza sciezka wewnetrzna jest albo sciezka wewnetrzna w poddrzewie albo sciezka wychodzaca
        T->longestPathIn = max(T->right->longestPathIn, T->longestPathOut);

    // T ma zarowno prawego jak i lewego potomka
    }else{

        // najdluzsza sciezka wychodzaca jest jedna ze sciezek wychodzacych w potomkow plus wagi odpowiednich krawedzi
        T->longestPathOut = max(T->left->longestPathOut + T->w_left, T->right->longestPathOut + T->w_right);
        // najdluzsza sciezka wewnetrzna jest jedna ze sciezek wewnetrznych u potomkow lub jest sciezka wychodzaca z jednego poddrzewa i wchodzaca do drugiego
        T->longestPathIn = max(T->left->longestPathIn, T->right->longestPathIn);
        T->longestPathIn = max(T->longestPathIn, T->left->longestPathOut + T->w_left + T->w_right + T->right->longestPathOut);

    }

}

int longestPathInTree(Tree *T){

    // dokonanie obliczen
    updatePathsInTree(T);

    // zwrocenie wyniku
    return max(T->longestPathIn, T->longestPathOut);
}

int main(){

    // ilosc wierzcholkow
    int N;
    scanf("%d", &N);

    // wierzcholki
    Tree nodes[N];

    // wczytanie wierzcholkow
    for(int i = 0; i<N; i++){
        int pId, lId, lW, rId, rW;
        scanf("%d %d %d %d %d", &pId, &lId, &lW, &rId, &rW);

        nodes[i].parent = ( pId == -1 ? NULL : &nodes[pId] );

        nodes[i].left = ( lId == -1 ? NULL : &nodes[lId] );
        nodes[i].w_left = lW;

        nodes[i].right = ( rId == -1 ? NULL : &nodes[rId] );
        nodes[i].w_right = rW;

        nodes[i].longestPathOut = 0;
        nodes[i].longestPathIn = 0;
    }

    // wypisanie wyniku
    printf("Najdluzsza sciezka: %d\n", longestPathInTree(&nodes[0]));

    return 0;
}
