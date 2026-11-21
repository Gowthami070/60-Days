#Part 3: Loops & Number Logic
'''
Q15. Check whether a number is prime.
Q16. Print all prime numbers between 1 and N.
Q17. Find the factorial of a number without using math.factorial().
Q18. Print the Fibonacci series up to N terms.
Q19. Check whether a number is an Armstrong number.
Q20. Find the GCD and LCM of two numbers.
Q21. Print the following pattern:
1
12
123
1234
12345
'''
#15
'''
n=int(input("enter the number:"))
if n<2:
    print("Its not a prime number:")
else:
    for i in range(2,n):
        if n%i==0:
            print("Its not prime")
            break
    else:
        print("Its prime")
        '''
#16
'''
n=int(input("enter the number:"))
for n in range(2,n+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n,end=" ")
      '''  
#17
'''
num=int(input("Enter the number:"))
fact=1
while num>0:
    if num==0 or num==1:
        fact = 1
        print("Factorial of a number is:",fact)
    else:
        fact = num*fact(num-1)
    
print("Factorial of a number is:",fact)
'''
        #or
'''  
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial =", fact)       
'''
#18
'''
n=int(input("Enter the number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
'''
#19
'''
n = int(input("Enter a number: "))
temp = n
power = len(str(n))
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10
if total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
'''
#20
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
x = a
y = b
while b != 0:
    a, b = b, a % b
gcd = a
lcm = (x * y) // gcd
print("GCD =", gcd)
print("LCM =", lcm)
'''
#21
'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    '''
