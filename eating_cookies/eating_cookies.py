#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n <= 0:
        return 1
    return eating_cookies(n - 1)
# 1, 1
# 2, 2
# 3, 4


"""
1 - 
1 cookie 1 time/all cookies

2-
1 cookie then 1 cookie
2 coookies 1 time

3 - 
1 cookie 3 times
1 cookies then 2 cookies
2 cookies then 1 cookie
3 cookies 1 time

4-
1 cookie 4 times
1 cookie then 3 cookies
1 cookie then 2 cookies then 1 cookie
1 cookie then 1 cookie then 2 cookies
2 cookies then 2 cookies
2 cookies then 1 cookie then 1 cookie
3 cookies then 1 cookie

5 - 
1 cookie 5 times
1 cookie then 1 cookie then 3 cookies
1 cookie then 3 cookies then 1 cookie
1 cookie then 2 cookie then 2 cookie
1 cookie then 1 cookie then 1 cookie then 2 cookie
1 cookie then 1 cookie then 2 cookies then 1 cookie
1 cookie then 2 cookies then 1 cookie then 1 cookie
2 cookies then 3 cookies
2 cookies then 1 cookies then 2 cookies
2 cookies then 2 cookies then 1 cookies
2 cookies then 1 cookie then 1 cookie then 1 cookie
3 cookies then 2 cookies
3 cookies then 1 cooke then 1 cookie
"""


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
