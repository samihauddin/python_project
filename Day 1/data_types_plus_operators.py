# Wat are operators?
# Symbols that excecute a particular mathematical or logical function.

# Arithmetic operators: + - * / %
# Logical comparison operatos: >, <, ==, !=, >=, <=

# Numeric types
# int (whole numbers), float (decimals), complex

# Strings types
# anything involving characters or texts
# in python you can use 'single quotes' or "double quotes"
# double quotes are usually preferred

# string slicing
# this is when you access only a particular part of a string
# assigns a number to each character, first character is ALWAYS 0
# spaces are also characters

# hw = "hello world"
# print(hw[0:5])
#this would print hello
# negative indexing is the reverse using negative numbers; starts from the end

# string methods
# they are codes that have been pre-write, we don't need to know how they work but can just select these and use
# these are in built and can be used to manipulate strings

# strip_string = "Hi my name is luke                  " - can be used to get rid of white spaces
# print(len(strip_string) ; the length of the string
# .count string - used for calculating in the text e.g. how many spaces
# .lower - turns all characters into lowercase
# .capitalise - turns all characters to uppercase
# .replace

# Concatention + casting
# when you join different strings from multiple locations

#a = 1
#b = 2.5
#c = 3

#print(a+b+int(c)) - this is casting
# print9str(a) + "" + str(b) + d)

#f-strings - means you do not need to use casting, makes things easier

#name = "lassie"
#years = 7
#height_cm = 60.2

#print(f"{name}is {years} years old and {height_cm} cm tall")

# Booleans
# either true or false

# rounding in python
# f-strings are the easiest way to do rounding
# pi = 3.1638924781
#print(f"pi to 3 decimal places:{pi:.5f})

# percentages
# score = 16
# max_score = 26
# print(f"you scored {score/max_score}")
# print(f"you scored {score/max_score:%}")
#print(f"you scored {score/max_score:.2%}")