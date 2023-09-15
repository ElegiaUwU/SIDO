def superDigit(n, k):
    a=sum(int(x) for x in n)
    a=(a*k-1)%9
    return a +1
