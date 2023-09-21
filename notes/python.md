#### Control Flow

Control Flow - controls the flow of your code. It allows you to make decisions and ignore certain code dependent on factors.

They allow you to check if conditions are true before you run a piece of code.

![Alt Text](Day 2/diagram1.png)
#### If statements
if statements are conditions to check against. 

```
age = 19

if age > 18:
    print("you are old enough to watch this movie")
```

#### Elif statements
elif statement is used if there is multiple if statements. It runs only if, if condition is not met.

```
film_rating = "U"

if film_rating.lower() == "u":
    print("All age groups can watch this movie")
elif film_rating.lower() == "pg":
   print("Parental guidance is advised for this movie")
elif film_rating.lower() == "12" or "12a":
    print("People over the age of 12 can watch this movie")
elif film_rating.lower() == "15":
    print("People aged 15 or over can watch this movie")

```
#### Else statements 

else statements - will always run if the if and else conditions aren't met.

```
film_rating = "U"

if film_rating.lower() == "u":
    print("All age groups can watch this movie")
elif film_rating.lower() == "18":
    print("People aged 18 can watch this movie")
else:
    print("This is not a valid rating, please use 'u', 'pg', '12, or '12a', '15','18")

```
#### LOOPS
A loop is an instruction that repeats multiple times as long as some condition is met. Python uses for only, no 'for each' loops.

#### For Loops

![Alt Text](Day 2/forloop.png)

A for loop in Python is used to iterate over a sequence.

```
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

for num in list_data:
    print(num * 2)
```
#### Nested for loops
```
for data in embedded_lists:
    print(data)
    for num in data:
       print(num)
```
#### Looping through dictionaries
```
for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)
```
#### Getting values for individual keys
```
for items in dict_data.values():
    print(items["money"])
```
#### Loops and if statements
```
for num in list_data:
    if num == 3:
        print("I found 3")
```

#### While loops

For loops are all to do with iterating through a collection. While loops are more like a monitor -> if something is true then act.

![Alt Text](Day 2/whileloop.png)
```
x = 0
while x <10:
    print(f"it's working --> {x}")
    x += 1
```