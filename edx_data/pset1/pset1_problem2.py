b = 'bob'
count = 0

l = len(b)

for i in range(len(s)):
    if s[i:i+l] == b:
        count += 1
print(" Number of times bob occurs is: ", count)