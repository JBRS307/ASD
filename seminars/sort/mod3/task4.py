#Mamy tablicę liczb rzeczywistych. tablica jest k-chaotyczna,
#To znaczy, że każda liczba jest co najwyżej k miejsc od właściwej pozycji w posortowanej tablicy

#dla k O(1) wystarczy insertion sort, wtedy jest O(n)
#k=O(log(n)) powinno być O(nlog(log(n)))

#Robimy kopiec k+1-elementowy począwszy od pierwszego elementu, zabieramy z niego minimum i dodajemy
#następny element i tak w kółko 