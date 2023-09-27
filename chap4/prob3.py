import random as r

ranNum = r.randrange(1,101)
count = 0
inputNum = -1

print("     Welcome to 'Guess My Number'!")
print("")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("")

while inputNum != ranNum :
  inputNum = int(input("Take a guess: "))
  if inputNum > ranNum :
    print("Lower...")
  elif inputNum < ranNum :
    print("Higher...")
  count = count + 1
print("you guessed it! The number was", ranNum)
print("And it only took you", count, "tries!")
