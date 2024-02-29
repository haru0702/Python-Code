#  Conditionals
def is_special(age):
    if age == 21:
        return True
    
    return False

# Conditionals are useful when the behavior of your program should be different depending on some variable or parameter that varies from time to time.

# Here are some examples of things that can be checked with conditionals:

# ------- is the user over 18?
# ------- is the password correct?
# ------- did the user select the "easy" difficulty in my game?
# ------- is there one slide left?
# ------- is there more than one page left to download?

def f(x):
    if x == 42:
        return True
    
def test(n):
    if n == 123:
        print("yay")
    else:
        print("nay")

test(123)
test(333)

def check_special(x):
    if x == 3 or x == 4:
        return "special number"
    else:
        return "not special"

print(check_special(1))
print(check_special(2))
print(check_special(3))
print(check_special(4))

def fixme(number):
    if number == 18 or number == 21:
        return True
    return False

# Comparison
# Sometimes you need to compare two numbers to see which is larger or smaller. The symbols < (less than) and > (greater than) let you do this.
def is_young(age):
    # your code here
    if age < 18:
        return True
    else:
        return False
    
number = 71*13
if (number >= 900):
    print("number is large enough")
    
# Inequality
def not_zero(x):
    return (x != 0)
