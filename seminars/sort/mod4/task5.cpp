#include <iostream>
#include <string>

using namespace std;

bool check_anagrams(string a, string b, int k){
    if(a.length() != b.length()) return false;
    int r = 'a';
    int letters[k];

    for(int c : a) letters[c-r] = 0;
    for(int c : a) letters[c-r]++;
    for(int c : b) letters[c-r]--;
    for(int c : a){
        if(letters[c-r] != 0) return false;
    }
    return true;
}

//Sprawdź czy 2 słowa są anagramami w czasie O(N)
//Zadeklaruj (ale nie inicjalizuj) tablicę długości K i przejdź po indeksach, które odpowiadają literom
int main(){
    string a, b;
    cin >> a >> b;
    int k = 26; //ilość liter w alfabecie łacińskim

    cout << (check_anagrams(a, b, k) ? "TRUE\n" : "FALSE\n");

    return 0;
}