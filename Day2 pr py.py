#1  Check whether a number is positive, negative or zero
'''
n=int(input("enter the num:"))
if n>0:
    print(n,"is Positive number")
elif n<0:
    print(n,"is Negative number")
else:
    print(n,"is Zero")
'''

#2 Check whether a number is even or odd.
'''
n=int(input("enter the number:"))
if n%2==0:
    print(n,"is Even number")
else:
    print(n,"is Odd number")
'''
#3 Find the largest of three numbers without using max().
'''
n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
n3=int(input("enter the number:"))
if n1>n2 and n1>n3:
    print(n1,"is greater")
elif n2>n1 and n2>n3:
    print(n2,"is greater")
else:
    print(n3,"is greater")
'''
#4  Create a student grading system.
'''
n=int(input("enter the marks:"))
if n==100 and n>=90:
    print("A Grade")
elif n<=89 and n>=80:
    print("B Grade")
elif n<=79 and n>=70:
    print("C Grade")
elif n<=69 and n>=60:
    print("D Grade")
else:
    print("Fail")
'''
#5 Check whether a year is a leap year.
'''
n=int(input("enter the year:"))
if (n%4==0 and n%100!=0) or (n%400==0):
    print(n,"is leap year")
else:
    print(n,"Not a leap year")
'''
#6  Create a simple calculator using +, -, *, /.
'''
n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
print("Addition is =",n1+n2)
print("Subtraction is =",n1-n2)
print("Multiplication is =",n1*n2)
print("Division is =",n1/n2)

'''
marks = int(input("Enter marks: "))

if marks <0 and marks>=100:
    print("Pass")
else:
    print("Fail")
















