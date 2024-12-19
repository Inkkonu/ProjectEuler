# Solution for https://projecteuler.net/problem=2

from functools import cache
from itertools import count
import time


def solve():
    total = 0
    for i in count():
        f = fibonacci(i)
        if f <= 4_000_000:
            total += f if (f & 1) == 0 else 0
        else:
            return total


@cache
def fibonacci(n: int):
    if n <= 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 4613732
    print(f'Time taken : {time.time() - start}s')  # 134.47 μs
