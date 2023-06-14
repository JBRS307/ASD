# Trzeba znaleźć w drzewie maksymalny zbiór wierzchołków niepołączonych

class Employee:
    def __init__(self, fun): # fun to wartość węzła - współcznynnik zabawy
        self.emp = [] # lista dzieci węzła
        self.fun = fun
        self.f = -1
        self.g = -1

# f(v) - wartość najlepszej imprezy w poddrzewie zakorzenionym w v
# g(v) - wartość najlepszej imprezy w poddrzewie zakorzenionym w v, ale v na nią nie idzie

def f(v):
    if v.f >= 0:
        return v.f
    
    x = v.fun
    for u in v.emp:
        x += g(u)
    y = g(v)
    v.f = max(x, y)
    return v.f

def g(v):
    if v.g >= 0:
        return v.g
    
    x = 0
    for u in v.emp:
        x += f(u)
    v.g = x
    return v.g