from zad2testy import runtests
from queue import PriorityQueue


def robot( L, A, B ):
    dp = [[[[-1]*3 for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]
    possible_moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    seconds = (60, 40, 30)
    q = PriorityQueue()
    q.put((0, A[0], A[1], 0, 0))

    while not q.empty():
        time, x, y, direction, speed = q.get()
        if (x, y) == B:
            return time
        if dp[y][x][direction][speed] != -1 or L[y][x] == 'X':
            continue
        dp[y][x][direction][speed] = time
        q.put((time+45, x, y, (direction+1)%4, 0))
        q.put((time+45, x, y, (direction+3)%4, 0))
        x += possible_moves[direction][0]
        y += possible_moves[direction][1]
        q.put((time+seconds[speed], x, y, direction, min(speed+1, 2)))

    return None
    
runtests( robot )


