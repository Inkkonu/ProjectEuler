# Solution for https://projecteuler.net/problem=3

import time
from Utilities import isPrime


def solve():
    i, largestPrimeFactor, n = 2, 1, 600851475143
    while i * i < n:
        largestPrimeFactor = i if (
            n % i == 0 and isPrime(i)) else largestPrimeFactor
        i += 1
    return largestPrimeFactor


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 6857
    print(f'Time taken : {time.time() - start}s')  # 51.65 ms
