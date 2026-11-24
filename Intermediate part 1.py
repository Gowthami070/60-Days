#A. Functions & Problem Solving
'''
PY01. Write a function that returns the second-largest distinct number in a list without sort() or max().
PY02. Return separate lists of even and odd numbers from a given list.
PY03. Check whether two strings are anagrams, ignoring spaces and letter case.
PY04. Find the most frequent character in a string; if tied, return the first one encountered.
PY05. Write a recursive function to calculate the sum of digits of a positive integer.
PY06. Return the running total of a list as a new list.
'''
#1
'''
def largest_second_num(list1):
    largest=second=float('-inf')
    for i in list1:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i<largest:
            second=i

    return second
list1=[5,8,9,2,4,6,1]
res=largest_second_num(list1)
print("Second largest num:",res)
'''
#2
'''
def even_odd_num(list1):
    even_num=[]
    odd_num=[]
    for i in list1:
        if i%2==0:
            even_num.append(i)
        else:
            odd_num.append(i)
    return even_num,odd_num
list1=[5,8,9,2,4,6,1]
res=even_odd_num(list1)
print("Even nums",res)
'''
#3
'''
str1="silent"
str2="listen"
if sorted(str1)==sorted(str2):
    print("Anagram")
else:
    print("Not a anagram")
'''
#4

#5
'''
def positive_digit_sum(list1):
    positive_sum=0
    for i in list1:
        if i>0:
            positive_sum+=i
        else:
            pass
    return positive_sum
list1=[5,8,-2,9,2,4,6,1,0,-6]
res=positive_digit_sum(list1)
print("The sum is =",res)
'''
