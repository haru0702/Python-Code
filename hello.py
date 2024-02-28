from string import ascii_uppercase

x = 13.25
z = float(x) + 100
print(z)

def capital_indexes(s):
    result=[]
    for i in range(len(s)):
        if s[i].isupper():
            result.append(i)
    return result

# example usage
indexes = capital_indexes("HeLlO")
print(indexes)

def capital_indexes(s):
    return[i for i in range(len(s)) if s[i].isupper()]
indexes = capital_indexes("HeLlO")
print(indexes)