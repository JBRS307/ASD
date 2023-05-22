from zad7testy import runtests
import sys
# Wojciech Wiśniewski
# Algorym używa algorytmu z nawrotami. Od pierwszego punktu próbuje odwiedzić
# wszystkie połączone punkty, i rekurencyjnie sprawdza czy z dalej da się stworzyć
# akceptowalną ścieżkę. Jeśli nie, wybiera inny punkt.
# Pesymistyczna złożoność czasowa to O(n!), optymistyczna to O(n)
# Złożoność pamięciowa to O(n)
sys.setrecursionlimit(1 << 20)

contains = list.__contains__


def backtrack(G: "list[tuple[list[int]]]", visited_cities: "list[bool]", n_visited: "list[int]", result: "list[int]", door: int) -> bool:
    if n_visited + 1 == len(G) and contains(G[result[0]][1], result[-1]):
        return True  # All cities were visited
    n_visited += 1
    current = result[-1]
    for ix in G[current][door]:
        if visited_cities[ix]:
            continue
        next_door = contains(G[ix][0], current)
        result.append(ix)
        visited_cities[ix] = True
        if backtrack(G, visited_cities, n_visited, result, next_door):
            return True
        visited_cities[ix] = False
        result.pop(-1)

    n_visited -= 1
    return False


def droga(G: "list[tuple[list[int]]]") -> "list[int]":
    n = len(G)
    visited_cities = [False for _ in range(n)]
    starting = min((len(G[i][0]), i) for i in range(n))[1]
    visited_cities[starting] = True
    result = [starting]
    n_visited = 0
    if backtrack(G, visited_cities, n_visited, result, 0):
        return result
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)