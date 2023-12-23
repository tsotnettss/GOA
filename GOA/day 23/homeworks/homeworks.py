# Simple multiplication
# This kata is about multiplying a given number by eight 
# if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    if number % 2 ==1:
        return number*9
    return number * 8


# A Needle in the Haystack
# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

def find_needle(haystack):
    index = haystack.index("needle")

    return ("found the needle at position "+str(index))


# Find Maximum and Minimum Values of a List
# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language )
# that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

def minimum(arr):
    arr.sort()
    return arr[0]


def maximum(arr):
    arr.sort()
    return arr[-1]


# Fake Binary
# Given a string of digits, you should replace any digit below 5 with '0' 
# and any digit 5 and above with '1'. Return the resulting string.
# Note: input will never be an empty string

def fake_bin(x):
    arr=[]
    for i in x:
        if int(i)>=5:
            arr.append(str(1))
        elif int(i)<=5:
            arr.append(str(0))

    return ("".join(arr))



# Invert values

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    arr = []
    for i in lst:
        arr.append(i * -1)
    return arr

# Sum Arrays
# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can 
# be negative or non-integer. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    return sum(a)


# Calculate average
# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

def find_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)
    

# How good are you really?
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!

def better_than_average(class_points, your_points):
    x=sum(class_points)
    y=len(class_points)
    c=x/y
    if c>your_points:
        return False
    else:
        return True
    

# Calculate BMI
# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    dmi = weight / height ** 2
    if dmi <= 18.5:
        return "Underweight"
    if dmi <= 25:
          return "Normal"
    if dmi <= 30:
         return "Overweight"
    else:
         return "Obese"