from zad7testy import runtests

def backtrack(G, visited_cities, n_visited, result, door):
    if n_visited[0]+1 == len(G) and (result[-1] in G[result[0]][1]):
        return True
    
    n_visited[0] += 1
    curr = result[-1]
    for ix in G[curr][door]:
        if not visited_cities[ix]:
            next_door = (curr in G[ix][0])
            result.append(ix)
            visited_cities[ix] = True
            if backtrack(G, visited_cities, n_visited, result, next_door):
                return True
            visited_cities[ix] = False
            result.pop(-1)
    
    n_visited[0] -= 1
    return False

def droga( G ):
    n = len(G)
    n_visited = [0]
    visited_cities = [False]*n
    start = min((len(G[i][0]), i) for i in range(n))[1]
    visited_cities[start] = True
    result = [start]
    if backtrack(G, visited_cities, n_visited, result, 0):
        return result
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )