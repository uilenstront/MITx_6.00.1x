def fib_iter(n):
    if n == 0:  # constant = O(1)
        return 0
    elif n == 1:  # constant = O(1)
        return 1

    else:
        fib_i = 0   # constant = O(1)
        fib_ii = 1  # constant = O(1)
        for i in range(n-1):    # linear O(n)
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii

    # best case = O(1)
    # worst case = O(n)

def fib_recur(n):
    if n == 0:     # constant = O(1)
        return 0
    elif n == 1:       # constant = O(1)
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)
    # two recursive calls, so it's exponential
    # worst case: O(2^n)




print(fib_iter((7)))
print(fib_recur((7)))

a = [1, 2, 3, 4, 0]

print(a[a[1]])


num = 5
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

a = [1, 2, 5, 7, 9]


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

print(search(a, 3))
print(search1(a, 3))