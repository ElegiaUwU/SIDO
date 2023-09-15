def fibonacciModified(t1, t2, n):
    i = int(3)
    t = 0
    lista = [t1, t2]
    while i < n+2:
        t = lista[0] + lista[1]*lista[1]
        lista[0] = lista[1]
        lista[1] = t
        i = i+1
    return lista[0]
