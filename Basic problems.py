#Part 1: Variables, Operators & Numbers
'''
Q1. Swap two numbers without using a third variable.
Q2. Find the sum of digits of a given number.
Q3. Reverse a given integer without converting it into a string.
Q4. Check whether a given number is a palindrome.
Q5. Find the product of all digits in a number.
Q6. Count the number of digits in a given integer.
Q7. Find the difference between the sum of even digits and odd digits.
Q8. Convert a given number of seconds into hours, minutes and seconds.
'''
#1
'''
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
a,b=b,a
print("A =",a)
print("B =",b)
'''
#2
'''
n=int(input("Enter the number:"))
n=abs(n)
digit_sum=0
while n>0:
    dig=n%10
    digit_sum=digit_sum+dig
    n=n//10
print("Sum =",digit_sum)
'''
#3
'''
n=int(input("Enter the number:"))
rev=0
n=abs(n)
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reversed number =",rev)
'''
#4
'''
n=int(input("Enter the number:"))
pal=0
temp=n
while n>0:
    dig=n%10
    pal=pal*10+dig
    n=n//10
if temp>=0 and temp==pal:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
#5
'''
n=int(input("Enter the number:"))
n=abs(n)
product=1
if n==0:
    product=0
else:
    while n>=0:
        dig=n%10
        product=product*dig
        n=n//10
print("Product=",product)
'''
#6
'''
n=int(input("Enter the number:"))
n=abs(n)
count=0
if n==0:
    count=1
else:
    while n>0:
        dig=n%10
        count=count+1
        n=n//10
print("count =",count)
'''
#7
'''
n=int(input("Enter the number:"))
even_digits=0
odd_digits=0
while n>0:
    dig=n%10
    if dig%2==0:
        even_digits+=dig
    else:
        odd_digits+=dig
    n=n//10
print("Even sum =",even_digits)
print("Odd sum =",odd_digits)
print("Difference =",even_digits-odd_digits)
'''


#8
'''
total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)
'''
















