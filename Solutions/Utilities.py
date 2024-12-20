from functools import cache


def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


@cache
def getTriangleNumber(n: int) -> int:
    if n <= 1:
        return n
    return n + getTriangleNumber(n-1)


def getDivisors(n: int) -> set:
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
        i += 1
    return divisors
