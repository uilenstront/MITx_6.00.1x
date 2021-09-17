def fib(n, d):
    """"
    n = nth
    d = dictionary
    """
    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib(6, d))
