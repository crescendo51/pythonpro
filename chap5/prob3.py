import random

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
selectWord = random.choice(words)
listWord = list(selectWord)
problem = ['_']
for i in range(len(selectWord) - 1) :
    problem += ['_']
count = 6

print(selectWord)
print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.")
print('')

print("Length of the selected word: " + str(len(selectWord)))

while count != 0 :
    print("Remaining attempts:", count)
    print("Current guessed word: ", end =" ")
    print(*problem)
    inputWord = input("Guess a letter: ")

    for j in range(len(selectWord)) :
        if inputWord == listWord[j] :
            problem[j] = inputWord
        
    if inputWord not in selectWord :
        print("Incorrect guess.")
        count -= 1

    if selectWord == ''.join(problem) :
        print("Congratulations! You guessed the word: " + selectWord)
        break;
if selectWord != ''.join(problem) :    
    print("You've used up all your attempts. The correct word was " + selectWord + ".")
