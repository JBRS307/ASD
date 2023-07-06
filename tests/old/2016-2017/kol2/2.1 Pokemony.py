# class PQ:
#     def __init__(self, n):
#         self.T = [None] * n
#         self.size = 0
#
#     @staticmethod
#     def parent(i):
#         return (i - 1) // 2
#
#     def swap(self, a, b):
#         self.T[a].heap = b
#         self.T[b].heap = a
#         self.T[a], self.T[b] = self.T[b], self.T[a]
#
#     def heapify(self, i):
#         l = 2 * i + 1
#         r = 2 * i + 2
#         m = i
#         if l < self.size and self.T[l].wage < self.T[m].wage:
#             m = l
#         if r < self.size and self.T[r].wage < self.T[m].wage:
#             m = r
#         if m != i:
#             self.swap(m, i)
#             self.heapify(m)
#
#     def insert(self, x):
#         self.T[self.size] = x
#         self.size += 1
#         i = self.size - 1
#         while i > 0 and self.T[i].wage < self.T[self.parent(i)].wage:
#             self.swap(i, self.parent(i))
#             i = self.parent(i)
#
#     def extractmin(self):
#         minim = self.T[0]
#         self.swap(0, self.size - 1)
#         self.T.pop()
#         self.size -= 1
#         self.heapify(0)
#         return minim.ind
#
#     def decreasekey(self, i, key):
#         self.T[i].wage = key
#         while i > 0 and self.T[i].wage < self.T[self.parent(i)].wage:
#             self.swap(i, self.parent(i))
#             i = self.parent(i)


class Pokemon:
    def __init__(self,ind):
        self.ind = ind
        self.preys = []
        self.pred = []
        self.proc = False


# def releasethem(T, n):
#     P = [Pokemon(i) for i in range(n)]
#     for pred, prey in T:
#         P[pred].preys += 1
#         P[pred].wage += 1
#         P[prey].predators.append(pred)
#     Q = PQ(n)
#     A = []
#     for i in range(n):
#         Q.insert(P[i])
#     while Q.size > 0:
#         pok = Q.extractmin()
#         if P[pok].preys == 1:
#             return None
#         for pred in P[pok].predators:
#             if not P[pred].proc and not P[pred].preys == 2:
#                 Q.decreasekey(P[pred].heap, P[pred].wage-1)
#         P[pok].proc = True
#         A.append(pok)
#     return A

def releasethem(T,n):
    P = [Pokemon(i) for i in range(n)]
    for a,b in T:
        P[a].preys.append(b)
        P[b].pred.append(a)
    A = []
    for i in range(n):
        if not P[i].preys:
            P[i].proc = True
            A.append(i)
    def search(ind):
        cnt = 0
        for prey in P[ind].preys:
            if P[prey].proc:
                cnt += 1
            if cnt == 2:
                break
        if cnt != 2:
            return
        P[ind].proc = True
        A.append(ind)
        for pred in P[ind].pred:
            if not P[pred].proc:
                search(pred)

    for i in range(n):
        if not P[i].proc:
            search(i)
    if len(A) != n:
        return None
    else:
        return A


T = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (5, 4), (5, 6), (0, 5), (5, 7), (7, 0), (7, 8)]
print(releasethem(T, 9))
