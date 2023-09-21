#control flow

#Control Flow - controls the flow of your code (make decisions and ignore certain code dependent on factors)

# check if conditions are true before you run a piece of code. Can think of each control flow statement, as a boolean.

# if, elif, else

# if statements - conditions to check against. only do x of y is the case.

#age = 19

#if age > 18:
    #print("you are old enough to watch this movie")

# elif statement is used if there is multiple if statements. less processing power runs only if, if condition is not met.

#film_rating = "U"

#if film_rating.lower() == "u":
#    print("All age groups can watch this movie")
# elif - Less processing power and runs only if if condition is not met.
#elif film_rating.lower() == "pg":
#    print("Parental guidance is advised for this movie")
#elif film_rating.lower() == "12" or "12a":
#    print("People over the age of 12 can watch this movie")
#elif film_rating.lower() == "15":
#    print("People aged 15 or over can watch this movie")
#elif film_rating.lower() == "18":
#    print("People aged 18 can watch this movie")
#else:
#    print("This is not a valid rating, please use 'u', 'pg', '12, or '12a', '15','18")
#else statements - will always run if the if and else conditions aren't met. Way to round of control flow block.

# In python there are no switch statements or case statements. 