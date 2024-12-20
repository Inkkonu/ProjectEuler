# Solution for https://projecteuler.net/problem=15

import time
from functools import cache


def solve():
    return getNumberOfPaths(0, 0, 20)


@cache
def getNumberOfPaths(x: int, y: int, gridSize: int) -> int:
    if x == gridSize and y == gridSize:
        return 1
    if x == gridSize:
        return getNumberOfPaths(x, y+1, gridSize)
    if y == gridSize:
        return getNumberOfPaths(x+1, y, gridSize)
    return getNumberOfPaths(x+1, y, gridSize) + getNumberOfPaths(x, y+1, gridSize)


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 137846528820
    print(f'Time taken : {time.time() - start}s')  # 385.76 μs
