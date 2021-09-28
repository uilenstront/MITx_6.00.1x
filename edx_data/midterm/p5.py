target = 1

aDict = {
    1:9,
    2:2,
    3:3,
    7:5,
    8:3
}


def keysWithValue(aDict, target):
    """
    aDict: a dictionary
    target: an integer
    """
    five = []
    for k in aDict:
        if aDict[k] == target:
            five.append(k)
    return sorted(five)



