#Part 4: String Problems
'''
Q22. Check whether a string is a palindrome without using slicing.
Q23. Count vowels, consonants, digits and special characters in a string.
Q24. Find the first non-repeating character in a string.
Q25. Remove duplicate characters from a string while preserving order.
'''

#22
'''
n=input("Enter the characters:")
pal=''
for i in range(len(n) -1,-1,-1):
    pal=pal+n[i]
if n==pal:
    print("Palindrome string")
else:
    print("Not a Palindrome string")
'''
#23
'''
n=input("Enter the string:")    
vowel_cnt=0
cons_cnt=0
digit_cnt=0
spl_cnt=0
for i in n:
    if i in "aeiouAEIOU":
        vowel_cnt+=1
    elif i.isalpha() and i not in "aeiouAEIOU":
        cons_cnt+=1
    elif i.isdigit():
        digit_cnt+=1
    else:
        spl_cnt+=1
print("Vowels =",vowel_cnt)
print("Consonents =",cons_cnt)
print("Digits =",digit_cnt)
print("Special chars =",spl_cnt)
'''
#24
'''
n=input("Enter the string")
for i in n:
    count=n.count(i)
    if count==1:
        print(i)
        break
else:
    print("Not found")
'''
#25
'''
n=input("Enter the string:")
dupli_chars=''
for i in n:
    if i not in dupli_chars:
        dupli_chars+=i
    else:
        #dupli_chars=i
        pass
print("The string is:",dupli_chars)
'''













