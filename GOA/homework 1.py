# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 
def square_sum(numbers):
    my_sum=0
    for num in numbers:
        my_sum+=(num**2)
    return my_sum





# Write a program that finds the summation of every number from 1 to num. The number will always be a positive 
# integer greater than 0.
# For example (Input -> Output):
def summation(num):
    my_sum=0
    for i in range(num+1):
        my_sum+=i
    return my_sum


# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):

def digitize(n):
    
    arr=[]
    
    for element in str(n):
        arr.append(int(element))
    
    return arr[::-1]




# Write a function `greet` that returns "hello world!"
def greet():
    return "hello world!"



# Write a function that removes the spaces from the string, then return the resultant string.
# Examples:
# Input -> Output
# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"

def no_space(x):
    my_string=x
    y_new_string = my_string.replace(" ","")
    return y_new_string




# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7

def string_to_number(s):
    return int(s)

# Code as fast as you can! You need to double the integer and return it.
def double_integer(i):
    return i*2




