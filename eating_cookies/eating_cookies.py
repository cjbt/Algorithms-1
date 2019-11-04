#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

cache = {

}
def eating_cookies(n, cache=cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1 # true => value now at 1
    elif n in cache:
        return cache[n]
    else:
        result = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        cache[n] = result
        print(cache)
        return result

print(eating_cookies(3))


"""
one
1 cookie

two
1 cookie + 1 cookie
2 coookies

three
1 cookie + 1 cookie + 1 cookie
2 cookies + 1 cookie
1 cookies + 2 cookies
3 cookies

four
1 cookie + 1 cookie + 1 cookie + 1 cookie
2 cookies + 1 cookie + 1 cookie
1 cookie + 2 cookies + 1 cookie
3 cookies + 1 cookie
1 cookie + 1 cookie + 2 cookies
2 cookies + 2 cookies
1 cookie + 3 cookies


========

if n > 3: n + 1, n + 2, n + 3
else: n, n + 1, n + 2

add n and minus 1 to it,
add 

==========

five
1 cookie + 1 cookie + 1 cookie + 1 cookie + 1 cookie
1 cookie + 2 cookies + 1 cookie + 1 cookie
2 cookies + 1 cookie + 1 cookie + 1 cookie
3 cookies + 1 cookie + 1 cookie
1 cookie + 1 cookie + 2 cookies + 1 cookie
2 cookies + 2 cookies + 1 cookie
1 cookie + 3 cookies + 1 cookie
1 cookie + 1 cookie + 1 cookie + 2 cookie
1 cookies + 2 cookies +  2 cookie
2 cookies + 1 cookie + 2 cookie
3 cookies + 2 cookie
1 cookie + 1 cookie + 3 cookie
2 coookies + 3 cookie

six

1 cookie + 1 cookie + 1 cookie + 1 cookie + 1 cookie + 1 cookie 
1 cookie + 2 cookies + 1 cookie + 1 cookie + 1 cookie 
2 cookies + 1 cookie + 1 cookie + 1 cookie + 1 cookie 
3 cookies + 1 cookie + 1 cookie + 1 cookie 
1 cookie + 1 cookie + 2 cookies + 1 cookie + 1 cookie 
2 cookies + 2 cookies + 1 cookie + 1 cookie 
1 cookie + 3 cookies + 1 cookie + 1 cookie 
1 cookie + 1 cookie + 1 cookie + 2 cookie + 1 cookie 
1 cookies + 2 cookies +  2 cookie + 1 cookie 
2 cookies + 1 cookie + 2 cookie + 1 cookie 
3 cookies + 2 cookie + 1 cookie 
1 cookie + 1 cookie + 3 cookie + 1 cookie 
2 coookies + 3 cookie + 1 cookie
1 cookie + 1 cookie + 1 cookie + 1 cookie + 2 cookies
2 cookies + 1 cookie + 1 cookie + 2 cookies
1 cookie + 2 cookies + 1 cookie + 2 cookies
3 cookies + 1 cookie + 2 cookies
1 cookie + 1 cookie + 2 cookies + 2 cookies
2 cookies + 2 cookies + 2 cookies
1 cookie + 3 cookies + 2 cookies
1 cookie + 1 cookie + 1 cookie + 3 cookies
2 cookies + 1 cookie + 3 cookies
1 cookies + 2 cookies + 3 cookies
3 cookies + 3 cookies

"""


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
