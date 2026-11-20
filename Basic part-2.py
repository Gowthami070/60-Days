#Part 2: Conditional Statements
'''
Q9. Find the largest among three numbers without using max().
Q10. Check whether a year is a leap year.
Q11. Check whether a character is an alphabet, digit or special character.
Q12. Calculate an electricity bill based on given unit slabs.
Q13. Create a simple calculator using operators.
Q14. Check whether three given sides can form a valid triangle and identify its type.
'''
#9
'''
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
n3=int(input("Enter the number:"))
if n1>=n2 and n1>=n3:
    print(n1,"is largest number")
elif n2>=n1 and n2>=n3:
    print(n2,"is largest number")
else:
    print(n3,"is largest number")
'''
#10
'''
year=int(input("Enter the number:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is the leap year")
else:
    print(year,"Its not a leap year")
'''
#11
'''
char=input("Enter the character:")
if char.isdigit():
    print(char,"is the digit")
elif char.isalpha():
    print(char,"is the alphabet")
else:
    print(char,"is the special character")
'''
#12
'''
units=int(input("Enter the units:"))
if units<0:
    print("Invalid units")
elif units<=100:
    bill=units*2
    print("The electricity bill is:",bill,"rupees")
elif units<=200:
    bill=(100*2)+(units - 100)*3
    print("The electricity bill is:",bill,"rupees")
else:
    bill=(100*2)+(100*3)+(units - 200)*5
    print("The electricity bill is:",bill,"rupees")
'''
#13
'''
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
choice=input("choose the option (+,-,*,/):")
if choice == '+':
    add=n1+n2
    print("The addition result is:",add)
elif choice == '-':
    sub=n1-n2
    print("The subtraction result is :",sub)
elif choice == '*':
    mul=n1*n2
    print("The multiplication result is :",mul)
elif choice == '/':
    if n2!=0:
        div=n1/n2
        print("The division result is:",div)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")
'''
#14

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a :
    print("Its valid triangle")
    if a==b==c:
        print("Its a 'Equilateral' triangle")
    elif a==b or a==c or b==c:
        print("Its a 'Isosceles' triangle")
    else:
        print("Its a 'Scalene' triangle")
else:
    print("It is invalid triangle")
























