import time

def c_to_f(c):
    return c * 9 / 5 + 32

t0 = time.time()

# 100000000 ~ 1,5 seconds
# 1000000000 ~ 15 seconds

for i in range(100000000):
    c_to_f(i)

t1 = time.time() - t0

print("time =", t0, ":", t1, "s")