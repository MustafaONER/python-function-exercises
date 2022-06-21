# 2. Sum of two strings
#Write a function that gets as parameters two strings. The function returns the number of characters that the strings have in common. Each character counts only once, e.g., the strings "bee" and "peer" only have one character in common (the letter “e”). You can consider capitals different from lower case letters. Note: the function should return the number of characters that the strings have in common, and not print it. To test the function, you can print the result in your main program.

str1=input('first string: ')       
str2=input('second string: ')         
def sum_string(str1,str2):
    list=set()
    for letter in str1 :
       if str2.find(letter)>=0:
           list.add(letter)
    print(len(list))  
sum_string(str1,str2)