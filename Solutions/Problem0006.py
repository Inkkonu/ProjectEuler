# Solution for https://projecteuler.net/problem=6

import time


def solve():
    return sum([i for i in range(1, 101)])**2 - sum([i**2 for i in range(1, 101)])


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 25164150
    print(f'Time taken : {time.time() - start}s')  # 125.89 μs
