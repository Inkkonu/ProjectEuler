# Solution for https://projecteuler.net/problem=1

import time


def solve():
    print(sum({i for i in range(3, 1000, 3)} | {i for i in range(5, 1000, 5)}))


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 233168
    print(f'Time taken : {time.time() - start}s')  # 294.45 μs
