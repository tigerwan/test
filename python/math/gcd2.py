
i = 0

def gcd(a, b):
    global i
    i = i + 1
    # print(i)
    if a == b:
        return a
    if a < b:
        return gcd(a, b - a)
    else:
        return gcd(a - b, b)

# gcd(15, 21)
print(gcd(6, 10))
