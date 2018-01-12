#https://www.hackerrank.com/challenges/ctci-lonely-integer/problem

import sys
def lonely_integer(a):
    result = 0
    for i in a:
        result = result ^ i
    return result


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
