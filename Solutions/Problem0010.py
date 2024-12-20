# Solution for https://projecteuler.net/problem=10

import time
from Utilities import isPrime


def solve():
    return sum([i for i in range(2, 2_000_000) if isPrime(i)])


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 142913828922
    print(f'Time taken : {time.time() - start}s')  # 8.81 s
