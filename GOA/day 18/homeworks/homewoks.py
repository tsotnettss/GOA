# Introduction
# The first century spans from the year 1 up to and including the year 100, 
# the second century - from the year 101 up to and including the year 200, etc.
# Task Given a year, return the century it is in.
# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
def century(year):
    # Finish this :)
    return year//100+1


# Write a function which converts the input string to uppercase.
def make_upper_case(s):
    return (s.upper())


# Are You Playing Banjo?
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

def are_you_playing_banjo(name):
    
    
    if name[0]=="R":
        return name + " plays banjo"
    elif name[0]=="r":
        return name + " plays banjo"
    else :
        return name + " does not play banjo"
    



# Beginner - Lost Without a Map
# Given an array of integers, return a new array with each value doubled.
# For example:[1, 2, 3] --> [2, 4, 6]

def maps(a):
    new_list=[]
    for i in a:
        a=i*2
        new_list.append(a)
    return new_list 


# Chuck Norris VII - True or False? (Beginner)
# It's a well known fact that anything Chuck Norris 
# wants, he gets. As a result Chuck very rarely has to use the word false.
# It is a less well known fact that if something is true, and Chuck doesn't
# want it to be, Chuck can scare the truth with his massive biceps, and it automatically becomes false.
# Your task is to be more like Chuck (ha! good luck!). You must return false
#  without ever actually using the word false...
# Go show some truth who's boss!

def if_chuck_says_so():
    x=0
    y=1
    return x>y


# Basic Mathematical Operations
# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

def basic_op(operator, value1, value2):
    if operator=="+":
        return value1+value2
    if operator=="-":
        return value1-value2
    if operator=="*":
        return value1*value2
    if operator=="/":
        return value1/value2
    

# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
# For example:

def litres(time):
    return time//2



# MakeUpperCase
# DESCRIPTION:
# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    return (s.upper())