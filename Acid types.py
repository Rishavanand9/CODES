#https://www.hackerrank.com/contests/w36/challenges/acid-naming



#!/bin/python3



import sys


def acidNaming(acid_name):
    if acid_name[0:5] == "hydro" and acid_name[-2:] == "ic":
        print("non-metal acid")
    elif acid_name[-2:] == "ic":
        print("polyatomic acid")
    else:
        print("not an acid")
    return


if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)

