def factorial(n):
    if (n==0 or n==1):
        return 1
    return n*factorial(n-1)
    

factorialnumber=int(input("Enter the number to find factorial: "))
print("The factorial of ",factorialnumber," is ",factorial(factorialnumber))