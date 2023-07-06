"""2. struct field {
int value;
int long j;
int short j;
};
Z każdego pola można skakać tylko o ilość pól zapisaną w long j lub short j. Napisać program
który zwróci maksymalną wartość jaką możemy osiągnąć poprzez przejście z pola 0 do n-1.
Można założyć że z każdego pola da się dojść do pola n-1."""

class Node:
    def __init__(self,val,long,short):
        self.val = val
        self.long = long
        self.short = short

def check(T):
    n = len(T)
    F = [-1]*n
    F[0] = T[0]
    for i in range(0,n-1):
        if i + T[i].long < n:
            F[i+T[i].long] = max(F[i + T[i].long],F[i] + T[i + T[i].long].val)
        if i + T[i].short < n:
         F[i + T[i].short] = max(F[i + T[i].short),F[i] + T[i+T[i].short].val)
    return F[n-1]

