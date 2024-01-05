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
