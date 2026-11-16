#Q1. Basic operations
'''
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
print("Addition is:",n1+n2)
print("Subtraction is :",n1-n2)
print("Multiplication is:",n1*n2)
print("Division is:",n1/n2)
print("Modulus is:",n1//n2)
'''

#Q2. Swap variables

# without 3rd variable
#pythonic way
'''
a=10
b=5
a,b=b,a
print("a =",a)
print("b =",b)
'''
#arthmetic way
'''
a=10
b=5
a=a+b
b=a-b
a=a-b
print(a)
print(b)
'''
#with 3rd variable
'''
a=10
b=5
temp=a
a=b
b=temp
print("A=",a)
print("B=",b)
'''

#Q3. Reverse a number
'''
rev=0
num=int(input("enter the number:"))
print("actual number =",num)
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("Reversed number:",rev)

'''
#Q4. Find the output
'''
a = 10
b = 3
print(a / b) #3.33
print(a // b)#3
print(a % b)#1
print(a ** b)#1000
'''
#Q5. Type conversion
'''
a = "100"
b = 50
c=int(a)+b
print("Sum=",c)
'''
#Q6. Find the output
'''
x = 10
y = x
x = 20
print(x)#20
print(y)#10
'''
#Q7. Practical problem
''''
Take a student's name and marks in three subjects. Calculate:
- Total marks
- Average
- Percentage (assuming each subject is out of 100)
'''
sum=0
name=input("enter the name:")
marks1=int(input("Enter the number:"))
marks2=int(input("Enter the number:"))
marks3=int(input("Enter the number:"))
total_marks=marks1+marks2+marks3
print("Total_marks :",total_marks)
average_marks=total_marks/3
print("Average_marks :",average_marks)
percentage=(total_marks/300)*100
print("percentage :",percentage)








