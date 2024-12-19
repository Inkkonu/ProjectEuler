# Solution for https://projecteuler.net/problem=5

from itertools import count
import time


def solve():
    for i in count(start=20, step=2):  # step=2 Because odd numbers are never divisible by 2
        if all([i % j == 0 for j in range(2, 21)]):
            return i


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 232792560
    print(f'Time taken : {time.time() - start}s')  # 75.48 s
