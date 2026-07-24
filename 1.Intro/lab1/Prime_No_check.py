#program to check whether a number is prime or not
n=int(input("Enter a number: "))
prime=0
for i in range(2,n):
    if n%i==0:
        prime=1
                
if prime==1:
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")