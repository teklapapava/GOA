# turtle-თი რენდომ რიცხვებით დახაზეთ შედევრი 
# forward(random.randint(100))

from turtle import *
import random


speed(10000)
colors = ["blue", "purple", "green", "red", "yellow"]
for i in range(1000):
    width(random.randint(1, 15))
    color(random.choice(colors))
    forward(random.randint(0, 100))
    right(random.randint(0, 50))


exitonclick()





