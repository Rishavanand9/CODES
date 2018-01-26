#https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/programming-competition



import sys

n = int(input().strip())
diff = {}
for i in range(n):
    name, d, j = input().strip().split(' ')
    name, d, j = [str(name), int(d), int(j)]
    x = j - d
    diff[name] = x

M = max(diff, key=diff.get)
print(M, diff[M])
