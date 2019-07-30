import random
import math
min = 1
max = 6

def total(roll):
    return sum(sorted(roll, reverse=True)[:3])

def modifier(roll):
    return math.floor((sum(sorted(roll, reverse=True)[:3])-10)/2)

print ("Roll them bones!")
print ("Here's your depressing stats.")
one = [random.randint(min, max) for i in range (4)]
two = [random.randint(min, max) for i in range (4)]
three = [random.randint(min, max) for i in range (4)]
four = [random.randint(min, max) for i in range (4)]
five = [random.randint(min, max) for i in range (4)]
six = [random.randint(min, max) for i in range (4)]


print ("Strength:", total(one), "[", modifier(one),"]")
print ("Dexterity:", total(two), "[", modifier(two),"]")
print ("Constitution:", total(three), "[", modifier(three),"]")
print ("Intelligence:", total(four), "[", modifier(four),"]")
print ("Wisdom:", total(five), "[", modifier(five),"]")
print ("Charisma:",total(six), "[", modifier(six),"]")

