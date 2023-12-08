# Are You Playing Banjo?
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
def are_you_playing_banjo(name):
    
    
    if name[0]=="R":
        return name + " plays banjo"
    elif name[0]=="r":
        return name + " plays banjo"
    else :
        return name + " does not play banjo"
    



# Counting sheep...
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts
# the number of sheep present in the array (true means present).For example,

def count_sheeps(sheep):
    x=0
    for i in sheep:
        if i== True :
            x=x+1
    return x 



# Convert a Boolean to a String
# Implement a function which convert the given boolean value into its string representation.
# Note: Only valid inputs will be given

def boolean_to_string(b):
    if b==True:
        return "True"
    else:
        return "False"
    

# Keep Hydrated!
# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

def litres(time):
    return time//2



# Basic Mathematical Operations
# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    if operator=="+":
        return value1+value2
    if operator=="-":
        return value1-value2
    if operator=="*":
        return value1*value2
    if operator=="/":
        return value1/value2
    

# Beginner - Lost Without a Map
# Given an array of integers, return a new array with each value doubled.

def maps(a):
    new_list=[]
    for i in a:
        a=i*2
        new_list.append(a)
    return new_list 



# Chuck Norris VII - True or False? (Beginner)
# It's a well known fact that anything Chuck Norris wants, he gets. As a result Chuck very 
# rarely has to use the word false.
# It is a less well known fact that if something is true, and Chuck doesn't want it to be, 
# Chuck can scare the truth with his 
# massive biceps, and it automatically becomes false.
# Your task is to be more like Chuck (ha! good luck!). You must return false without ever 
# actually using the word false...
# Go show some truth who's boss!


def if_chuck_says_so():
    x=0
    y=1
    return x>y





# Century From Year
# The first century spans from the year 1 up to and including the year 100, the second century - from the
#  year 101 up to and including the year 200, etc.
# Task
# Given a year, return the century it is in

def century(year):
    if year%100==0:
        return year/100
    return year//100+1


# Beginner Series #2 Clock
# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds

return ((h*3600000)+(m*60000)+(s*1000))