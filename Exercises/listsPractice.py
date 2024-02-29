# List
def get_numbers():
    return [1, 2, 3, 4, 5]

# laundry = ["shirts", "socks", "pants"]
# Note that a list is a value. So you can store a list in a variable, just as you can with integers, strings, and booleans.
def get_laundry():
    laundry = ["shirts", "socks", "pants", "shorts"]
    return laundry

# names = ["Alice", "Bob"]

# special_birthdays = [18, 21, 100]

# passwords = ["secret", "1234"]

# valid_modes = [
#     "easy", 
#     "medium", 
#     "hard"
# ] 

# How to use lists
# To write a list:

# start with a left square bracket: [
# write each item separated by commas
# write the right square bracket: ]
# After the left square bracket that begins the list, you can put items on new lines if you think that's more readable.

# Items in a list are sometimes called list elements by programmers.

def zero_one():
    return [0, 1]

# Why use lists?
# Lists are useful when you need to do something with each thing in the list.

# For example, your program could:

# send a mail to each address in a list of emails.
# download each file from a list of links.
# take a list of accounts and follow each one on Twitter.
# store a list of lessons and have the user choose one of them.
# store a list of slides and show them one at a time to the user.
# valid_passwords = ["1234", "123456", "secret"]
# return password in valid_passwords

# Mixing item types
# All the items in a list don't have to be of the same type.

# Write a function, get_mix, that returns a list where:

# the first element is the boolean False
# the second element is the integer 1
# the third element is the string `"three"
def get_mix():
    return[False, 1, "three"]

# One step further
# Lists can contain values of any type.

# You can even put lists inside other lists! Here is an example of this, where a list named examples contains the example lists from a previous slide.

# examples = [
#     ["Alice", "Bob"],
#     [18, 21, 100],
#     ["secret", "1234"],
#     ["easy", "medium", "hard"]
# ]
# It gets easier to think about lists with practice.

# Using lists
# In Python you can use various keywords and functions to do things with lists. For example, you can:

# check if an item is in a list
# take an item out of a list
# concatenate (combine) lists
# insert items into lists
# remove items from lists

def check(password):
    passwords = ["1234", "secret"]
    return password in passwords

def test(x):
    numbers = [11, 22, 33, 44]
    # your code here
    return x in numbers

def is_short(numbers):
    # your code here
    return len(numbers) <= 3

# Concatenating lists
# Previously you saw that you can use the + sign to combine two strings:
# "a" + "b" == "ab"
# Programmers call this concatenating strings.
# You can do the same with lists, using the + sign too:
# [1] + [2] == [1, 2]
def add_123(numbers):
    to_add = [1, 2, 3]
    return numbers + to_add

# Terminology
# When taking an item out of a list at some position, programmers say that you index into the list. For instance, letters[0] is an example of indexing into the letters list at index 0.
xs = [7, 8, 9]
x = xs[1]
print(x)

def third_item(xs):
    return xs[2]

# Indexing into strings
# Indexing works for strings, too. For example:
# "abc"[0] == "a"
# "12345"[3] == "4"

# Indexing by a variable
# You can use a variable as an index, as long as it is an integer small enough to not go out of bounds of the list.
# Here is an example:
# index = 2
# numbers = [1, 2, 3]
# print(numbers[index])
def get_at(numbers, i):
    return numbers[i]

# Modifying a list
# You can use the same square-bracket notation to change a list item at an index.
# Here is an example:
# colors = ["red", "green", "blue"]
# colors[1] = "purple"
# print(colors)
colors = ["red", "green", "blue"]
colors[2] = "pink"
print(colors)

def set_minus1(numbers):
    numbers[0] = -1
    return numbers