#Practice_01
import math
#calculate the factorial of given number
# n! = n * (n-1) * (n-2) * (n-3)

x = int(input("ENTER YOUR NUMBER"))
fact = 1

for i in range(1 , x + 1):
    fact = fact * i

print(fact)