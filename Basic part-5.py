#Part 5: Advanced Basic Challenges
'''
Q26. Find the second-largest number in a list without using sort() or max().
Q27. Remove duplicates from a list without using set().
Q28. Find the missing number in a list containing numbers from 1 to N.
Q29. Find the frequency of each element in a list.
Q30. Merge two lists and find common elements without using built-in set operations.
'''
#26
'''
n=list(map(int,input("Enter the numbers:").split()))
largest_num=float('-inf')
second_num=float('-inf')
for i in n:
    if i>largest_num:
        second_num=largest_num
        largest_num=i
    elif i>second_num and i<largest_num:
        second_num=i
print("Second largest =",second_num)
'''
#27
'''
n=[2,3,5,2,6,4,5,7,3]
original_list=[]
for i in n:
    if i not in original_list:
        original_list.append(i)
print("The list is =",original_list)
'''
#28
'''
numbers = [1, 2, 3, 5, 6]
N = 6
expected_sum = N * (N + 1) // 2
actual_sum = 0
for i in numbers:
    actual_sum += i
missing_number = expected_sum - actual_sum
print("Missing number:", missing_number)
'''
#29
'''
n = list(map(int, input("Enter the numbers:").split()))
frequency = {}
for i in n:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
for key, value in frequency.items():
    print(key, ":", value)
'''
#30
'''
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
merged_list=list1+list2
print("Merged list :",merged_list)
common=[]
for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print("common elements :",common)
'''
