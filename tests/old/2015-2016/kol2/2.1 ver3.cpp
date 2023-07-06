#include<iostream>
#include<cstdlib>
#define INF 2147483647
using namespace std;
const int max_lvl=5;
struct SLNode
{
    SLNode **next;
    int value;
    int lvl;
};
struct SkipList
{
    SLNode *first;
    SLNode *last;
};
int level()
{
    int lvl=1;
    int x=rand()%100;
    while(x<50)
    {
        lvl++;
        x=rand()%100;

    }
    return min(lvl,max_lvl);
}
void add(int val, SkipList a){
	int lvl = level();
	SLNode *temp = new SLNode;
	temp->next = new SLNode*[lvl];
	temp->value = val;
	temp->lvl=lvl;
	lvl--;
	for (int i = max_lvl-1; i >= 0; i--)
	{
		while (a.first->next[i]->value < val)
			a.first = a.first->next[i];
		if (i <= lvl)
		{
			temp->next[i] = a.first->next[i];
			a.first->next[i] = temp;
		}

	}
}
SkipList merge(SkipList a, SkipList b)
{
    SkipList S;
	SLNode *first = new SLNode;
	first->value = -INF -1;
	first->next = new SLNode*[max_lvl];
	first->lvl=max_lvl;
	SLNode *last = new SLNode;
	last->value = INF;
	last->next = new SLNode*[max_lvl];
	last->lvl=max_lvl;
	for (int i = 0; i < max_lvl; i++){
		first->next[i] = last;
		last->next[i] = NULL;
	}
	S.first = first;
	S.last = last;
	SLNode *tmp=S.first;

    while(a.first->next[0]->value<INF and b.first->next[0]->value<INF)
    {

        int valueA=a.first->next[0]->value;
        int valueB=b.first->next[0]->value;

        if(valueA<valueB)
        {
            for (int i = max_lvl-1; i >= 0; i--)
            {
                if (i <= ((a.first->next[0]->lvl)-1))
                {
                    a.first->next[i]->next[i] = S.last;
                    tmp->next[i] = a.first->next[i];
                    tmp=tmp->next[i];
                    a.first=a.first->next[i];

                }
                SLNode *temp=S.first;
                while (temp != NULL)
                {
                    cout << temp->value;
                    temp = temp->next[i];
                    cout << "   ";
                }
                cout << endl;

            }
        }
        else
        {
            for (int i = max_lvl-1; i >= 0; i--)
            {
                if (i <= ((b.first->next[0]->lvl)-1))
                {
                    tmp->next[i] = b.first->next[i];
                    b.first->next[i]->next[i] = S.last;
                    tmp->next[i]=tmp->next[i];
                    b.first=b.first->next[i];

                }

            }
        }
    }
   /* if(a.first->next[0]->value==INF)
    {
        while(b.first->next[0]->value!=INF)
        {
            for (int i = max_lvl-1; i >= 0; i--)
            {
                if (i <= b.first->lvl-1)
                {
                    tmp->next[i] = b.first->next[i];
                    b.first->next[i] = S.last;
                    tmp=tmp->next[i];
                    b.first=b.first->next[i];
                }

            }
        }

    }
    else
    {
           while(a.first->next[0]->value!=INF)
        {
            for (int i = max_lvl-1; i >= 0; i--)
            {
                if (i <= a.first->lvl-1)
                {
                    tmp->next[i] = a.first->next[i];
                    a.first->next[i] = S.last;
                    tmp=tmp->next[i];
                    a.first=b.first->next[i];
                }

            }
        }

    }
*/
    return S;
}
int main()
{
    SkipList a,b;
	SLNode *first = new SLNode;
	first->value = -INF -1;
	first->next = new SLNode*[max_lvl];
	first->lvl=max_lvl;
	SLNode *last = new SLNode;
	last->value = INF;
	last->next = new SLNode*[max_lvl];
	last->lvl=max_lvl;
	for (int i = 0; i < max_lvl; i++){
		first->next[i] = last;
		last->next[i] = NULL;
	}
	SLNode *first2 = new SLNode;
	first2->value = -INF -1;
	first2->next = new SLNode*[max_lvl];
	first2->lvl=max_lvl;
	SLNode *last2 = new SLNode;
	last2->value = INF;
	last2->next = new SLNode*[max_lvl];
	last2->lvl=max_lvl;
	for (int i = 0; i < max_lvl; i++){
		first2->next[i] = last2;
		last2->next[i] = NULL;
	}
	a.first = first;
	a.last = last;
	b.first = first2;
	b.last = last2;
	add(2,a);
	add(4,a);
	add(8,a);
	add(3,b);
	add(10,b);
	add(12,b);
    /*for (int i = max_lvl-1; i >= 0; i--) {
		SLNode *tmp = a.first;

		while (tmp != NULL)
		{
			cout << tmp->value;
			tmp = tmp->next[i];
			cout << "   ";
		}
		cout << endl;
	}*/
    merge(a,b);

}
