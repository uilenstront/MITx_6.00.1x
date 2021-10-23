def c_to_f(c):
    # 3 operations:
    # 1 multiplication, 1 division, 1 addition
    return c * 9.0 / 5 + 32



# this one does 1 + 3x operations:
def mysum(x):
    # operation 1 is an assignment:
    total = 0
    # operation 2 is to get i from the range
    for i in range(x + 1):
        # operations 3 and 4 are the addition and the assignment - += are 2 operations
        total += 1
    return total # <- note in course: this counts for 1 as well which would make it 1 + 4x




def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

'''
2 * n + 1, want:
hele loop door ,dus dat is n keer
n

per loop doe je 1x "for e in L" , dus 1xn
1 * n

per loop doe je 1x "if e == x" dus nog 1xn
2 * n

return statement wordt altijd 1x uitgevoerd (de return False)
2 * n + 1
'''

#### PROGRAM 1

def program1(x):
    total = 0                   # best_case: 1
    for i in range(1000):       # best_case: 1000x for i in range
        total += i              # best_case: 1000x for +, and 1000x for =

    while x > 0:                # best_case: x is less than or equal to zero, so just the 1
        x -= 1                  # best_case: not done
        total += x              # best_case: not done

    return total                # best_case: 1
                                # total of 1 + 1000 + 1000 + 1000 + 1 + 1 = 3003 times


def program1(x):
    total = 0                   # worst_case: 1
    for i in range(1000):       # worst_case: 1000x for i in range
        total += i              # worst_case: 1000x for +, and 1000x for =

    while x > 0:                # worst_case: x is way groter dan 0, dus dit wordt n keer uitgevoerd      : 1 * n
                                # worst_case: als x 0 is wordt deze ook nog 1 keer uitgevoerd               1
        x -= 1                  # de - wordt n keer uitgevoerd, de = wordt n keer uitgevoerd:             : 2 * n
        total += x              # de + wordt n keer uitgevoerd, de = wordt n keer uitgevoerd:             : 2 * n

    return total                # worst_case: 1
                                # total of 1 + 1000 + 1000 + 1000 + ( 5 * n) + 1 + 1 = 5n + 3003




#### PROGRAM 2

def program2(x):
    total = 0                   # bc: 1                 wc: 1
    for i in range(1000):       # bc: 1000              wc: 1000
        total = i               # bc: 1000              wc: 1000

    while x > 0:                # bc: 1                 wc: log2(n)
                                #                       wc: 1
        x = x//2                # bc: 0                 wc: 2 * log2(n) + 1
                                #                       wc: log(2) brengt ons tot x = 1 dus nog 1 x extra
        total += x              # bc: 0                 wc: 2 * log2(n)

    return total                # bc: 1                 wc: 1
                                # best_case: 2003       worst_case: 1 + 2000 + 5 * (log2(n) + 1) + 1 + 1 = 5 * log2(n) + 2008


#### PROGRAM 3
# best: empty list
# worst: L is a list with increasing values

def program3(L):
    totalSum = 0                        # bc: 1                             # wc: 1
    highestFound = None                 # bc: 1                             # wc: 1
    for x in L:                         # bc: 0 (no assignments dus 0)      # wc: n
        totalSum += x                   # bc: 0                             # wc: 2n

    for x in L:                         # bc: 0                             # wc: n         en dan opnieuw n-1 keer
        if highestFound == None:        # bc: 0                             # wc: 1* n      deze 1 * n
            highestFound = x            # bc: 0                             # wc: 1* n      deze is nu False
        elif x > highestFound:          # bc: 0                                             deze nu 1 * n
            highestFound = x            # bc: 0                                             deze 1 * n

    return (totalSum, highestFound)     # bc: 1                             # wc: 1
                                        # best_case: 3                      # worst_case: 2 + 3n + 4n - 1 + 1 = 7 * n + 2




def program1(L):
    multiples = []                  #bc1        #wc1    1
    for x in L:                     #bc0        #wc
        for y in L:                #                    n^2
            multiples.append(x*y)
    return multiples                #bc1                1

3 * n + 2