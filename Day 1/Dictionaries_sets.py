# What is a dictionary?

# dictionaries use keys and value pairs
# key = the reference to the object
# value = the data storage mechanism you want to use (variable, list, dictionary etc)

# making a dictionary

student_1 = {
    "name": "Luke",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types","operators"]
}

print(student_1)

# accessing data using the key(s)

print(student_1["stream"])

# changing a value in a dict

student_1["completed_lesson"] = 3
print(student_1["completed_lessons"])

# Getting the keys
# print(student_1.keys)() - prints out the keys

# sets and frozen sets
# no order, completely random, no duplicated items
# frozen sets - immutable set ([])