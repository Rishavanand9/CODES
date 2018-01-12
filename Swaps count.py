#https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
for i in range(n):
    for j in range(n - 1):
        count = 0
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            count = count + 1

print("Array is sorted in", count, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[n - 1])

