import random
import math
min = 1
max = 6

print ("Roll them bones!")
print ("Here's your depressing stats.")
one = [random.randint(min, max) for i in range (4)]
two = [random.randint(min, max) for i in range (4)]
three = [random.randint(min, max) for i in range (4)]
four = [random.randint(min, max) for i in range (4)]
five = [random.randint(min, max) for i in range (4)]
six = [random.randint(min, max) for i in range (4)]


print ("Strength:", sum(sorted(one, reverse=True)[:3]), "[", math.floor((sum(sorted(one, reverse=True)[:3])-10)/2),"]")
print ("Dexterity:", sum(sorted(two, reverse=True)[:3]), "[", math.floor((sum(sorted(two, reverse=True)[:3])-10)/2),"]")
print ("Constitution:", sum(sorted(three, reverse=True)[:3]), "[", math.floor((sum(sorted(three, reverse=True)[:3])-10)/2),"]")
print ("Intelligence:", sum(sorted(four, reverse=True)[:3]), "[", math.floor((sum(sorted(four, reverse=True)[:3])-10)/2),"]")
print ("Wisdom:", sum(sorted(five, reverse=True)[:3]), "[", math.floor((sum(sorted(five, reverse=True)[:3])-10)/2),"]")
print ("Charisma:",sum(sorted(six, reverse=True)[:3]), "[", math.floor((sum(sorted(six, reverse=True)[:3])-10)/2),"]")
