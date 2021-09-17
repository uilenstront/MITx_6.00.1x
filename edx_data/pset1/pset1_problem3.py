s = 'zyxwvutsrqponmlkjihgfedcba'

l = 1
longest = 0
start = 0

for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        l += 1
        if l > longest:
            longest = l
            start = i - (l - 1)
    else:
        l = 1           #reset the counter if the list isn't long enough

# if longest string is not in the 'body', it only the first char -- zyxwvutsrqponmlkjihgfedcba
if longest == 0:
    longest += 1

print("Longest substring in alphabetical order is:", s[start:start+longest])
