#Factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

#Fibonacci
dp=[-1]*1005
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1 
    if dp[n]!=-1:
        return n       
    dp[n]=fibonacci(n-1)+fibonacci(n-2)
    return dp[n]
f=int(input("Enter the value:"))
print(f"Fibonacci of {f}->{fibonacci(f)}") 

#Bottom-up apross Fibonacii
n=8
fibo=[-1]*105
fibo[0]=0
fibo[1]=1
for i in range(2,n+1):
    fibo[i]=fibo[i-1]+fibo[i-2]
print(fibo[n]) 

#Stairs problem
dp=[-1]*105
def stairs(n):
    if n<3:
        return n 
    if dp[n]!=-1:
        return dp[n]    
    dp[n]=stairs(n-1)+stairs(n-2)
    return dp[n]
print(stairs(5)) 