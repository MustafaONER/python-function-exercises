#3. Guessing number
"""Write a guessing number function that holds a random number between 1 and 10 and get a parameter number. The return for that function will be :

"Too big" if the parameter number is bigger than the held number.
"Too small" if the parameter number is smaller than the held number.
"You are SUPER" if the parameter number is the same as the held number.
Enter the parameter number via the terminal with a help of the input method."""

from random import randint  
number = input( "Please enter some number: " )
randint( 1, 10 )
def guessNumber(number):
    num=randint( 1, 10 )
    if (number>num):
        print('too big')
    elif  (number<num):
      print('too small')
    else:
      print('You are SUPER')
guessNumber(int(number))