#Solve the single problem
R=float(input())
n=3.14159
r=n*R*R
print(f"A={r:.4f}")

#Solve the single problem
A=int(input())
B=int(input())
sum=A+B
print(f"SOMA = {sum}")

#Solve the single problem
A=float(input())
B=float(input())
C=float(input())
Y=(A*2+B*3+C*5)/10
result=Y/X
print(f"MEDIA = {result:.1f}")

#Solve the single problem
Employee_name=input()
A=float(input())
B=float(input())
Total=(A + .15*B)
print(f"TOTAL = R$ {Total:.2f}")

#Solve the single problem
A,B,C=map(float,input().split())
pi=3.14159
triangle=.5*A*C
circle=pi*C*C
trapezium=.5*(A+B)*C
squre=pow(B,2)
rectangle=A*B
print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {squre:.3f}")
print(f"RETANGULO: {rectangle:.3f}")

#Solve the single problem
A,B,C=map(int,input().split())
mx=max(A,B,C)
print(f"{mx} eh o maior")

#Solve the single problem
import math
X1,Y1=map(float,input().split())
X2,Y2=map(float,input().split())
sum=(X2-X1)**2+(Y2-Y1)**2
distance=math.sqrt(sum)
print(f"{distance:.4f}") 

#Recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5) 