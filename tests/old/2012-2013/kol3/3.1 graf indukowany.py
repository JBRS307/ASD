class Heap:
    def __init__(self, arr=None):
        self.arr = []
        if arr is not None:
            self.build(arr)
        self.size = 0

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return i * 2 + 1

    @staticmethod
    def right(i):
        return i * 2 + 2

    def insert(self, val):
        self.arr.append(val)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.arr[i][0] < self.arr[self.parent(i)][0]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)

    def build(self, arr):
        for el in arr:
            self.insert(el)

    def fix(self, i):
        l = self.left(i)
        r = self.right(i)
        m = i
        if l < self.size and self.arr[l][0] < self.arr[m][0]:
            m = l
        if r < self.size and self.arr[r][0] < self.arr[m][0]:
            m = r
        if m != i:
            self.arr[i], self.arr[m] = self.arr[m], self.arr[i]
            self.fix(m)

    def pop(self):
        if self.empty():
            raise IndexError("Heap is empty")
        root = self.arr[0]
        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]
        self.arr.pop()
        self.size -= 1
        self.fix(0)
        return root

    def empty(self):
        return self.size == 0


def induced_graph(G, k):
    H = Heap()
    n = len(G)
    vis = [False]*n
    for i in range(n):
        if len(G[i]) < k:
            H.insert((len(G[i]), i))
    while not H.empty():
        degree,u = H.pop()
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                for i in range(len(G[v])):
                    if G[v][i] == u:
                        G[v][i],G[v][-1] = G[v][-1],G[v][i]
                        G[v].pop()
                    if len(G[v]) < k:
                        H.insert((len(G[v]),v))
                    break
    cnt = 0
    for i in range(n):
        if vis[i]:
            cnt += 1
    return n-cnt

