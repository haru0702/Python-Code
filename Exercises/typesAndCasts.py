# Casting from string to int
print(int("999"))

# Casting to strings
x = 42
print(str(x))

compute = 56 * 66
print(str(compute))

def say_age(years):
    print("You are " + str(years) + " years old")

say_age(99)

# Booleans
# Examples of comparing values
print(123 == 123)

age = 30
print(age == 18)

print(42 == 42)

print(8*13+9 == 10*11+3)

# True or False
# inequality
print(3 != 4)

print("abc" != "abc")

# AND and its example
well_fed = False
got_sleep = True

print(well_fed and got_sleep)

print(True and True)

print(True != False and False == False)

# OR and its example
sleepy = False
hungry = True

# your code goes here
print(sleepy or hungry)

print(True == True or False != True or False == False)

# Negation
x = not(False)
print(x)

# Casting to boolean
x = bool(0)
y = bool(1)

# your code goes here
print(x)
print(y)

