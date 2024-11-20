num =6
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")

#USING RECURSION

def factorial(n):
    
    
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 


num = 5
print("Factorial of",num,"is",factorial(num))
