# Solution for https://projecteuler.net/problem=14

import time
from functools import cache


def solve():
    longestSequence, startingNumber = -1, -1
    for i in range(1, 1_000_000):
        seq = getSequence(i)
        if len(seq) > longestSequence:
            longestSequence = len(seq)
            startingNumber = i
    return startingNumber


@cache
def getSequence(n: int) -> list:
    if n == 1:
        return [n]
    return [n] + getSequence(n//2 if (n & 1) == 0 else 3*n+1)


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 837799
    print(f'Time taken : {time.time() - start}s')  # 7.35 s
