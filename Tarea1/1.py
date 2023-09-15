def saveThePrisoner(n, m, s):
    resultado=(m+s-1)%n
    if(resultado==0):
        resultado=n
    return(resultado)
