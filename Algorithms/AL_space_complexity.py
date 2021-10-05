# O(1) space complexity
def factorial1(n):
    fac = 1
    for index in range(2, n+1):
        fac *= index
    return fac

# O(n) space complexity
def factorial2(n):
    if n > 1:
        return n * factorial2(n-1)
    else:
        return 1