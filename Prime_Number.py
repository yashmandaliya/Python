# Input two integer number and print all prime number between this..

n1=int(input("Enter a no:"))
n2=int(input("Enter a 2 no:"))

if n1>n2:
    n1,n2 = n2,n1

if n1<=2:
    print(2,"IS PRIME")
    n1 =3

if n1%2==0:
    n1+=1
    print("n1=",n1)

for i in range(n1,n2+1,2):
    flag =0
    for j in range(3,(i//2)+1,2):
        if i%j==0:
            flag =1
            break
    if flag == 0:
        print(i ,"IS PRIME")

# Outpput :-

Enter a no:1
Enter a 2 no:100
2 IS PRIME
3 IS PRIME
5 IS PRIME
7 IS PRIME
11 IS PRIME
13 IS PRIME
17 IS PRIME
19 IS PRIME
23 IS PRIME
29 IS PRIME
31 IS PRIME
37 IS PRIME
41 IS PRIME
43 IS PRIME
47 IS PRIME
53 IS PRIME
59 IS PRIME
61 IS PRIME
67 IS PRIME
71 IS PRIME
73 IS PRIME
79 IS PRIME
83 IS PRIME
89 IS PRIME
97 IS PRIME
