# Print Series :- 1 ,2 ,4 ,7 ,11 ,16 ,22 ,29 ,37 ,46 
n = int(input("Enter A No:"))
a=1
b=1
for i in range(n):
    print(a,",",end="")
    a+=b
    b+=1

print("")


# Print Series :-  1 ,2 ,5 ,10 ,17 ,26 ,37 ,50 ,65 ,82
n = int(input("Enter A No:"))
a=1
b=1
for i in range(n):
    print(a,",",end="")
    a+=b
    b+=2
print("")


# Print Series :-  1 ,2 ,4 ,8 ,15
n=int(input("Enter NO:"))
a=1
b=1
c=1
for i in range(n):
    print(a,",",end="")
    a+=b
    b+=c
    c+=1

print("")


#  Print Series :- 1 ,2 ,6 ,24 ,120 ,
n=int(input("Enter NO:"))
a=1
b=2
c=1
for i in range(n):
    print(a,",",end="")
    a*=b
    b+=c
    c=1
print("")


#  Print Series :- 1 ,2 ,4 ,8 ,16
n = int(input("Enter NO:"))
a=1
b=2
for i in range(n):
    print(a,",",end="")
    a*=b
    b=2
print("")
