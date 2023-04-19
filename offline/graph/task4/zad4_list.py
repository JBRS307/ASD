from zad4testy import runtests


def count_path(parent, s, t):
    res = 0
    curr = t
    while curr != s:
        curr = parent[curr]
        res += 1
    return res

def BFS(G, s, t):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    q = []
    q.append(s)

    visited[s] = True
    while len(q) != 0:
        v = q.pop(0)
        for v_next in G[v]:
            if not visited[v_next]:
                parent[v_next] = v
                if v_next == t: return parent
                visited[v_next] = True
                q.append(v_next)
    return None

def longer( G, s, t ):
    parent = BFS(G, s, t)
    if parent is None: return None
    min_path = count_path(parent, s, t)
    
    curr = t
    while curr != s:
        G[parent[curr]].remove(curr)
        
        new_parent = BFS(G, s, t)
        if new_parent is None: return (parent[curr], curr)
        if count_path(new_parent, s, t) > min_path: return (parent[curr], curr)

        G[parent[curr]].append(curr)
        curr = parent[curr]
    
    return None
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )