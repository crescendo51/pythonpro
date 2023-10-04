import random

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
selectWord = random.choice(words)

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.")
print('')

count = 6

print("Length of the selected word: " + str(len(selectWord)))
