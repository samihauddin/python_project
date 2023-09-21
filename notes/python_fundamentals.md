
### PYTHON FUNDAMENTALS 

#### Variables 

A variable is a reserved memory location used to store data types and objects.<br>
It is a way of organising data.

Example:

a = 1 <br>
b = 2
#### Data types & Operators

There are 3 main built in types of data types:<br>
- Numbers: can be intergers (whole numbers) or floating numbers (decimals)
- Strings: anything involving characters or texts
- Booleans: either True or False

Operators: <br>
Operators are Symbols that excecute a particular mathematical or logical function.

Arithmetic operators: +, -, *, /, % <br>
Logical comparison operators: >, <, ==, !=, >=, <=

String types: <br>
String types are anything involving characters or texts 

String slicing: <br>
This is when you access only a particular part of a string. Python assigns a number to each character and the first chacarter is always 0. Spaces are also included as characters. <br>

String methods:
<br>
There are various string methods in pyhton, they are codes that have been pre-wriiten. W can select these and use them accordingly. 

Concatentaion & casting:<br>

This is when you join different strings from multiple locations 

```
a = 1
b = 2.5
c = 3

print(a+b+int(c)) 
```
F-strings: using f-strings is easier as you do not need to use casting.

```
name = "lassie"
years = 7
height_cm = 60.2

print(f"{name}is{years} years old and {height_cm} cm tall")
```
#### Booleans

Booleans values can only be one or two values; <br>
True (1) or False (0) <br>
They must be capitalised

#### Lists & Tuples

Lists are collections that can store multiple pieces of data inside. In other languages they are alos known as arrays. 
```
shopping_list = ["salad", "eggs", "doughnuts", "milk", "salmon"]
print(shopping_list)
```

List Methods: <br>

There are a number of built in list methods. 

Example 1: Add something to the end of a list 
```
shopping_list.append("carrots") # adds to the end
shopping_list.extend(["water","celery"]) #adds multiple

```

Example 2: Removing items from a list
```
#shopping_list.remove("salad") 
```

Tuples: they cannot be changed, they are immutable

#### Dictionaries

Dictionaries use keys and value pairs <br>
key = the reference to the object
value = the data storage mechanism you want to use (variable, list, dictionary etc)

Example: making a dictionary

```
student_1 = {
    "name": "Luke",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types","operators"]
}
print(student_1)
```