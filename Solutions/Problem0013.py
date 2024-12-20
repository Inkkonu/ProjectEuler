# Solution for https://projecteuler.net/problem=13

import time


def solve():
    with open('./Inputs/Problem0013_input.txt', 'r') as f:
        return str(sum([int(line.strip()) for line in f.readlines()]))[:10]


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 5537376230
    print(f'Time taken : {time.time() - start}s')  # 236.03 μs
