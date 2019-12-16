#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps = ['rock', 'paper', 'scissors']
    if n <= 0:
        return [[]]
    result = []
    new_arr = []

    def recurse(arr, num):
        if num == 0:
            result.append(arr)
            return
        for item in rps:
            recurse(arr + [item], num - 1)
    recurse(new_arr, n)
    return result


print(rock_paper_scissors(4))
# print([[1, 2, 3]] + [[4, 5, 6]])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
