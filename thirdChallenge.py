# Challenges III
# Returning an integer --> Write a function named f that takes no parameters and always returns an integer. The integer returned is up to you; it could be 0, 1, 123, or something else.
def f():
        return 23

# Returning a boolean --> Write a function called b that takes no parameters and always returns a boolean.
def b():
    return True

# Is it ten? --> Write a function called is_ten that takes one parameter called x. The function must return True if x is 10 and False otherwise.
def is_ten(x):
      if x == 10:
            return True
      else:
            return False
      
# Triple and --> Write a function named triple_and that takes three booleans, combines them with and, and returns the result.
def triple_and(x, y, z):
    return x and y and z

# Inequality test --> Write a function named different that takes two values and tests whether they are different. Return the result
def different(x, y):
      return x != y

# Casts -> Write a function named x that takes a string as its only parameter. The function should cast its input parameter to an integer and add 3 to it. Don't forget to return the result. For example, calling x("0") should return 3 and calling x("123") should return 126.
def x(num):
    return int(num) + 3

# Test or long --> Write a function named test_or_long. The function should take one parameter. The function should return a boolean; that is, it should return either True or False based on the value of the parameter. If the parameter is the string "test" or if its length is 6, test_or_long should return True. Otherwise it should return False.
def test_or_long(x):
    return x == "test" or len(x) == 6

# Day of the month --> Write a function named make_day_string that takes an integer named day and returns the string "it is day X of the month" where X is the value of the day parameter. For example, calling make_day_string(3) should return "it is day 3 of the month". Remember that to concatenate a string with an integer, you must cast the integer to a string. Note that the function should return a value. It should not print anything.
def make_day_string(x):
     return "it is day " + str(x) + " of the month"
#      print("it is day " + str(x) + " of the month")
# make_day_string(3)

