def decentNumber(n):
    if n in (1,2,4,7): 
        print(-1) 
        return
    tres = (0, 10, 5)[n%3]
    print('5'*(n-tres)+'3'*tres)
