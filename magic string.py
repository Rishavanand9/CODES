#https://www.hackerearth.com/problem/algorithm/its-all-about-magic/description/

M=int(input().strip())
s="1"
for i in range(M):
    l=len(s)
    for j in range(l):
        if s[j]=="1":
            s=s.replace("1","0")
        elif s[j]=="0":
            s=s.replace("0","0 1")
        print(s)

