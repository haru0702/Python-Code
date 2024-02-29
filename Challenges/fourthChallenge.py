# Challenges IV
# Check if a number is small --> Write a function, is_small, that takes the parameter x. Your function should return True if x is strictly smaller than 10, and False otherwise.
def is_small(x):
    if x < 10:
        return True
    else:
        return False
    
# Password checker -->  Write a function named check that takes a password string as its parameter. check should check if the password is the string "secret".
def check(password):
    return password == "secret"

# Max health --> Write a function named max_health that takes a parameter named mode. If the mode is "easy", max_health should return 100. If the mode is "medium", it should return 75. If the mode is "hard" or any other string, it should return 35.
def max_health(mode):
    if mode == "easy":
        return 100
    elif mode == "medium":
        return 75
    return 35

# Screen height --> Write a function named screen_height that computes the height in pixels of a device screen. Your function should take a single parameter representing a device. If the device is "nexus5x", return 732. If the device is "iphone5", return 568. If the device is "thinkpad", return 1080. Otherwise, if the device is unknown, return -1.
def screen_height(device):
    if device == "nexus5x":
        return 732
    elif device == "iphone5":
        return 568
    elif device == "thinkpad":
        return 1080
    return -1

# Special birthday --> Write a function, special_birthday, that takes a single parameter, age. The function should return True if the age parameter is 18, 21, or at least 100. The function should return False otherwise.
def special_birthday(age):
    return (age == 18 or age == 21 or age >= 100)

# Valid age -->  Write a function, valid_age that returns True if it is given a parameter that is greater than or equal to 0 and less than or equal to 150.
def valid_age(age):
    return age >= 0 and age <= 150

# Stocks --> Write a function named decide that takes a single parameter named price, which is the price of a stock.
# If the price is less than 100, decide should return "buy".
# If the price is between 100 and 150, both inclusive, it should return "hold".
# If the price is strictly above 150, it should return "sell".
# For example:
# decide(99) == "buy"
# decide(100) == "hold"
# decide(150) == "hold"
# decide(151) == "sell"
def decide(price):
    if price < 100:
        return "buy"
    elif price > 150:
        return "sell"
    return "hold"