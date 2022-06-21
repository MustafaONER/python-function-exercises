# 1. Multiplication
#Create a function that gets a number as a parameter, and then prints the multiplication table for that number from 1 to 10. E.g., when the parameter is 12, the first line printed is “1 x 12 = 12” and the last line printed is “10 x 12 = 120.”

def mult(parameter):
    for num in range(1,11,1):
        print('{} * {} ={}'.format(num,parameter,parameter*num))
        
mult(12)



