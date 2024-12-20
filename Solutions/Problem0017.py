# Solution for https://projecteuler.net/problem=17

import time
from num2words import num2words


def solve():
    return sum([len(num2words(i).replace(' ', '').replace('-', '')) for i in range(1, 1001)])


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 21124
    print(f'Time taken : {time.time() - start}s')  # 22.50 ms
