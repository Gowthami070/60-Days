#Q1. Print numbers from 1 to 20.
'''
for i in range(1,21):
    print(i,end=' ')
'''
#Q2. Find the sum of numbers from 1 to N.
'''
n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum =",sum)
'''
#Q3. Print the multiplication table of a given number.
'''
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,'*',i,'=',n*i)

'''
#Q4. Count the number of digits in a number.
'''
n=int(input("Enter the number:"))
count=0
while n>0:
        n=n//10
        count=count+1
print(count)
'''
#Q5. Reverse a number.
'''
n=int(input("Enter the number:"))
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)    
'''
#Q6. Check whether a number is prime.

n=int(input("Enter the number:"))
for i in range(2,(n+1)//2):
    if i%2!=0:
        print("Prime number")
    else:
        print("Not prime number")
        
    

























