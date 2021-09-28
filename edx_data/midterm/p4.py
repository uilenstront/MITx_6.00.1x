def getSubLists(L, n):
    lcopy = L[:]
    r = []
    for i in range(0, len(L)-n+1):
        r.append(lcopy[i:i+n:1])
        del(L[0])
    return r

print(getSubLists(L, n))