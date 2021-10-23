'''
Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order.
A prime number is a number that is divisible only by 1 and itself. This function takes in an integer and returns a list of integers.
'''

def prime(N):
    primes = []

    for i in range(2, N + 1):
        if i > 1:
            for j in range (2, i):
                if (i % j) == 0:
                    break
            else:
                primes.append(i)
    return primes



l = 8
print(prime(l))