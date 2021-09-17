animals = {
    'a': ['aardvark'],
    'b': ['baboon'],
    'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
#
#
# def biggest(L):
#     m = max(map(len, L.values()))
#     return m
#
# for key, value in animals.items():
#     if len(value) == biggest(animals):
#         print (key)
#

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    m = max(map(len, aDict.values()))
    print(m)

    for key, value in aDict.items():
        if len(value) == max(map(len, aDict.values())):
            return (key)

biggest(animals)
