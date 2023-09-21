import random

rand_coin = [0,1]
print(random.choice(rand_coin))

if rand_coin == 0:
    print("Heads")
else:
    print("Tails")