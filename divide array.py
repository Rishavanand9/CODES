#https://www.hackerearth.com/practice/algorithms/string-algorithm/z-algorithm/practice-problems/algorithm/divide-array-2/description/

A= list()
N = int(input("Enter how many elements you want:"))
print ("Enter numbers:")
for i in range(int(N)):
    n = input("number:")
    A.append(int(n))
Q=int(input("Enter the number of operations :"))
D=int(input("Enter the Divisor :"))
for i in range(Q):
   for j in range(N-1):
      A[j]=A[j]//D
   print(A)

