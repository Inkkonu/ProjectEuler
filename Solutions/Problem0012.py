# Solution for https://projecteuler.net/problem=12

import time
from itertools import count
from Utilities import getDivisors, getTriangleNumber


def solve():
    for i in count():
        triangleNumber = getTriangleNumber(i)
        if len(getDivisors(triangleNumber)) > 500:
            return triangleNumber


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 76576500
    print(f'Time taken : {time.time() - start}s')  # 2.91 s
