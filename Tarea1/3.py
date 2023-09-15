def closestNumbers(arr):
    ar = sorted(arr)
    i = int(0)
    dif = []
    while i < len(ar)-1:
        dif.append(ar[i+1]-ar[i])
        i = i + 1
    minimo = min(dif)
    j = int(0)
    final = []
    while j < len(ar)-1:
        if ar[j+1]-ar[j] == minimo:
            final.append(ar[j])
            final.append(ar[j+1])
        j = j + 1    
    return final
