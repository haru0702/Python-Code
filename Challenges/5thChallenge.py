# Challenges V
# Return a list of strings --> Write a function, three_strings, that returns a list with three items:
# the first item must be "x"
# the second item must be "y"
# the third item must be "z"
def three_strings():
    return ["x", "y", "z"]

# Mode validation --> Write a function, is_valid, that takes the parameter mode. The function must define a list with the strings "easy", "medium", and "hard". If mode is in this list, it is valid. Otherwise it is not.
def is_valid(mode):
    valid_modes = ["easy", "medium", "hard"]
    return mode in valid_modes

# Contains 42 --> Write a function, contains_42, that takes a single list as its parameter. The function should check if the list contains the number 42.
def contains_42(lists):
    return 42 in lists

# Second item --> Write a function, second_item, that extracts and returns the second item of a list that it is given as a parameter.
def second_item(lists):
    return lists[1]

# Double up --> Write a function named double that takes a list, adds the list to itself, and returns the result.
# For example: double([1, 2, 3]) == [1, 2, 3, 1, 2, 3]
def double(numbers):
    return numbers + numbers

# Same length --> Write a function, same_length, that takes two lists and checks if they have the same length.
def same_length(lst, item):
    return len(lst) == len(item)

# Second item with a twist -->  The function second_item below returns the second item in the list l. However, what if l has length 0 or 1? Then taking the second item makes no sense and will result in an error. Change the code so that it detects these cases and returns -1 for lists of length 0 or 1, rather than causing an error. For any other list, the function should still return the second item.
def second_item(l):
    if len(l) > 1:
        return l[1]
    return -1

# First of the first -->  Write a function, first, that takes as input a list of strings. Your function should extract the first element of the list, which is a string. It should then extract the first letter of the string and return it. (If you want extra difficulty, do it in one line of code.)
def first(items):
    return items[0][0]

# Last element --> Write a function named last that uses the len function to extract the last item of a list and return it. For example:
# last([1, 2, 3]) == 3
# last(["a", "b"]) == "b"
def last(numbers):
    return numbers[len(numbers)-1]

# List of lists --> Lists can contain numbers, strings, and other Python values -- including other lists!
# Write a function named nested_lists that defines a list named outer and returns it. The outer list must contain two other lists. You can put whatever you want in these two lists.
def nested_lists():
    outer = [[],[]]
    return outer

