import random

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
selectWord = random.choice(words)
answer = selectWord
strToList = list(selectWord)
random.shuffle(strToList)

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")

str = ''
for i in strToList:
  str += i
    
print("Jumbled word: " + str)
inputStr = input("Your guess: ")

if answer == inputStr :
  print("Correct!")
else :
  print("Sorry, that's not correct. The word was: " + answer)
