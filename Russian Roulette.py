#https://www.hackerrank.com/contests/w36/challenges/revised-russian-roulette


# !/bin/python3

import sys


def revisedRussianRoulette(doors):
    count = 0
    c = 0
    for j in range(n):
        if doors[j] == 1:
            c = c + 1
    for i in range(n):
        if doors[i] == 1:
            doors[i] = 0
            count = count + 1
            if doors[i + 1] == 1:
                doors[i + 1] = 0

    print(count, c)


if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)



