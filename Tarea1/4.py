def missingNumbers(arr, brr):
        c = max(arr + brr) + 1
        list = [0 for _ in range(c)]
        for i in arr:
            list[i] = list[i]+1
        for i in brr:
            list[i] = list[i]-1
        solution=sorted([item for item in range(len(list)) if list[item] != 0])
        return solution
