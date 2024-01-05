# Individual Digit Sum Ex :- 12345 = 1+2+3+4+5 = 15

n = int(input("Enter A Number: "))
s=0
while n>0 :
    r = n%10
    s = s+r
    n = n//10
else:
    print('Total Sum Of Individual Digit Are:' , s)
