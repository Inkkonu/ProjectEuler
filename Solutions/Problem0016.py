# Solution for https://projecteuler.net/problem=16

import time


def solve():
    return sum(list(map(int, [i for i in str(2**1000)])))


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 1366
    print(f'Time taken : {time.time() - start}s')  # 141.86 μs
