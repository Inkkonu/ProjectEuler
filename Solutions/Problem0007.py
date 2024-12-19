# Solution for https://projecteuler.net/problem=7

import time
from itertools import count


def solve():
    counter = 0
    for i in count(start=2):
        if isPrime(i):
            counter += 1
            if counter == 10_001:
                return i


def isPrime(n: int):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 104743
    print(f'Time taken : {time.time() - start}s')  # 124.11 ms
