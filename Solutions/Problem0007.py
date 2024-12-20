# Solution for https://projecteuler.net/problem=7

import time
from itertools import count
from Utilities import isPrime


def solve():
    counter = 0
    for i in count(start=2):
        if isPrime(i):
            counter += 1
            if counter == 10_001:
                return i


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 104743
    print(f'Time taken : {time.time() - start}s')  # 124.11 ms
