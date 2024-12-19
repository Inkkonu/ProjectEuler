# Solution for https://projecteuler.net/problem=4

import time


def solve():
    largestPalindrome = -1
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if isPalindromic(i*j):
                largestPalindrome = max(i*j, largestPalindrome)
    return largestPalindrome


def isPalindromic(n: int):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    start = time.time()
    print(solve())  # 906609
    print(f'Time taken : {time.time() - start}s')  # 128.38 ms
