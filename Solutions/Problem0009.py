# Solution for https://projecteuler.net/problem=9

import time
from math import sqrt


def solve():
    for a in range(1, 1000):
        for b in range(a+1, 1000):
            c = sqrt(a**2 + b**2)
            if a+b+c == 1000:
                return a*b*c


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 31875000
    print(f'Time taken : {time.time() - start}s')  # 28.97 ms
