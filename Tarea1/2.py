def theLoveLetterMystery(s):
    n=math.floor(len(s)/2)
    m=len(s)-1
    pasos=0
    for x in range(n):
        a=abs(ord(s[x])-ord(s[m-x]))
        pasos=pasos+a
    return pasos
