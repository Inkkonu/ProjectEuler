# Solution for https://projecteuler.net/problem=9

import time


def solve():
    return sum([i for i in range(2, 2_000_000) if isPrime(i)])


def isPrime(n: int):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 142913828922
    print(f'Time taken : {time.time() - start}s')  # 8.81 s
