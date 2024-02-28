# ---- def function
def f(x):
    result = x + 2
    return result
print(f(1))
print(f(2))
print(f(10))

def g(y):
    return y*5
print(g(10))

def h(a, b):
    result = a + b
    return result
print(h(1,2))
print(h(5,7))

# ---- the def keyword a function name inputs inside the parentheses the function body the return keyword

def add(number):
    result = number + 40
    return result

print(add(15))

def forty_two():
    # add the function body here
    return 42

# add a call here
print(forty_two())

# It is important to understand exactly what happens when Python runs your code.
# Run the code to continue. Make sure you understand why the text "never reached" is not printed.
# If this isn't clear to you, click the Hint button to see a detailed explanation.
def f():
    return 123
    print("never reached")

y = f()
print(y)

# Change the given code. You should change the order of the lines of code in the f function body so that print is called before 123 is returned.
def f():
    print("make this reachable")
    return 123
    

y = f()
print(y)

# Practice II
# Call a function
def add_five(n):
    return n + 5

print(add_five(10))

# your code here
print(add_five(20))

def make_greeting(name):
    greeting = "Hello, " + name
    return greeting

greeting = make_greeting("Alice")
print(greeting)

# your code here
greeting = make_greeting("Bob")
print(greeting)


def square(number):
    return number * number

# your code here
print(square(5))
print(square(50))

name1 = "Camilla"
name2 = "Eve"

def make_greeting(name):
    greeting = "Hello, " + name
    return greeting

# your code here
print(make_greeting(name1))
print(make_greeting(name2))

def square(number):
    return number * number

# your code here
num = len("Alice")
print(square(num))


def square_length(string):
    length = len(string)
    return length * length

# your code here
print(square_length("Bob"))

def show_greeting(name):
    greeting = "Hello, " + name
    print(greeting)

# your code here
def make_greeting():
    greeting = "Hello, " + name
    return greeting
    
show_greeting("Daniel")

def test():
    print("Hello")
print("Goodbye")
test()

def print_happy_birthday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear " + name)
    print("Happy birthday to you")

print("For Alice:")
print_happy_birthday("Alice")

print("And for Bob:")
print_happy_birthday("Bob")

def hello(string):
    print("Hello there, " + string)
hello("Bob")

def goodbye(name):
    print("Goodbye, " + name)

goodbye("Bob")


def multiply(x, y):
    # your code here
    return x * y

print(multiply(5, 7))
print(multiply(2, 3))

def double_up(number):
    return number * 2