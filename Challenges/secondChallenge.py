# Challenges II
# Square --> The code box defines the square function.Call the square function with 5 as an argument and print the result
def square(number):
    result = number * number
    return result

# your code here
print(square(5))

# Add three --> The code box defines a function named add_three. It must be called with three arguments. The function adds all three arguments together and returns the result.Add to the code so that you call the add_three function with arguments 1, 2, and 3. Print the result.
def add_three(a, b, c):
    return a + b + c

# your code here
print(add_three(1,2,3))

# Defining a simple function --> Define a function named f that takes the single parameter x. The function must return 5*x.
def f(x):
    return 5 * x

# Sum of lengths --> Define a function named length_sum that computes the sum of the lengths of two strings.The function length_sum should take two parameters. The two parameters are strings.Your function should compute the length of each string, storing these lengths in variables. Add the lengths together and return the result.
def length_sum(length1, length2):
    result = len(length1) + len(length2)
    return result

print(length_sum("abc","ab"))

# Imperial to metric again --> Define a function named convert that takes two parameters named feet and inches.In the first line of the function body, compute the variable cm like this: cm = 30.48*feet + 2.54*inches Then, on the second line, return the cm variable.
def convert(feet, inches):
    cm = 30.48*feet + 2.54*inches
    return cm

# Multiple functions --> Define two functions, f and g. f should take a parameter named x and return x+3. g should take a parameter named y and return 5*f(y). Note that g uses the result from a call to f to calculate its value. After the two definitions, compute g(3). Remember to print the result. What do you expect? Does the output match?
def f(x):
    return x + 3

def g(y):
    return 5*f(y)

print(g(3))