""" Storing values in variables """

# A variable is like a box in the computer’s memory where you can store a single value.
# If you want to use the result of an evaluated expression later in your program, you can save it inside a variable.

spam = 40
print(spam)

eggs = 2
print(eggs)

print(spam + eggs + spam)

# When a variable is assigned a new value, the previous value will be forgotten and replaced with the new value.
# This is called overwriting the variable or reassigning a value.

oldValue = "Hello"
print(oldValue)

newValue = "Goodbye"
print(newValue)

# Variable Names.
# Your variable name must obey the following four rules:
# It can't have spaces, it can only use letters, numbers, and have the underscore (_) character.
# It's can't begin with a number.
# It can't be a Python keyword, such as if, or, return or other keywords.
# Variable names are case-sensitive. It is a Python convention to start your variable with a lowercase letter.

old_value = "snake case"
print(old_value)
