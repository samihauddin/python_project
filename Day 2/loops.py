# LOOPS
# A loop is an instruction that repeats multiple times as long as some condition is met. Python uses for only, no 'for each' loops.

# For Loops

# A for loop in Python is used to iterate over a sequence.

list_data =[1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson",
        "money": "£0.05"},
    2: {"name": "Masha",
        "money": "£3.66"},
    3: {"name": "Roscoe",
        "money": "£1.14"}
}

#for num in list_data:
#    print(num * 2)

# nested for loops
#for data in embedded_lists:
#    print(data)
#    for num in data:
 #       print(num)

# looping through dictionaries

#for item in dict_data.values():
#    for embed_value in item.values():
 #       print(embed_value)

# get values for individual keys

#for items in dict_data.values():
#    print(items["money"])

# loops and if statements

#for num in list_data:
#    if num == 3:
#        print("I found 3")

# While loops

# For loops are all to do with iterating through a collection.
# While loops are more like a monitor -> if something is true then act.

#x = 0

#while x <10:
#    print(f"it's working --> {x}")
 #   x += 1

