n = int(input("Enter A No:"))
m=n
c=0
while m>0:
    c=c+1
    m=m//10


m=n
s=0

while m>0:
    r=m%10
    s=s+r **c
    m=m//10


    if n==s:
        print(n,"Is Armstrong")
    else:
        print(n,"Is Not Armstrong")
