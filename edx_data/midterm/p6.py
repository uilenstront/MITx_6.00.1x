def sumDigits(N):
    if N == 0:
        return 0
    else:
        return N % 10 + sumDigits(N // 10)

print(sumDigits(34))



# def count7(N):
#     if N == 7:
#         return 1
#     elif N < 7:
#         return 0
#     elif N % 10 == 7:
#         return 1 + count7(N // 10)
#     else:
#         return 0 + count7(N // 10)
#
# print(count7(0))