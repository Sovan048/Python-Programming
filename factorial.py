n = int(input("Enter a number: "))

factorial = 1

if(n <= 0):
    print("Number should be a positive integer")
else:    
    for i in range(1,n+1):
        factorial = factorial * i
        print(f"The factorial of {n} is = {factorial}")  
