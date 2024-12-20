# Solution for https://projecteuler.net/problem=11

import time


def solve():
    with open('./Inputs/Problem0011_input.txt', 'r') as f:
        data = [list(map(int, line.strip().split())) for line in f.readlines()]
    greatestProduct = -1
    for i in range(len(data)-3):
        for j in range(len(data[0])):
            if j > 16:
                lp = -1
                rdp = -1
            else:
                lp = data[i][j] * data[i][j+1] * data[i][j+2] * data[i][j+3]
                rdp = data[i][j] * data[i+1][j+1] * data[i+2][j+2] * data[i+3][j+3]

            if j < 3:
                ldp = -1
            else:
                ldp = data[i][j] * data[i+1][j-1] * data[i+2][j-2] * data[i+3][j-3]

            cp = data[i][j] * data[i+1][j] * data[i+2][j] * data[i+3][j]

            greatestProduct = max(greatestProduct, lp, cp, rdp, ldp)
    return greatestProduct


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 70600674
    print(f'Time taken : {time.time() - start}s')  # 405.31 μs
