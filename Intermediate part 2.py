#Question 1: Smart Warehouse Stock Analyzer
'''
A warehouse stores products in different storage locations. Each location contains a certain number of products.
Write a Python program to count how many storage locations contain fewer than 50 products.
Input Format:
•	First line contains an integer N, representing the number of storage locations.
•	Second line contains N space-separated integers representing product quantities.
Output Format:
Print the number of locations containing fewer than 50 products.
Sample Test Case 1
Input:
6
120 35 80 20 45 100
Output:
3
Sample Test Case 2
Input:
5
60 70 80 90 100
Output:
0
Constraints:
•	1 ≤ N ≤ 100000
•	0 ≤ quantity ≤ 1000000
Expected Concepts: For loop, if condition, counter.
'''
####
'''
N=int(input("Enter the no.of storage locations:"))
product_cnt=0
for product_quantity in range(N):
    product_quantity=int(input("enter the quantities:"))
    if product_quantity <= 50:
        product_cnt+=1
print("The number of locations containing fewer than 50 products are:",product_cnt)
'''
#Question 2: Consecutive Temperature Stability
'''
A weather monitoring system records daily temperatures. Identify the maximum number of consecutive days during which the temperature remains below 30 degrees.
Input Format:
•	First line contains integer N.
•	Second line contains N space-separated temperature values.
Output Format:
Print the maximum consecutive count of days with temperatures below 30.
Sample Test Case 1
Input:
8
25 27 29 35 28 26 24 31
Output:
3
Sample Test Case 2
Input:
6
32 35 40 28 29 27
Output:
3
Constraints:
•	1 ≤ N ≤ 100000
•	-50 ≤ temperature ≤ 100
Expected Concepts: For loop, counter reset, maximum tracking.
'''
###
'''
N=int(input("Enter the no.of days:"))
temp_cnt=0
print("Enter the Temperature values:")
for temp_vals in range(N):
    temp_vals=int(input())
    if temp_vals<=30:
        temp_cnt+=1
print("The temperature values below 30 is:",temp_cnt)
'''




























